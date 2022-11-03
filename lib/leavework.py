# time difference + 09:00:00
from datetime import datetime
import math

def countTime():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_time_split = current_time.split(":")
    ct_h = current_time_split[0]
    ct_m = current_time_split[1]
    ct_s = current_time_split[2]

    if not datetime.today().weekday() < 5:
        return "휴일이다 병신아"

    if int(ct_h)+9 > 17:
        return "이징 씨아반"

    if  int(ct_h)+9  < 9:
        return "출근 전이다 씹련아"

    total_left_seconds = 17*3600 - ((int(ct_h)+9)*3600 + int(ct_m)*60 + int(ct_s))

    left_hours = math.floor(total_left_seconds/ (60 * 60))
    total_left_seconds -= left_hours * 60 * 60
    left_mins = math.floor(total_left_seconds / 60)
    total_left_seconds -= left_mins * 60
    left_secs =  total_left_seconds
    
    return f"퇴근까지 {left_hours}시간 {left_mins}분 {left_secs}초 남았습니다"
