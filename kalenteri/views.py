from django.shortcuts import render
#import kalenteri
from datetime import datetime
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.utils import timezone
import calendar
from django.template import loader
from django.http import Http404



from .models import Tapahtuma

months = {
     1: "tammikuu",
     2: "helmikuu",
     3: "maaliskuu",
     4: "huhtikuu",
     5: "toukokuu",
     6: "kesäkuu",
     7: "heinäkuu",
     8:  "elokuu",
     9:  "syyskuu",
     10: "lokakuu",
     11: "marrasku",
     12: "joulukuu",
     }

    
def index(request):
    last_Tapahtuma_list = Tapahtuma.objects.order_by
    template = loader.get_template("kalenteri/index.html")
    context = {"last_Tapahtuma_list": last_Tapahtuma_list,
    }
    return HttpResponse(template.render(context, request))
           
def index(request, year=None, month=None):
    if not year:
        year = timezone.now().year
    if not month:
        month = timezone.now().month
    name = "Tervetuloa kalenteriisi!"
    month_name = months[month].capitalize()
    # Convert month from name to number

    Tapahtuma.objects.all()

def etusivu(request, id):
    try:
        tapahtuma = Tapahtuma.objects.get(id=id)
    except Tapahtuma.DoesNotExist:
        return HttpResponseNotFound(f"Tapahtuma {id} ei löydy.")
         
    if request.method == "POST":
        tapahtuma = request.POST.get("toiminto")
        if tapahtuma == "merkitse_merkatuksi":
            tapahtuma.merkattu = True
            tapahtuma.save()
        else:
            return HttpResponseBadRequest("Tuntematon toiminto")
        return render(request, "tervetuloa.html", context={"tapahtuma": tapahtuma })

    # create  a calendar
    # cal = HttpResponse().formatmonth(
    #     year,
    #     month_number)
    # Get current year
    # now = datetime.now() 
    # current_year = now.year
    return render(request,
                    'tervetuloa.html', {
                    
                    "current_year": timezone.now().year,
                    "kalenteri_taulukko": calendar.HTMLCalendar().formatmonth(2023, 5),
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
             ohjelmasi.poista_kirjaus(request.user)
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
    
def paivays(request, tapahtuma_id):
    try:
        tapahtumna = Tapahtuma.objects.get(pk=tapahtuma_id)
    except Tapahtuma.DoesNotExist:
        raise Http404("Sivulla ei tapahtumia")
    return render(request, "kalenteri/detail.html", {"tapahtuma" : tapahtumna})
