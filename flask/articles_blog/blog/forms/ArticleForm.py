from flask_wtf import FlaskForm
from wtforms. validators import DataRequired, Length
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from flask_ckeditor import CKEditorField

class ArticleForm(FlaskForm):
    # نوع بيانات سترنج
    # DataRequired نحدده حقل اجباري
    # Length نحدد الطول
    title = StringField("عنوان المقاله", validators=[DataRequired(), Length(min=5, max=255)])
    # ملف
    # FileAllowed الامتدادات المسموحة
    artical_img = FileField("صورة المقالة", validators=[FileAllowed(['jpg', 'png'])])
    # نص
    # content = TextAreaField("محتوى المقاله", validators=[DataRequired(), Length(min=100, max=10000)])
    content = CKEditorField("محتوى المقاله", validators=[DataRequired(), Length(min=100, max=10000)])
    # خانة ارسال
    submit = SubmitField("نشر المقاله")