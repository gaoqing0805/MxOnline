#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name: forms.py
Author: cyan
Time: 2019/8/17 17:54
Desc: 
"""
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

