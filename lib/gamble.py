import random

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
        # 조합까지 맞췄을 때
        if bot1 == user2:
            return "승리", 0xFAFA00, str(bot1), str(bot2), str(user1), str(user2), 5000000
        # 순서까지 맞췄을 때
        if bot1 == user1:
            return "승리", 0xFAFA00, str(bot1), str(bot2), str(user1), str(user2), 25000000
        return "승리", 0xFAFA00, str(bot1), str(bot2), str(user1), str(user2), 1000000
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