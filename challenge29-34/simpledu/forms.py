#!/usr/bin/env python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, DataRequired, URL, NumberRange,Regexp
from simpledu.models import db, User, Course, Live
from wtforms import ValidationError, TextAreaField, IntegerField

class RegisterForm(FlaskForm):
    #username = StringField('用户名', validators=[DataRequired(), Regexp(r'^[0_9a_zA_Z]{3,24}$', message='用户名只能包含数字和字母， 长度在3到24之间')])
    username = StringField('用户名', validators=[DataRequired(), Length(3, 24)])
       # Length(3, 24)])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    repeat_password = PasswordField(
            '重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('提交')

    def create_user(self):
        user = User()
        self.populate_obj(user)
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user
    
    def validate_username(self, field):
        if not field.data.isalnum():
            raise ValidationError('用户名只能包含数字和字母')
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')

class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(3, 24)])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_eamil(self, field):
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱未注册')

    def validate_password(self, field):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')

class CourseForm(FlaskForm):
    name = StringField('课程名称', validators=[DataRequired(), Length(5, 32)])
    description = TextAreaField(
            '课程简介', validators=[DataRequired(), Length(20, 256)])
    image_url = StringField('封面图片', validators=[DataRequired(), URL()])
    author_id = IntegerField('作者ID', validators=[DataRequired(), NumberRange(
        min=1, message='无效的用户ID')])
    submit = SubmitField('提交')

    def validate_author_id(self, field):
        if not User.query.get(field.data):
            raise ValidationError('用户不存在')

    def create_course(self):
        course = Course()
        # 使用课程表单数据填充 course 对象
        print('--------------------------------')
        print(self.populate_obj.__doc__)
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

    def update_course(self, course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

class LiveForm(FlaskForm):
    name = StringField('直播名称', validators=[DataRequired(), Length(1, 256)])
    user_id = IntegerField('用户ID', validators=[DataRequired(), NumberRange(min=1, message=('无效的用户ID'))])
    submit = SubmitField('提交')

    def validate_user_id(self, field):
        if not User.query.get(self.user_id.data):
            raise ValidationError('用户不存在')

    def create_live(self):
        live = Live()
        self.populate_obj(live)
        db.session.add(live)
        db.session.commit()
        return live

    def update_live(self, live):
        self.populate_obj(live)
        db.session.add(live)
        db.session.commit()
        return live

class MessageForm(FlaskForm):
    text = StringField('发送后台消息', validators=[DataRequired(), Length(1, 256)])
    submit = SubmitField('提交')
