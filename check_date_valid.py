from datetime import datetime as dt
def is_date_valid(val): return dt.strptime(val, "%B %d, %Y %H:%M:%S") if val else False
print(is_date_valid("December 17, 1995 03:24:00"))
#dt.strftime("%B %d, %Y") → December 17, 1995
#dt.strftime("%d %B %Y") → 17 December 1995
#dt.strftime("%m/%d/%Y") → 12/17/1995
#dt.strftime("%A, %B %d, %Y") → Sunday, December 17, 1995