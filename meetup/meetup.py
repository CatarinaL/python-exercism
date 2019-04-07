import calendar
from datetime import date

class MeetupDayException(Exception):
    pass

def meetup_day(year, month, day_of_the_week, which):
    #create a calendar object
    cld = calendar.Calendar()
    monthdays = cld.itermonthdays2(year, month)
    weekdays = {"Monday": 0,
                "Tuesday": 1,
                "Wednesday": 2,
                "Thursday": 3,
                "Friday": 4,
                "Saturday": 5,
                "Sunday": 6}
    which_weekday = {"1st": 0,
                    "2nd": 1,
                    "3rd": 2,
                    "4th": 3,
                    "5th": 4,
                    "last": -1
                    }
    possible_days = [day for day, weekday in monthdays if (weekday == weekdays[day_of_the_week] and day != 0)]
    if which == "teenth":
        which_day = [day for day in possible_days if (day >= 13 and day <= 19)][0]
    elif which_weekday[which] < len(possible_days):
        which_day = possible_days[which_weekday[which]]
    else:
        raise MeetupDayException("No date found for your parameters.")
    #print(year, month, day_of_the_week, which, date(year, month, which_day))
    return date(year, month, which_day)
'''   
print(meetup_day(2019, 4, "Monday", "1st"))
print(meetup_day(2018, 4, "Monday", "1st"))
print(meetup_day(2019, 3, "Sunday", "1st"))
'''