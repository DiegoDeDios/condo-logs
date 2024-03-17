import pytz
from datetime import datetime

def get_cst_time(ts):
    cst = pytz.timezone('America/Mexico_City') #Hora local Mexico
    local_date =  datetime.fromtimestamp(ts, tz=pytz.utc).astimezone(cst)
    return local_date.strftime("%y/%m/%d %H:%M:%S")

