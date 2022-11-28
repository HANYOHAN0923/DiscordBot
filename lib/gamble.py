import random

def enhancedDice(x,y):
    print("game.py - enhancedDice")
    bot1 = random.randint(1,4)
    bot2 = random.randint(1,4)
    bot_total = bot1 + bot2
    print(f"봇의 숫자 {bot1}, {bot2}")
    
    user1, user2 = int(x), int(y)
    user_total = user1 + user2
    print(f"유저 숫자 {user1}, {user2}")

    # 숫자 합만 맞췄을 때
    if bot_total == user_total:
        n = random.randint(1,25)
        if n == 25:
            return "아이템 획득", 0x023020, 0, 0, 0, 0, 1
        # 조합까지 맞췄을 때
        if bot1 == user2:
            n = random.randint(1,5)
            if n == 5:
                return "아이템 획득", 0x023020, 0, 0, 0, 0, 1
            return "승리", 0xFAFA00, str(bot1), str(bot2), str(user1), str(user2), 10000000
        # 순서까지 맞췄을 때
        if bot1 == user1:
            n = random.randint(0,1)
            if n == 1:
                return "아이템 획득", 0x023020, 0, 0, 0, 0, 1
            return "승리", 0xFAFA00, str(bot1), str(bot2), str(user1), str(user2), 30000000
        return "승리", 0xFAFA00, str(bot1), str(bot2), str(user1), str(user2), 2500000
    # 꽝
    else:
        return "패배", 0xFF0000, str(bot1), str(bot2), str(user1), str(user2), 0

def dice(x, y):
    print("game.py - dice")
    bot1 = random.randint(1,6)
    bot2 = random.randint(1,6)
    bot_total = bot1 + bot2
    print(f"봇의 숫자 {bot1}, {bot2}")
    
    user1, user2 = int(x), int(y)
    user_total = user1 + user2
    print(f"유저 숫자 {user1}, {user2}")

    # 숫자 합만 맞췄을 때
    if bot_total == user_total:
        n = random.randint(1,50)
        if n == 50:
            return "아이템 획득", 0x023020, 0, 0, 0, 0, 1
        # 조합까지 맞췄을 때
        if bot1 == user2:
            n = random.randint(1,10)
            if n == 10:
                return "아이템 획득", 0x023020, 0, 0, 0, 0, 1
            return "승리", 0xFAFA00, str(bot1), str(bot2), str(user1), str(user2), 10000000
        # 순서까지 맞췄을 때
        if bot1 == user1:
            n = random.randint(0,1)
            if n == 1:
                return "아이템 획득", 0x023020, 0, 0, 0, 0, 1
            return "승리", 0xFAFA00, str(bot1), str(bot2), str(user1), str(user2), 30000000
        return "승리", 0xFAFA00, str(bot1), str(bot2), str(user1), str(user2), 2500000
    # 꽝
    else:
        return "패배", 0xFF0000, str(bot1), str(bot2), str(user1), str(user2), 0

def gamble():
    print("game.py - coin")
    coin_face = random.randint(0,4)
    
    if coin_face <= 1:
        print("성공")
        return True
    else:
        print("실패")
        return False