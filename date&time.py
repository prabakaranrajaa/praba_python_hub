import datetime as dt
current_date = dt.date(2022,10,22)
print('current date :',current_date)

time = dt.datetime.now()
print(time)

new_year = dt.date(2023,1,1)
curent = dt.datetime.now()
difference = new_year - curent

print(difference)

print('--------------------------------------------')

new = dt.datetime(2022,5,31,12,2,10)
print(new)
print(new.date()) # date shown
print(new.time()) # time shown
