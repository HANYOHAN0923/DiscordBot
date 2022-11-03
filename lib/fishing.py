from random import randint, choice

price_bait = 5000

def buyBait(arg):
    ea = int(arg)
    return price_bait * ea

def fishing():
    normalList = ["전어","고등어","굴비","붕어","정어리","넙치","꽁치","우럭","숭어","홍어","부서진CD","갈치","오징어","문어"]
    normal = {
        "부서진CD": -1000,
        "전어": 25000,
        "고등어": 13000,
        "굴비": 20000,
        "붕어": 10000,
        "정어리": 10000,
        "넙치": 35000,
        "꽁치": 30000, 
        "우럭": 55000,
        "숭어": 37000,
        "홍어": -31000,
        "갈치": 20000,
        "오징어": 7000,
        "문어": 33000
}

    rareList = ["킹크랩","광어","복어","볼락","참돔","재방어","붉바리","다금바리","낙지","술병","미끼"]
    rare = {
        "킹크랩": 110000,
        "광어": 98000,
        "복어": 106000,
        "볼락": 120000,
        "참돔": 100000,
        "재방어":80000,
        "붉바리": 140000,
        "다금바리": 100900,
        "낙지": 80000,
        "술병": -25000,
        "미끼": 10
    }

    uniqList = ["상어","파랑비늘돔","돗돔","참치","줄가자미","악어", "피라냐"]
    uniq = {
        "피라냐": -900000,
        "줄가자미": 130000,
        "상어": 800000,
        "파랑비늘돔": 600000,
        "돗돔": 400000,
        "참치": 500000,
        "악어": 300000
    }

    legendaryList = ["수리남 홍어","리조두스 힙버티","엔코두스 아미크로두스","히네리아","에우스테노렙론","훼이크다 이 병신들아"]
    legendary = {
        "수리남 홍어": -3100000,
        "리조두스 힙버티": 1000000,
        "엔코두스 아미크로두스": 2500000,
        "히네리아": 5000000,
        "에우스테노렙론": 8000000,
        "훼이크다 이 병신들아": 0
    }

    ancientList = ["하이쿠이크티스","실러캔스","착취"]
    ancient = {
        "하이쿠이크티스": 50000000,
        "실러캔스": 37000000,
        "착취": 1,
    }

    n = randint(1,110)

    if n <= 10:
        fish = "fail"
        result = "fail"
        color = 0xff0000
        deg = "fail"
    elif 10 < n < 56:
        fish = choice(normalList)
        result = normal[fish]
        color = 0x0067A3
        deg = "노말"
    elif 55 < n < 87:
        fish = choice(rareList)
        if fish == "미끼":
            color = 0xFFC0CB
        result = rare[fish]
        color = 0x81C147
        deg = "레어"
    elif 86 < n < 97:
        fish = choice(uniqList)
        result = uniq[fish]
        color = 0x8B00FF
        deg = "유니크"
    elif 96 < n < 106:
        fish = choice(legendaryList)
        result = legendary[fish]
        color = 0xC27C0E
        deg = "레전더리"
    else:
        fish = choice(ancientList)
        if fish == "착취":
            color = 0x023020
        result = ancient[fish]
        color = 0x7F8C8D
        deg = "에인션트"
    return fish, result, color, deg