from django.shortcuts import render
#import kalenteri
from datetime import datetime
from django.http import HttpResponse


def index(request_id):
      return HttpResponse("Tervetuloa kalenteriin!")


def ohjelmasi(request, year, month):
    name = "Tervetuloa kalenteriisi!"
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(ohjelmasi.month.name).index(month)
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

def kirjaa_ohjelmasi(request):
    ohjelmasi = ohjelmasi.objects.get(id=id)
    context = {'ohjelmasi' : ohjelmasi}

    if request.method == "POST":
        toiminto = request.POST.get("toiminto", "merkitse")
        if toiminto == "kirjaa":
               kirjattu = ohjelmasi.kirjaa(request.user)
               context["kirjattu"] = kirjattu
        elif toiminto == "peru":
             ohjelmasi.poista_kkirjaus(request.user)
             context["kirjattu"] = False
        else:
             raise ValueError(f"Tuntematon toiminto: {toiminto}")
    else:
         kirjattu = ohjelmasi.onko_kirjattu(request.user)       
         context["kirjattu"] = kirjattu

    return render(request, 'kirjaa.html', context)        

# def kalenteri(request, Model):
#     return self.date >= timezone.now()
#     datetime.timedelta(days=1)
    

