# _*_ encoding:utf-8 _*_
from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='your name', max_length=20)
    # sex = forms.ChoiceField('male', 'female')


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)  # widget用以声明charfield类型
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)






