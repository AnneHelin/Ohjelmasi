from kalenteri import HTMLKalenteri
from datetime import datetime as datetime, date, time
import datetime
from models import Ohjelmasi

class OhjelmasiKalenteri(HTMLKalenteri):
    def __init__(self, ohjelmasi=None):
        super(OhjelmasiKalenteri, self).__init__()
        self.ohjelmasi = ohjelmasi

    def muoto(self, paiva, viikko, ohjelmasi):
        """Päivän palutus
        """
        ohjelmasi_from_day = ohjelmasi.filter(day__day=paiva)
        ohjelmasi_html = "<ul>"
        for ohjelmasi in ohjelmasi_from_day:
            ohjelmasi_html += ohjelmasi.get_absolute_url() + "<br>"
        ohjelmasi_html +="</ul>"

        if paiva == 0:
            return '<td class="boday">&nbsp;</td>' # Day of the following month
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[viikko], paiva, ohjelmasi_html)
         
        def viikonmuotoilu(self, viikko, ohjelmasi):
            """Palauttaa viikon riveinä
            """
            s = ''.join(self.päivämuotoilu(d, wd, ohjelmasi) for (d, wd) in viikko)
            return '<tr>%s</tr>' % s
        
        def kuukausimuotoilu(self, kuukausi, ohjelmasi):
            """Palauttaa kuukauden riveinä
            """ 
            ohjelmasi = Ohjelmasi.objects.filter(day_month=month)

            v = []
            a = v.append
            a('<table border="0" cellpadding = "0" cellspacing="0" class="month">')
            a('\n')
            a(self.kuukausimuotoilu(vuosi, kuukausi, vuosi=vuosi))
            a('\n')
            a(self.viikkomuotoilu())
            a('\n')
            for viikko in self.kuukaudenpaivat2kalenteri(vuosi, kuukausi):
                a(self.viikkomuotoilu(viikko, ohjelmasi))
                a('\n')
            a('</table>')
            a('\n')
            return '', join(v)                                


