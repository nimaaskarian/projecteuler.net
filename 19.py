def is_century(year):
    return year%100 == 0

def is_leap_year(year):
    if is_century(year):
        return year%400 == 0
    return year%4 == 0 

def months(year):
    if is_leap_year(year):
        feb = 29
    else:
        feb = 28
    return [31,feb,31,30,31,30,31,31,30,31,30,31]

def days(year):
    return sum(months(year))

# 0: sun, 1: mon, 2: tue, 3: wed, 4: thu, 5: fri, 6: sat
def gen_20th_century_first_day_of_month_sundays():
    first_day_1900 = 1
    start = (first_day_1900 + days(1900))%7
    for year in range(1901, 2001):
        for month in months(year):
            if start == 0:
                yield 1
            start=(start+month)%7

sundays_count = sum(gen_20th_century_first_day_of_month_sundays())
print(sundays_count)
