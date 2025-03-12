from datetime import date, timedelta

# yesterday = date.today().day - 1
# print(yesterday.day)
# yesterday = yesterday.day - 1
# print(yesterday)

today = date.today()
a_day_ago = timedelta(days=1)
yesterday = today - a_day_ago
print(yesterday)
print(yesterday.day)
print(yesterday.month)
print(yesterday.year)