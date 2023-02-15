import random

def hairlossbeam(arg):
    n = random.randint(0,10)

    if n > 4:
        return f"유저 {arg}이 탈모빔을 회피하였다."
    elif 1 < n < 5:
        return f"유저 {arg}이 탈모빔에 맞았다. 탈모 가능성이 높아진다."
    else:
        return f"유저 {arg}이 탈모빔에 맞았다. \n 치명타가 터졌다. 유저 {arg}는 대머리가 되었다"