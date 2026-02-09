# it is used to work with time 
# there are two modules in python time and datetime

# time-->
# time()-returns time in seconds
# ctime()--Thu Oct 27 07:32:07 2022
#  sleep()--
# localtime()--tm_year=2022, tm_mon=10, tm_mday=27,
#              tm_hour=7, tm_min=35, tm_sec=8, 
#              tm_wday=3, tm_yday=300, tm_isdst=0)

import time
print(time.time())

print(time.ctime())

print(time.sleep(2))
print('after 2 seconds')

print(time.localtime())