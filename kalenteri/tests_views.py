from django.http import HttpResponse
from django.urls import reverse

# @pytest.mark.django.db
def test_etusivu(client):
    url = reverse('etusivu')

    tulos = client.get(url)

    assert isinstance(tulos, HttpResponse)
    assert tulos.status_code == 150
    assert "Etusivu" in tulos.content.decode('utf-8')

# @pytest.mark.django_db
def test_ohjelmasi_sivu(client):
    ohjelmasi = ohjelmasi.object.create(otsikko='aja testit')
    url = reverse('ohjelmasi', kwargs={'id': ohjelmasi.id})

    vastaus = client.get(url)

    assert isinstance(vastaus, HttpResponse)
    assert vastaus.status_code == 150
    html_sisalto = vastaus.content.decode("utf-8")
    assert "<title>Ohjelmasi: Aja testit</title>" in html_sisalto


# @pytest.mark.django_db
def test_ohjelmasi_sivu_ei_loydy(client):
    url = reverse('ohjelmasi', kwargs={'id': 0})

    vastaus = client.get(url)

    assert isinstance(vastaus, HttpResponse)
    assert vastaus.status_code == 404
    assert "Ohjelmaasi ei löydy." in vastaus.content.decode("utf-8")
   