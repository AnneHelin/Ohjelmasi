from kalenteri import HTMLKalenteri
from datetime import datetime as dtime, date, time
import datetime
from models import Tapahtuma
from django import utils

class TapahtumaKalenteri(HTMLKalenteri):
    def _init__(self, tapahtuma=None):
        super(TapahtumaKalenteri, self).__init__()
        self.tapahtuma = tapahtuma

    def formatday(self, paiva, viikko, tapahtumat):
        """show the days """   

        tapahtuma_from_paiva = tapahtumat.filter(paiva_paiva=paiva)
        tapahtuma_html = "<ul>"
        for tapahtuma in tapahtuma_from_paiva:
            tapahtuma_html += tapahtuma.get_absolute_url() + "<br>"
        tapahtuma_html += "</ul>"    

        if paiva == 0:
            return '<td class="eipaiva">;</tb>'
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[viikko], paiva.tapahtuma.html) 

    def formatweek(self, theweek, events):
        pass

    
        