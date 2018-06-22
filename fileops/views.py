# _*_ encoding: utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from .forms import NameForm, ContactForm
# Create your views here.


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            return HttpResponse(form.cleaned_data['your_name'])

    else:
        form = NameForm()
        return render(request, 'form_test1.html', {'form': form})


def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['huangjian17@outlook.com']
            if cc_myself:
                recipients.append(sender)

            # send_mail(subject, message, sender, recipients)
            # return HttpResponse('send mail successfully')
        try:
            # 如何send mail如何设置暂且搁置？
            send_mail(subject, message, sender, recipients)
            return HttpResponse('send mail successfully')
        except:
            return HttpResponse('send failed')
    else:
        form = ContactForm()
        return render(request, 'form_test1.html', {'form': form})