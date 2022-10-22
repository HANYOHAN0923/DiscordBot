import random

def dice(user_input):
    print("game.py - dice")
    bot1 = random.randrange(1,7)
    bot2 = random.randrange(1,7)

    a = bot1 + bot2
    b = user_input

    if a == b:
        return "승리", 0xFAFA00, str(bot1), str(bot2), str(a), str(b)
    else:
        return "패배", 0x00ff56, str(bot1), str(bot2), str(a), str(b)

def gamble():
    print("game.py - coin")
    coin_face = random.randrange(0,5)
    
    if coin_face <= 1:
        print("성공")
        return True
    else:
        print("실패")
        return False