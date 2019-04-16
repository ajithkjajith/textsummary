from flask import Flask 



app = Flask(__name__)
app.config['SECRET_KEY'] = '39fe1dd9ee4672c0c1bb3c2c048b584c'

from TextSummerization import routes