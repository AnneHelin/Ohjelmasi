from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("Tervetuloa kalenteriisi!")

def tapahtuma_view(request):
    kaikki_tapahtumat = Tapahtuma.objects.all()
    get_tapahtuma_types = Tapahtuma.objects.only('Tapahtuma tyyppi')

    
# If filters applied then get parameter and filter based on condition else return
def Tapahtuma(request):
    if request.GET:
        Tapahtuma = []
        if request.GET.get('tapahtuma_type') == "all":
            all_tapahtuma = Tapahtuma.objects.all()
        else:
            all_tapahtuma = Tapahtuma.objects.filter(tapahtuma_type__icontains=request.GET.get('tapahtuma_type'))

        for i in all_tapahtuma:
            tapahtuma_sub_arr = {}
            tapahtuma_sub_arr['title'] = i.tapahtuma_name
            aloitus_aika = datetime.datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            lopetus_aika = datetime.datetime.strftime(str(i.end_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            tapahtuma_sub_arr['aloitus'] = aloitus_aika
            tapahtuma_sub_arr['lopetus'] = lopetus_aika
            Tapahtuma.append(tapahtuma_sub_arr)
            return HttpResponse()
        
        context = {
           
        }
        return render(request,'admin/kalenteri/tapahtuma_management.html', context)
   