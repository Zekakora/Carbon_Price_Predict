import numpy as np
import pandas as pd
from datetime import datetime

def time_convert(start, end):
    start = pd.Timestamp(start)
    end = pd.Timestamp(end)
    time = pd.date_range(start=start, end=end, freq='M')
    time = time.strftime('%Y%m')
    return time

time_setting = ('20231201', '20231231')
timerange = time_convert(time_setting[0], time_setting[1])
for time in timerange:
    time1 = datetime.strptime(time, '%Y%m')
    time1 =time1.to_period(freq='M')
    print(time1.days_in_months)
    print(type(time1))
    print(time1)

# month = pd.Timestamp('2022-01-01')
# print(month.days_in_month)