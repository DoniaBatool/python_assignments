DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def Second_year():
    print(f"There are {DAYS_PER_YEAR*HOURS_PER_DAY+MIN_PER_HOUR*SEC_PER_MIN} seconds in a year!")
Second_year()