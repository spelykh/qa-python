__author__ = 'Stepan_Pelykh'


from datetime import datetime

formats = ('%d %b %Y', '%d %B %Y', '%d.%m.%Y', '%m/%d/%y')


def string_to_date(date):
    for a in formats:
        try:
            b = datetime.strptime(date, a).date()
            print(b)
        except ValueError:
            pass

dates = ('11 Jan 2016', '4 April 2011', '11.03.2014', '03/24/91')

for x in dates:
    string_to_date(x)