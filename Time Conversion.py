import math
import os
import random
import re
import sys
from datetime import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    dt = datetime.strptime(s, "%I:%M:%S%p")
    
    time_24_hours = dt.strftime("%H:%M:%S")
    
    return time_24_hours
    
if __name__ == '__main__':
    
    s = "12:01:00AM"
 
    result = timeConversion(s)

    print(result)