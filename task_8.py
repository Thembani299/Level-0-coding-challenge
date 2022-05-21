def number_to_time(number):
    hours=number//60
    minutes=number%60
    if hours ==1:
        x="hour"
    else:
        x="hours"
    if minutes ==1:
        y="minute"
    else:
        y="minutes"
    print(str(hours)+" "+x+", "+str(minutes)+" "+y)