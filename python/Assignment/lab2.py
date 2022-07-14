hour = int(input("starting time (hours): "))
mins = int(input("starting time (minutes): "))
dura = int(input("starting time (minutes): "))
#if an event start at 12:17 and last for 59 minutes, it will ed at 13:16
#sample data: 12,17,59
#expected output:13:16
#sample data: 23,58,642
#expected output:10:40
#sample data: 0,1,2939
#expected output:1:0
total_time = hour*60
total_time = total_time + mins + dura
print((total_time/60)%24, end=":")
print(total_time%60)

