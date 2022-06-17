from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PlagForm(FlaskForm):
  checkText = TextAreaField('Enter Here',validators=[DataRequired()])
  submit = SubmitField('Submit')
