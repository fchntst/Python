# making a clock 
hours = int(input('give hours: '))
minutes = int(input('give minutes: '))
seconds = int(input('give seconds: '))

if 0 <= hours < 10:
    message1 = '0' + str(hours)
elif 10 <= hours <= 23:
    message1 = str(hours)
    
if 0 <= minutes <= 10:
    message2 = '0' + str(minutes)     
elif 10 <= minutes <= 60:
    message2 = str(minutes)

if 0 <= seconds <= 10:
    message3 = '0' + str(seconds)
elif 10 <= seconds <= 60:
    message3 = str(seconds)

message = message1+ ":" + message2 + ':' + message3 
print(message)