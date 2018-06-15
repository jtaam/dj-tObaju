from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import NewsletterUser, Newsletter


class NewsletterUserSignUpForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False
    helper.add_input(Submit('submit', 'Subscribe'))

    class Meta:
        model = NewsletterUser
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email


class NewsletterCreationForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'body', 'email', 'status']
