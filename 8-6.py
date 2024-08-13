from datetime import date

day_now = date.today()
print(day_now)

xday = date(2024, 4, 5)
td = day_now - xday
print(td)
print(type(td))

