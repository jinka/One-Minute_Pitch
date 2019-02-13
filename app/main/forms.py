
from flask_wtf import FlaskForm


from wtforms.validators import Required,Email
from ..models import User

from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
# from wtforms.validators import 
from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Say something about you.',validators = [Required()])
    submit = SubmitField('Submit')

# S Pitch
class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):

    title = StringField('New Pitch',validators=[Required()])
    text = TextAreaField('Text',validators=[Required()])
    category = SelectField('Type',choices=[('interview','Interview pitch'),('product','Product pitch'),('promotion','Promotion pitch')],validators=[Required()])
    submit = SubmitField('Submit')
#E Pitch