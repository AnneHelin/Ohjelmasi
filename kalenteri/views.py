from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    return HttpResponse("Tervetuloa kalenteriin")    

def kalenteri(request):
    template = loader.get_template('kalenteri.html')
    return HttpResponse(template, render())


def menosi(request):
    menosi = kalenteri.objects.all()
    context = {
        'menosi' : menosi,

    }
    return render(request, 'listaus.html', context)

def kirjaa_menosi(request, id):
    menosi = kalenteri.objects.get(id=id)
    context = {'menosi' : menosi}

    if request.method == "Post":
        kirjaa = request.POST.get("kirjaa", "merkkaa")
        if kirjaa == 'merkkaa':
            merkattu = menosi.merkkaa(request.user)
            context["merkattu"] = merkattu
        elif merkattu == "poista":
            menosi.poista_menosi(request.user)
            context["merkattu"] = False
        else:
            raise ValueError(f"Tuntematon toiminto: ")
    
        merkattu = menosi.onko_kirjattu(request.user)
        context["merkattu"] = merkattu

    return render(request, 'merkkaa.html', context)