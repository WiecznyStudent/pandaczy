# -*- uft-8 -*-

from datetime import date

today_date = date.today()

day_of_month = today_date.strftime('%j')

print('Dzisiaj jest %s dzień %s roku' % (str(day_of_month), str(today_date.year)))
