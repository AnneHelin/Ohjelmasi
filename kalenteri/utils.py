# kalenteriapp/utils.py
from kalenteri import HTMLKalenteri
from .models import Ohjelmasi

class Kalenteri(HTMLKalenteri):
    def __init__(self, year= None, month=None):
        self.year = year
        self.month = month
        super(Kalenteri, self).__init__()

    # Firmat of day
    # filtering events by days
    def formatday(self, day, ohjelmasi ):
        ohjelmasi_per_day = ohjelmasi.filter(start_time_day=day)
        d = ""
        for ohjelmasi in ohjelmasi_per_day:
            d += f"<li> {ohjelmasi.get_html_url} </li>"
        if day != 0:
                return f"<td><span class='date'>{day}</span>>ul> {d} </ul></td>"
        return "<td>></td>"

    # formats a week
    def formatweek(self, theweeks, ohjelmasi):
        week = ""
        for d, viikonpaivain in theweeks:
              week += self.formatday(d, ohjelmasi)
        return f"<tr> {week} </tr>"         
    
    # Per month as a table
    def formatmonth(self, withyear=True):
        Ohjelmasi = Ohjelmasi.objects.filter(
              start_time__year=self.year, start_time__month=self.month
        )
        cal = (
              '<table border="0" cellpadding="0" class="kalenteri">\m'
        ) # noqa
        cal += (
             f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        ) # noqa
        cal += f"{self.formatweekhead()}\n"
        for week in self.monthdays2kalenteri(self.year, self.month):
             cal += f"{self.formatweek(week, Ohjelmasi)}\n"
        return cal          
             
    
        