import calendar

from datetime import datetime
from decimal import Decimal

from django.utils.datastructures import SortedDict


def _create_datetime_object(year, month):
    # year, month, day, hour, minute, second
    return datetime(year, month, 1, 0, 0, 0)


def _get_months_days(year):
    """ Returns a list of the number of days for each month of the
        given year. It takes into consideration leap years."""
    return [0] + [calendar.monthrange(y, m)[1] \
                                for y in [year] \
                                    for m in range(1, 13)]


def _handle_one_month(from_day, until_day, month, year):
    """ Return the days in the range (from_day, until_day) for the given
        month of the given year. """
    months_days = _get_months_days(year)

    if until_day == -1:  # trick to ask for the days until the
                         # end of the month
        until_day = months_days[month]

    return range(1, until_day + 1)


def _handle_one_year(from_month, until_month):
    """ Return a list of the months between from_month and until_month"""
    return [month for month in range(from_month, until_month + 1)]


def _get_filter_dates(from_year, until_year, from_month, until_month):
    """ Get a SortedDict of the shape {<year>: <list of months>} to
        filter orders with. """
    filter_dates = SortedDict()

    if from_year == until_year:  # We are handling months of a single year:
        year = from_year
        filter_dates[year] = _handle_one_year(from_month, until_month)

    else:  # We are handling months from more than one year.

        # The months for the initial year
        filter_dates[from_year] = _handle_one_year(from_month, 12)

        if until_year - from_year > 1:
            # there are years between from_year and until_year
            for year in range(from_year + 1, until_year):
                filter_dates[year] = _handle_one_year(1, 12)

        # The months for the last year
        filter_dates[until_year] = _handle_one_year(1, until_month)

    return filter_dates


def _safe_get_sum(values_sum):
    """ This little function handles safely the mixed addition of integers and
        decimals, and returns their integer representation. """
    if isinstance(values_sum, int):
        return values_sum
    elif isinstance(values_sum, Decimal):
        return int(values_sum.to_integral_exact().to_eng_string())
    else:
        return '0'


def _get_weekday(year, month, day):
    """ Return the string name of the weekday the given day is. """
    cal = calendar.Calendar()
    aux = cal.monthdays2calendar(year, month)

    # un-nest the tuple list:
    aux = [item for sublist in aux for item in sublist]
    day_number = [t[1] for t in aux if t[0] == day][0]
    day_name = calendar.day_name[day_number]

    return day_name
