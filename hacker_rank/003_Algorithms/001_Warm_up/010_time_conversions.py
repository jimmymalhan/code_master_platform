# Given a time 12- hour AM/PM format, convert it to military
# (24hour) time

from time import strptime, strftime
def timeConversion(s):
    print(strftime("%H:%M:%S", strptime(s, "%I:%M:%S%p")))
if __name__ == '__main__':
    s = input()
    timeConversion(s)