# _*_ encoding:utf-8 _*_
from django import forms
from django.forms.utils import ErrorList

from .models import UploadFileModel


class NameForm(forms.Form):
    your_name = forms.CharField(label='your name', max_length=20)
    # sex = forms.ChoiceField('male', 'female')


class ContactForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    subject = forms.CharField(max_length=100, help_text='输入主题')
    message = forms.CharField(widget=forms.Textarea)  # widget用以声明charfield类型
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


# 修改表单错误信息显示方式
class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join([
            '<div class="error">%s</div>' % e for e in self
        ])


class ContactFormWithMugshot(ContactForm):
    mugshot = forms.ImageField(help_text='需要上传一张图片')
    choice = forms.ChoiceField(choices=(('fr', 'first'), ('sd', 'second'), ('td', 'third')))


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ['title', 'file']


