from pybaseball import statcast
from datetime import datetime, timedelta

def fetch_statcast_data():

    start_date = "2025-04-01" 
    end_date = "2025-04-01"

    df = statcast(start_dt = start_date, end_dt = end_date)
    
    return df