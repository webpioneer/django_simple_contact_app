# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import FormView


from .forms import ContactForm


class ContactView(FormView):

    template_name = 'contact.html'
    success_url = 'contact'
    form_class = ContactForm

    def form_valid(self, form):
        cleaned_data = form.cleaned_data

        recipients_list = settings.RECIPIENTS_LIST

        send_mail(subject='hello',
                  message=cleaned_data['message'],
                  from_email=cleaned_data['email'],
                  recipient_list=recipients_list)

        return super(ContactView, self).form_valid(form)
