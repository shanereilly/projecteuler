#!/usr/bin/env python3

dayNames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months = ["Jan", "Feb", "March", "Apr", "May", "Jun", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapYear = False

sundayCount = 0

year = 1901
date = 1
dayNum = 1 # Tuesday
monthNum = 0

while year < 2001:
    if dayNum == 6 and date == 1:
        sundayCount += 1
    dayNum = (dayNum + 1) % 7
    date += 1
    if date > monthDays[monthNum]:
        date = 1
        monthNum += 1
        if monthNum > 11:
            monthNum = 0
            year += 1
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                monthDays[1] = 29
            else:
                monthDays[1] = 28


print("{} {} {}, {}".format(dayNames[dayNum], months[monthNum], date, year))
print(sundayCount)
