from datetime import datetime as dt
import arrow

today = arrow.now().format('MM-DD-YYYY')
st = "6/1/2017"
end = today

# returns True if d1 is smaller than d2
def is_smaller(d1, d2):
  return dt.strptime(d1, "%m/%d/%Y") < dt.strptime(d2, "%m/%d/%Y")

# returns True if date is in between st and end
def filter_func(date):
  return is_smaller(st, date)

dates=['04/6/2016', '05/4/2016', '06/26/2016', '07/26/2017', '09/5/2017', '10/7/2017', '10/12/2017', '04/12/2017', '05/10/2017', '06/12/2018', '07/19/2018', '08/15/2018', '09/17/2018', '04/21/2018', '05/28/2018', '07/26/2018']

print(list(filter(filter_func, dates)))