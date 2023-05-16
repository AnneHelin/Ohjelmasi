from django.shortcuts import render
#import kalenteri
from datetime import datetime
from django.http import HttpResponse

def index(request, kalenteri_id):
    return HttpResponse("Tervetuloa kalenteriin!")


def kalenteri(request, year, month):
    name = "Tervetuloa kalenteriisi!"
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(kalenteri.month_name).index(month)
    month_number = int(month_number)

    # create  a calendar
    cal = HttpResponse().formatmonth(
        year,
        month_number)
    # Get current year
    now = datetime.now() 
    current_year = now.year
    return render(request,
                    'tervetuloa.html', {
                    "name" : name,
                    "year" : year,
                    "month" : month,
                    "month_number" : month_number,
                    "current_year": current_year,
                  })

# def kalenteri(request, Model):
#     return self.date >= timezone.now()
#     datetime.timedelta(days=1)


