import traceback
import numpy as np
import pendulum as pdl
import pandas as pd
import math
import datetime
from datetime import datetime
import calendar


# def SECOND(date_str):
#     parsed = pdl.parse(date_str, exact=True, strict=False)
#     return parsed.second
#
#
# def TODAY():
#     return pdl.today()
#
#
# def DATESBETWEEN(start_date, end_date, interval):
#     start = pdl.parse(start_date, exact=True)
#     end = pdl.parse(end_date, exact=True)
#     period = pdl.period(start, end)
#     dates_between = None
#     if interval == "months":
#         dates_between = [dt.strftime("%Y-%m-%d") for dt in period.range('months')]
#     elif interval == "days":
#         dates_between = [dt.strftime("%Y-%m-%d") for dt in period.range('days')]
#     return dates_between
#
#
# def ENDOFMONTH(date_str):
#     pass
#
#
# def WEEKDAY(date_str):
#     c = pdl.parse(date_str, exact=True)
#     print("weekday", c.weekday())
#     return c.weekday()


def ADD_MONTHS(date_str, months):
    date = pdl.parse(date_str, exact=True, strict=False)
    return str(date.add(months=months))


def ADD_DAYS(date_str, days):
    date = pdl.parse(date_str, exact=True, strict=False)
    return str(date.add(days=days))


def CONVERT_TZ(date_str, to_tz_zone, from_tz_zone=None):
    date = pdl.parse(date_str, exact=True, strict=False)
    if from_tz_zone is not None:
        dt = date.in_tz(from_tz_zone).in_tz(to_tz_zone)
    else:
        dt = date.in_tz(to_tz_zone)
    return dt


def CURRENT_DATE():
    pass


def CURRENT_TIME():
    pass


def CURRENT_TIMESTAMP():
    pass


def DATE_FUNCTION():
    pass


def DATEDIFF(date_1, date_2, interval):
    try:
        date_1 = pdl.parse(date_1, exact=True, strict=False)
        date_2 = pdl.parse(date_2, exact=True, strict=False)
        delta = None
        if interval == 'SECONDS':
            delta = date_1.diff(date_2).in_days()
        elif interval == "HOURS":
            delta = date_1.diff(date_2).in_hours()
        elif interval == "MINUTES":
            delta = date_1.diff(date_2).in_minutes()
        elif interval == "DAYS":
            delta = date_1.diff(date_2).in_days()
        return delta
    except Exception as e:
        traceback.print_exc()
        print(e)


def DATES_ADD(date_str, no_of_intervals, interval):
    date_1 = pdl.parse(date_str, exact=True)
    dates_add = None
    if np.sign(no_of_intervals) == 1:
        if interval == "years" or interval == "YEARS":
            dates_add = date_1.add(years=no_of_intervals)
    else:
        if interval == "years" or interval == "YEARS":
            dates_add = date_1.subtract(years=abs(no_of_intervals))
    dates_add = dates_add.to_datetime_string()
    return dates_add


def DATE_FORMAT(date_str, format):
    format_date = datetime.strptime(date_str, format=format)
    return format_date


def DATES_SUBTRACT():
    pass


def DAY_NAME(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    day_name = date.strftime("%A")
    return day_name


def DAY_OF_MONTH(date_str):
    dt = pdl.parse(date_str, exact=True, strict=False)
    return dt.day


def DAY_OF_WEEK(date_str):
    dt = pdl.parse(date_str, exact=True, strict=False)
    return dt.day_of_week


def DAY_OF_YEAR(date_str):
    dt = pdl.parse(date_str, exact=True, strict=False)
    return dt.day_of_year


def EXTRACT():
    pass


def FROM_DAYS():
    pass


def FROM_UNIXTIME():
    pass


def GET_FORMAT():
    pass


def HOUR(date_str):
    parsed = pdl.parse(date_str, exact=True, strict=False)
    return parsed.hour


def LAST_DATE_OF_MONTH(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    last_date_of_month = date.replace(day=calendar.monthrange(date.year, date.month)[1])
    print(last_date_of_month)
    return last_date_of_month


def LAST_DAY_OF_MONTH(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    # monthrange() gets the date range
    # required of month
    last_day_of_month = calendar.monthrange(date.year, date.month)[1]
    return last_day_of_month


def MAKEDATE(year, month, day):
    make_date = datetime.datetime(year, month, day)
    return make_date


def MAKETIME(hour,minute, second):
    make_time = datetime.time(hour, minute, second)
    return make_time


def MICROSECOND(date_str):
    parsed = pdl.parse(date_str, exact=True, strict=False)
    return parsed.microsecond


def MINUTE(date_str):
    parsed = pdl.parse(date_str, exact=True, strict=False)
    return parsed.minute


def MONTH(date_str):
    parsed = pdl.parse(date_str, exact=True, strict=False)
    return parsed.month


def MONTHNAME(date_str):
    dt = pdl.parse(date_str, exact=True, strict=False)
    return dt.format(MONTHNAME(date_str))


def NOW():
    return pdl.now()


def PERIOD_ADD():
    pass


def PERIOD_DIFF():
    pass


def QUARTER(date_str):
    q = pdl.parse(date_str, exact=True, strict=False)
    return q.quarter


def SECOND_FROM_TIME(time_str, format):
    get_time = datetime.strptime(time_str, format=format)
    seconds = get_time.second
    return seconds


def SEC_TO_TIME(seconds):
    sec_to_time = datetime.timedelta(seconds=seconds)
    return sec_to_time


def STR_TO_DATE(date_str, format):
    str_to_date = datetime.strptime(date_str, format)
    return str_to_date


def SUBTRACT_DATE(date_str, no_of_days):
    date = pdl.parse(date_str, exact=True, strict=False)
    subtracted_date = date.subtract(days=no_of_days)
    return subtracted_date


def SUBTRACT_TIME():
    pass


def TIME_FUNCTION():
    pass


def TIME_DIFF():
    pass


def TIMESTAMP_FUNCTION():
    pass


def TIMESTAMP_ADD():
    pass


def TIMESTAMP_DIFF():
    pass


def TIME_FORMAT():
    pass


def TIME_TO_SEC():
    pass


def TO_DAYS():
    pass


def TO_SECONDS():
    pass


def UNIX_TIMESTAMP():
    pass


def UTC_DATE():
    pass


def UTC_TIME():
    pass


def UTC_TIMESTAMP():
    pass


def WEEK():
    pass


def WEEKDAY():
    pass


def WEEKOFYEAR():
    pass


def YEAR():
    pass


def YEARWEEK():
    pass


def week_of_month(date_str):
    c = pdl.parse(date_str, exact=True)
    print("week_num", c.week_of_month)
    return c.week_of_month


def distinct_count(input_list):
    l1 = []
    count = 0
    for item in input_list:
        if item not in l1:
            count += 1
            l1.append(item)
    print("No of unique items are:", count)
    return count


def days_btw_two_dates(date1, date2):
    return abs(date2-date1).days


def search_string_in_list(input_list, search_string):
    index_list = []
    i = 0
    for e in input_list:
        if search_string in e.lower():
            index_list.append(i)
        i += 1
    return index_list


def create_new_column(col_names, col_values):
    res = {}
    df = pd.DataFrame(col_values, columns=col_names)
    df["col3"] = df['budget'] + df['actual']
    res["columns"] = df.columns.tolist()
    res["values"] = df.values.tolist()
    return res


def get_cosine_value(number):
    # returning the value of cosine of pi / 6
    print("The value of cosine of number is : ", end="")
    return math.cos(number)


def date_add(start_date):
    date_1 = datetime.datetime.strptime(start_date, "%m/%d/%y")
    print(date_1)
    added_date = date_1 + datetime.timedelta(days=10)
    return added_date



