import datetime

date = datetime.date(2026, 1, 1) #Initialize a date object with the year 2026, month 1 (January), and day 1
today = datetime.date.today()    #Get the current date

time = datetime.time(12, 30, 0) #Initialize a time object with hour 12, minute 30, and second 0
now = datetime.datetime.now()   #Get the current date and time

now = now.strftime("%Y-%m-%d %H:%M:%S") #Format the current date and time as a string in the format "YYYY-MM-DD HH:MM:SS"

target_datetime = datetime.datetime(2030, 1, 1, 12, 30, 0) #Initialize a target datetime object with the year 2030, month 1 (January), day 1, hour 12, minute 30, and second 0
current_datetime = datetime.datetime.now() #Get the current date and time
time_difference = target_datetime - current_datetime #Calculate the time difference between the target datetime and the current datetime
days_remaining = time_difference.days #Get the number of days remaining until the target datetime



print("Date:", date) #Print the initialized date object
print("Today:", today) #Print the current date
print("Time:", time) #Print the initialized time object
print("Now:", now) #Print the formatted current date and time
print("Target DateTime:", target_datetime) #Print the target datetime object
print("Time Difference:", time_difference) #Print the time difference between the target datetime and the current datetime
print("Days Remaining:", days_remaining) #Print the number of days remaining until the target datetime
