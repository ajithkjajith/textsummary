
from flask import  render_template , url_for  , redirect , request
from TextSummerization.forms import  SummerizeForm
from TextSummerization import app
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import bs4 as bs
import urllib.request
import os


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/summerize" , methods=['GET','POST'])
def summerize():
    print('Summerize')
    form = SummerizeForm()
    # ('#summerizeId').hide()
    if form.validate_on_submit():
        if form.url.data is "" :
           tokenized_result = tokenize(form.text.data,form.length.data)          
        else:
           tokenized_result = fetch_data_from_url(form.url.data,form.length.data)
        form.result = tokenized_result['summary']
        return render_template('summerize.html',form=form)
    return render_template('summerize.html' , title='Summerize' , form=form)

def fetch_data_from_url(url,n):
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source,'lxml')

    for sup in soup.findAll('sup'):
       sup.decompose()
    
    para_txt = ""
    for paragraph in soup.find_all('p'):
        para_txt = str(para_txt + paragraph.text)
    return tokenize(para_txt,n)

def tokenize(text,n):
    text = text.replace("’","")
    sents=sent_tokenize(text)
    word_sent = word_tokenize(text.lower())
    stopw = set(stopwords.words('english')+list(punctuation)) 
    word_sent = [word for word in word_sent if word not in stopw]

    from nltk.probability import FreqDist
    freq = FreqDist(word_sent)

    from collections import defaultdict
    ranking = defaultdict(int)
    for i,sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]
    from heapq import nlargest
    sents_idx = nlargest(n,ranking,key=ranking.get)

    return {'talkingabout' : nlargest(5,freq,key=freq.get), 'summary': [sents[j] for j in sorted(sents_idx)]}

