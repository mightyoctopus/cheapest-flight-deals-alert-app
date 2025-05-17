from datetime import datetime, timedelta
from time import strftime

def check_the_date_after_tmr() -> str:
    now = datetime.now()
    tmr = now + timedelta(days=2)
    return tmr.strftime("%Y-%m-%d")

def get_date_6_months_later() -> str:
    now = datetime.now()
    six_months_later = now + timedelta(days=180)
    return six_months_later.strftime("%Y-%m-%d")

