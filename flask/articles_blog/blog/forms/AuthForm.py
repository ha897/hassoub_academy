# مصادق الاستمارات 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms. validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models.AuthModel import User

class LoginForm(FlaskForm):
  email = StringField("البريد الالكتروني",validators=[DataRequired(), Email()])
  password = PasswordField("كلمة السر", validators=[DataRequired()])
  remember = BooleanField('تذكرني')
  submit = SubmitField("تسجيل الدخول")

class RegistrationForm(FlaskForm):
  username = StringField("اسم المستخدم", validators=[DataRequired(), Length(min=3, max=30)])
  email = StringField("البريد الالكتروني",validators=[DataRequired(), Email(message="البريد الالكتروني غير صالح")])
  password = PasswordField("كلمة السر", validators=[DataRequired()])
  config_password = PasswordField("تاكيد كلمة السر", validators=[DataRequired(), EqualTo("password",message="كلمة المرور غير متطابقة")])
  submit = SubmitField("انشاء حساب")
  
  # التاكد ان اسم المستخدم والايميل لم يسجل بهم من قبل
  def validate_email(self, field):
    if User.query.filter_by(email=field.data).first():
      raise ValidationError("البريد اللكتروني مسجل سابقة")
    
  def validate_username(self, field):
    if User.query.filter_by(username=field.data).first():
      raise ValidationError("اسم المستخدم مسجل سابقة")
    
class RequestResetForm(FlaskForm):
  email = StringField("البريد الالكتروني",validators=[DataRequired(), Email(message="البريد الالكتروني غير صالح")])
  submit = SubmitField("استعادة كلمة السر")
  
  
  def validate_email(self, field):
    email = User.query.filter_by(email = field.data).first()
    if email is None:
      raise ValidationError("لا يوجد بريد الكتروني مسجل بهذا الاسم")
    
class RequestPasswordForm(FlaskForm):  
  password = PasswordField("كلمة السر", validators=[DataRequired()])
  config_password = PasswordField("تاكيد كلمة السر", validators=[DataRequired(), EqualTo("password",message="كلمة المرور غير متطابقة")])
  submit = SubmitField("تغيير كلمة السر")