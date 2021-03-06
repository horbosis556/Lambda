from datetime import datetime

#Initialization of current date.
initialize = datetime.datetime.now()

#Assign each attribute into separate lambdas.
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
local_time = lambda x: x.time()

#Call each lambda to print year, month, day, local_time, UTC_offset and timezone.
print(year(initialize),month(initialize),day(initialize),local_time(initialize),initialize.strftime(%z),initialize.strftime(%Z))







