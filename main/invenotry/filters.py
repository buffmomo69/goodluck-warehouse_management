# from tkinter.tix import Select
# from typing import Text
from dataclasses import field
import django_filters
from django_filters import CharFilter, ChoiceFilter
from .models import *
from django.forms import TextInput, Select


class MarkaFilter(django_filters.FilterSet):
    # should use the exact name in field_name
    markname = CharFilter(field_name="markname", lookup_expr='icontains',
                          widget=TextInput(attrs={'placeholder': "Marka"}))
    containernumber = Select()

    class Meta:
        model = Marka
        fields = "__all__"
        exclude = ['cbm']
