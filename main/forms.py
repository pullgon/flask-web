# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2020/8/20 23:51
# Description: 表单处理

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

