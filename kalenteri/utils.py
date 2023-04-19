from datetime import datetime, timedelta
from kalenteri import HTMLKalenteri
from .models import Tapahtuma

class Kalenteri(HTMLKalenteri):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Kalenteri, self).__init__()

        # Päivien muotoilu
        # Kaventaa tapahtumia päivän mukaan
    def formatday(self, date, tapahtumat):
            tapahtumat_per_date = tapahtumat.filter(start_time_date=date)
            date = ''
            for tapahtuma in tapahtumat_per_date:
                    date += f'<li> {tapahtuma.title} </li>'

            if date != 0:
                  return f"<td><span class= 'date'>{date}</span><ul>  </ul></td>"
            return '<td></td>'
    
    # Viikkojen muotoilu
    def weekly(self, week, tapahtuma):
            week = ''
            for day, weekday  in week:
                    week += self.weekly(day, tapahtuma)
            return f'<tr> {week} </tr>'
                
    
    # Kuukausien muotoilu
    # Tapahtumien järjestäminhen vuoden ja kuukausien mukaan
    def month(self, withyear=True):
           tapahtuma = Tapahtuma.objects.filter(aloitus_aika_vuosi=self.year, aloitus_aika_kuukausi=self.month)

           kalenteri = f'<table border="0" cellpadding= "0" cellspacing="0" class="kalenteri">\n'
           kalenteri += f'{self.monthname(self.year, self.month, withyear=withyear)}\n'
           kalenteri += f'{self.weekheader()}\n'
           for week in self.monthdays2calendar(self.year, self.month):
                  kalenteri += f'{self.weekly(week, tapahtuma)}\n'
           return kalenteri       

