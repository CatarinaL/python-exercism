import calendar
from datetime import date

class MeetupDayException(Exception):
    pass


WEEKDAYS = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}
WHICH_WEEKDAY = {
    "1st": 0,
    "2nd": 1,
    "3rd": 2,
    "4th": 3,
    "5th": 4,
    "last": -1
}


def get_possible_week_days(year, month, day_of_the_week):
    cld = calendar.Calendar()
    monthdays = cld.itermonthdays2(year, month)
    return [day for day, weekday in monthdays if (weekday == WEEKDAYS[day_of_the_week] and day != 0)]


def meetup_day(year, month, day_of_the_week, which):
    possible_days = get_possible_week_days(year, month, day_of_the_week)
    if which == "teenth":
        which_day = [day for day in possible_days if (day >= 13 and day <= 19)][0]
    elif WHICH_WEEKDAY[which] < len(possible_days):
        which_day = possible_days[WHICH_WEEKDAY[which]]
    else:
        raise MeetupDayException("No date found for your parameters.")

    return date(year, month, which_day)
