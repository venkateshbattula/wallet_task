from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.forms import ModelForm, RadioSelect
from .models import *
from django.utils.translation import gettext as _


class addWalletForm(ModelForm):
    class Meta:
        model = userWallet
        fields = "__all__"

        labels = {'status': _('Select Status')}

    def clean_status(self):
        input_status = self.cleaned_data['status']
        if input_status is False:
            raise ValidationError('Please enable your wallet status')
        return input_status


class addmonettowallet(ModelForm):
    class Meta:
        model = userWallet
        fields = "__all__"

        labels = {'status': _('Select Status')}

    def clean_status(self):
        input_status = self.cleaned_data['status']
        if input_status is False:
            raise ValidationError('Please enable your wallet status')
        return input_status

    def amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise ValidationError('Add amount should be minimum is "1" or more')
        return amount
