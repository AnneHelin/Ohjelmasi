from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# import kalenteri
# from datetime import datetime
from datetime import date
from typing import Any, Dict, Iterable, Mapping, Optional
from django import forms

# def kalenteri(request, year, month):
  #  name = "Tervetuloa kalenteriisi!"
  #  month = month.capitalize()
    # Convert month from name to number
  #  month_number = list(kalenteri.month_name).index(month)
  #  month_number = int(month_number)

    # create  a calendar

def kalenteri(reguest):
    return HttpResponse("Tervetuloa kalenteriin!")    


class DataSelectorWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        days = [(day, day) for day in range(1, 32)]
        month = [(month, month) for month in range(1, 13)]
        years = [(year, year) for year in [2021, 2022, 2023]]
        widgets = [
            forms.Select(attrs=attrs, choices=days),
            forms.Select(attrs=attrs, choices=month),
            forms.Select(attrs=attrs, choices=years),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, date):
            return [value.day, value.month, value.year]
        elif isinstance(value, str):
            year, month, day = value.split("-")
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        day, month, year = super().value_from_datadict(data, files, name)     
        # DateField expects a single string that it can parse into a date.
        return "{}--{}--{}" .format(year, month, day)
    
    def home(request):
        name = "Tervetuloa kalenteriin!"
        return render(request,
                        'home.html' , {
                        "name" : name

                      })