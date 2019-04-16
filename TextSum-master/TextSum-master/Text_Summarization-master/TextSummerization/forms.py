from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField  , SubmitField , BooleanField , TextAreaField , SelectField
from wtforms.validators import DataRequired , Length , Email , EqualTo ,ValidationError
from flask_wtf.file import FileField , FileAllowed

class SummerizeForm(FlaskForm):
    text = TextAreaField('')
    length = SelectField(u'Length of Summary', coerce=int ,choices=[(3, '3'), (4, '4'), (5, '5'),(6, '6'), (7, '7'), (8, '8'),(9, '9'), (10, '10'), (11, '11')])
    file = FileField('Upload File',validators=[FileAllowed(['pdf','doc'])])
    url = StringField('Url/Link')
    result = TextAreaField('Result')
    submit = SubmitField('Summerize')   