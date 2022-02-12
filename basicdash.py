#import color for terminal display
from termcolor import colored
#import calendar, time and datetime function
import calendar
import datetime
import time
#import regular expressions
import re

def showcal():
    #get current month and year from host
    today = datetime.date.today()
    year = today.year
    month = today.month
    currentmonth = calendar.month(year,month)
    date = today.day.__str__().rjust(2)
    rday  = ('\\b' + date + '\\b').replace('\\b ', '\\s')
    #7 Swaps foreground and background colors and print the current date
    rdayc = "\033[7m" + date + "\033[0m"
    print(colored(re.sub(rday,rdayc,currentmonth),"yellow"))

#define the clock function
def clock():
    while True:
        #show the time
        print(colored(datetime.datetime.now().strftime("The time is: " + "%H:%M:%S"),"blue"),end="\r")
        #the program waits for 1 second before printing the latest time 
        time.sleep(1)

#run the functions
showcal()
clock()

#the calendar highlight stuff was borrowed from shorturl.at/clzO9
