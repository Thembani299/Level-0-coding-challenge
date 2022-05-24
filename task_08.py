def number_to_time(number):
    number_of_hours=number//60
    number_of_minutes=number%60
    if number_of_hours ==1:
        hours="hour"
    else:
        hours="hours"
    if number_of_minutes ==1:
        minutes="minute"
    else:
        minutes="minutes"
    print(str(number_of_hours)+" "+hours+", "+str(number_of_minutes)+" "+minutes)
number_to_time(71)
number_to_time(133)
