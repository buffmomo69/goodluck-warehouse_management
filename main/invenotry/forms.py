from pyexpat import model
from django import forms
from django.forms import TextInput, Select, NumberInput
from invenotry.models import Marka, Container, Firm


class StockEntryForm(forms.ModelForm):
    class Meta:
        model = Marka
        fields = '__all__'
        widgets = {
            "markname":
                TextInput(
                    attrs={
                        'class': "form-control",
                        'placeholder': 'Mark Name',
                        'required': 'True',
                    }, ),

            "cartoon":
                NumberInput(attrs={
                    'class': "form-control",
                    'placeholder': 'Cartoon Number',
                    'required': 'True',
                }),

            "cbm":
                TextInput(attrs={
                    'class': "form-control",
                    'placeholder': 'CBM',
                    #  'required': 'False',
                }),

            "containernumber":
                Select(attrs={
                    'class': "form-select form-control form-floating ",
                    'placeholder': 'Container Number',
                    'required': 'True',

                }),

        }
        error_messages = {

            'markname': {
                'required': "Please enter marka name",
            },

            'cartoon': {
                'required': "Please enter cartoon number for the lot",
                'number': "Please enter a number"

            }
        }


class ContainerEntryForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = '__all__'
        widgets = {
            "ContainerNumber":
                TextInput(
                    attrs={
                        # 'label':"Container Number",
                        'class': "form-control",
                        'placeholder': 'Container Number',
                        'required': 'True',
                    }, ),

            "firm_name":
                Select(attrs={
                    'class': "form-select form-control",
                    'placeholder': 'Company Name',
                    'required': 'True',

                }),

        }


class FirmEntryForm(forms.ModelForm):
    class Meta:
        model = Firm
        fields = '__all__'

