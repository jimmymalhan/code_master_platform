from time import strptime, strftime

def timeConversion(s):
    print(strftime("%H:%M:%S", strptime(s, "%I:%M:%S%p")))
if __name__ == '__main__':
    s = input()
    timeConversion(s)
