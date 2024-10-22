hours=int(input())
minutes=int(input())
time_format=str(input())

def time_string(hours, minutes, time_format):
    if time_format=="24":
        time=hours,":",minutes
    elif time_format=="12":
        if hours>12:
            a=hours-12
            time=a,":",minutes, 'am'
        else:
            a=hours
        time=a,':',minutes,"pm"
    return time


t=time_string(hours, minutes, time_format)
print(t)

