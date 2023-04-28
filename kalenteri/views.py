from django.shortcuts import render
import kalenteri
from datetime import datetime


def kalenteri(request, year, month):
    name = "Tervetuloa kalenteriisi!"
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(kalenteri.month_name).index(month)
    month_number = int(month_number)

    # create  a calendar
