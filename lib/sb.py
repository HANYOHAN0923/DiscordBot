import random

def sb(arg):
    n = random.randint(0,10)
    if n > 3:
        return f"{arg}는 정상인입니다"
    elif 0 < n < 4:
        return f"{arg}는 병신입니다"
    else:
        return f"{arg}는 세계 최고 병신입니다"