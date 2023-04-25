from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import kalenteri
from datetime import datetime

def kalenteri(request, year, month):
    name = "Tervetuloa kalenteriisi!"
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(kalenteri.month_name).index(month)
    month_number = int(month_number)

    # create a calendar
    cal = (
        year, 
        month_number)
    
    # Get current year
    now = datetime.now()
    current_year = now.year
    
    # Get current time
    time = now.strftime('%I:%M: %p')
    return render(request,
                'kalenteri.html', {
                "name": name,
                "year": year,
                "month": month,
                "month_number": month_number,
                "cal" : cal,
                "current_year": current_year,
                "time" : time,
    })



