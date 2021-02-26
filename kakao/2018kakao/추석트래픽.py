from datetime import datetime, timedelta
def solution(lines):
    start_time = []
    end_time = []
    time_info = dict()
    check = [0]*len(lines)
    for i in range(len(lines)):
        dates, times, info = lines[i].split()
        hour, minute, seconds = times.split(':')
        end = int(hour)*60*60 + int(minute)*60 + float(seconds)
        start = end - float(info[:-1]) + 0.001
        if start not in time_info.keys():
            time_info[start] = end
            
        start_time.append(start)
        end_time.append(end)
    
    print(start_time)
    print(end_time)
    print(now_start_time)
    for i in range(len(lines)):
        for j in range(len(lines)):
            if  start_time[i] <= now_start_time[j] and now_start_time[j] <= end_time[i]:
                check[i] += 1
    print(check)

    return 

# lines =  ["2016-09-15 20:59:57.421 0.351s",
# "2016-09-15 20:59:58.233 1.181s",
# "2016-09-15 20:59:58.299 0.8s",
# '2016-09-15 20:59:58.688 1.041s',
# '2016-09-15 20:59:59.591 1.412s',
# '2016-09-15 21:00:00.464 1.466s',
# '2016-09-15 21:00:00.741 1.581s',
# '2016-09-15 21:00:00.748 2.31s',
# '2016-09-15 21:00:00.966 0.381s',
# '2016-09-15 21:00:02.066 2.62s'
# ]
lines = [
'2016-09-15 01:00:04.002 2.0s',
'2016-09-15 01:00:07.000 2s'
]
print(solution(lines))
