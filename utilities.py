from datetime import datetime, timedelta
from time import strftime

def check_the_date_after_tmr() -> str:
    """
    Return the date of 2 days from now(today) for setting as the start date for flight search
    :return: A string representing the date two days from now, formatted as YYYY-MM-DD
    """
    now = datetime.now()
    tmr = now + timedelta(days=2)
    return tmr.strftime("%Y-%m-%d")

def get_date_6_months_later() -> str:
    """
    Return the date of 2 days from now(today) for as the end date for flight search
    :return: A string representing the date 6 months from now, formatted as YYYY-MM-DD
    """
    now = datetime.now()
    six_months_later = now + timedelta(days=180)
    return six_months_later.strftime("%Y-%m-%d")

