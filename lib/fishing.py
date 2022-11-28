from random import randint, choice

price_bait = 5000

def buyBait(arg):
    ea = int(arg)
    return price_bait * ea

def bkFishing():
    normalList = ["전어","고등어","굴비","붕어","정어리","넙치","꽁치","우럭","숭어","갈치","오징어","문어"]
    normal = {
        "전어": [25000,'https://i.imgur.com/SXSf8wf.jpg'],
        "고등어": [13000,'https://i.imgur.com/TikM1a9.jpg'],
        "굴비": [20000,'https://i.imgur.com/DsEImBQ.jpg'],
        "붕어": [10000,'https://i.imgur.com/S7duJaE.jpg'],
        "정어리": [10000,'https://i.imgur.com/4veznVy.jpg'],
        "넙치": [35000,'https://i.imgur.com/xA5tDsA.jpg'],
        "꽁치": [30000,'https://i.imgur.com/hpaSePl.jpg'], 
        "우럭": [55000,'https://i.imgur.com/jKZJGfV.jpg'],
        "숭어": [37000,'https://i.imgur.com/B3zg3qq.jpg'],
        "갈치": [20000,'https://i.imgur.com/5elN7D7.jpg'],
        "오징어": [7000,'https://i.imgur.com/wV3NmAE.jpg'],
        "문어": [33000,'https://i.imgur.com/Dnl7TYm.jpg']
}

    rareList = ["킹크랩","광어","복어","볼락","참돔","재방어","붉바리","다금바리","낙지","미끼","가오리"]
    rare = {
        "가오리": [250000,'https://i.imgur.com/LP3yIeQ.jpg'],
        "킹크랩": [110000,'https://i.imgur.com/rFYtiUh.png'],
        "복어": [106000,'https://i.imgur.com/3yOyqmH.jpg'],
        "볼락": [120000,'https://i.imgur.com/6FUAtPN.png'],
        "참돔": [100000,'https://i.imgur.com/4GeH5VK.jpg'],
        "재방어":[80000,'https://i.imgur.com/qCeoTcZ.jpg'],
        "붉바리": [140000,'https://i.imgur.com/VMpRCVd.jpg'],
        "다금바리": [100900,'https://i.imgur.com/M4DXnfl.jpg'],
        "낙지": [80000,'https://i.imgur.com/FCOjIzK.png'],
        "미끼": [10,'https://i.imgur.com/P3vA4iV.jpg']
    }

    uniqList = ["상어","파랑비늘돔","돗돔","참치","줄가자미","악어"]
    uniq = {
        "줄가자미": [290000,'https://i.imgur.com/H92UUtd.jpg'],
        "상어": [800000,'https://i.imgur.com/A4EQaYd.jpg'],
        "파랑비늘돔": [600000,'https://i.imgur.com/SSUjkhO.jpg'],
        "돗돔": [400000,'https://i.imgur.com/hlmX4aW.jpg'],
        "참치": [500000,'https://i.imgur.com/970HOkV.jpg'],
        "악어": [350000,'https://i.imgur.com/v7XGgg2.jpg']
    }

    legendaryList = ["리조두스 힙버티","엔코두스 아미크로두스","히네리아","에우스테노렙론"]
    legendary = {
        "리조두스 힙버티": [1000000,'https://i.imgur.com/LFnQcXF.jpg'],
        "엔코두스 아미크로두스": [2500000,'https://i.imgur.com/tI3izI8.jpg'],
        "히네리아": [5000000,'https://i.imgur.com/Q7Cuj23.jpg'],
        "에우스테노렙론": [8000000,'https://i.imgur.com/FhtukM9.jpg'],
    }

    ancientList = ["하이코우이크티스","실러캔스","착취의 손아귀","피라루크", "고승환의 커터칼"]
    ancient = {
        "하이코우이크티스": [50000000,'https://i.imgur.com/3iaJwT2.jpg'],
        "실러캔스": [37000000,'https://i.imgur.com/P8EyrL3.jpg'],
        "피라루크": [20000000,'https://i.imgur.com/Afsxae1.jpg'],
        "착취의 손아귀": [1,'https://i.imgur.com/cFFk2oA.jpg'],
        "고승환의 커터칼": [3, 'https://i.imgur.com/UBSG3DT.jpg']
    }

    n = randint(1,110)

    if n == 0:
        fish = "fail"
        result = "fail"
        color = 0xff0000
        deg = "fail"
        url = 'https://i.imgur.com/q5ddg5Z.jpg'
    elif 0 < n < 50:
        fish = choice(normalList)
        result = normal[fish][0]
        color = 0x0067A3
        deg = "노말"
        url = normal[fish][1]
    elif 49 < n < 80:
        fish = choice(rareList)
        result = rare[fish][0]
        color = 0x81C147
        deg = "레어"
        if fish == "미끼":
            color = 0xFFC0CB
        url = rare[fish][1]
    elif 79 < n < 95:
        fish = choice(uniqList)
        result = uniq[fish][0]
        color = 0x8B00FF
        deg = "유니크"
        url = uniq[fish][1]
    elif 94 < n < 107:
        fish = choice(legendaryList)
        result = legendary[fish][0]
        color = 0xC27C0E
        deg = "레전더리"
        url = legendary[fish][1]
    else:
        fish = choice(ancientList)
        result = ancient[fish][0]
        color = 0x7F8C8D
        deg = "에인션트"
        if fish == "착취의 손아귀":
            color = 0x023020
        if fish == "고승환의 커터칼":
            color = 0xff0000
        url = ancient[fish][1]
    return fish, result, color, deg, url


def enhancedFishing():
    normalList = ["전어","고등어","굴비","붕어","정어리","넙치","꽁치","우럭","숭어","홍어","부서진CD","갈치","오징어","문어"]
    normal = {
        "부서진CD": [-1000,'https://i.imgur.com/S5HraGt.png'],
        "전어": [25000,'https://i.imgur.com/SXSf8wf.jpg'],
        "고등어": [13000,'https://i.imgur.com/TikM1a9.jpg'],
        "굴비": [20000,'https://i.imgur.com/DsEImBQ.jpg'],
        "붕어": [10000,'https://i.imgur.com/S7duJaE.jpg'],
        "정어리": [10000,'https://i.imgur.com/4veznVy.jpg'],
        "넙치": [35000,'https://i.imgur.com/xA5tDsA.jpg'],
        "꽁치": [30000,'https://i.imgur.com/hpaSePl.jpg'], 
        "우럭": [55000,'https://i.imgur.com/jKZJGfV.jpg'],
        "숭어": [37000,'https://i.imgur.com/B3zg3qq.jpg'],
        "홍어": [-31000,'https://i.imgur.com/ILojN2x.jpg'],
        "갈치": [20000,'https://i.imgur.com/5elN7D7.jpg'],
        "오징어": [7000,'https://i.imgur.com/wV3NmAE.jpg'],
        "문어": [33000,'https://i.imgur.com/Dnl7TYm.jpg']
}

    rareList = ["킹크랩","광어","복어","볼락","참돔","재방어","붉바리","다금바리","낙지","술병","미끼","가오리"]
    rare = {
        "가오리": [250000,'https://i.imgur.com/LP3yIeQ.jpg'],
        "킹크랩": [110000,'https://i.imgur.com/rFYtiUh.png'],
        "복어": [106000,'https://i.imgur.com/3yOyqmH.jpg'],
        "볼락": [120000,'https://i.imgur.com/6FUAtPN.png'],
        "참돔": [100000,'https://i.imgur.com/4GeH5VK.jpg'],
        "재방어":[80000,'https://i.imgur.com/qCeoTcZ.jpg'],
        "붉바리": [140000,'https://i.imgur.com/VMpRCVd.jpg'],
        "다금바리": [100900,'https://i.imgur.com/M4DXnfl.jpg'],
        "낙지": [80000,'https://i.imgur.com/FCOjIzK.png'],
        "술병": [-25000,'https://i.imgur.com/TkW4eB1.jpg'],
        "미끼": [10,'https://i.imgur.com/P3vA4iV.jpg']
    }

    uniqList = ["상어","파랑비늘돔","돗돔","참치","줄가자미","악어", "피라냐"]
    uniq = {
        "피라냐": [-900000,'https://i.imgur.com/8F5eOzW.png'],
        "줄가자미": [290000,'https://i.imgur.com/H92UUtd.jpg'],
        "상어": [800000,'https://i.imgur.com/A4EQaYd.jpg'],
        "파랑비늘돔": [600000,'https://i.imgur.com/SSUjkhO.jpg'],
        "돗돔": [400000,'https://i.imgur.com/hlmX4aW.jpg'],
        "참치": [500000,'https://i.imgur.com/970HOkV.jpg'],
        "악어": [350000,'https://i.imgur.com/v7XGgg2.jpg']
    }

    legendaryList = ["수리남 홍어","리조두스 힙버티","엔코두스 아미크로두스","히네리아","에우스테노렙론","훼이크다 이 병신들아"]
    legendary = {
        "수리남 홍어": [-3100000,'https://i.imgur.com/Lbg46Ti.png'],
        "리조두스 힙버티": [1000000,'https://i.imgur.com/LFnQcXF.jpg'],
        "엔코두스 아미크로두스": [2500000,'https://i.imgur.com/tI3izI8.jpg'],
        "히네리아": [5000000,'https://i.imgur.com/Q7Cuj23.jpg'],
        "에우스테노렙론": [8000000,'https://i.imgur.com/FhtukM9.jpg'],
        "훼이크다 이 병신들아": [0,'https://i.imgur.com/wocEm6q.jpg']
    }

    ancientList = ["하이코우이크티스","실러캔스","착취의 손아귀","피라루크", "고승환의 커터칼"]
    ancient = {
        "하이코우이크티스": [50000000,'https://i.imgur.com/3iaJwT2.jpg'],
        "실러캔스": [37000000,'https://i.imgur.com/P8EyrL3.jpg'],
        "피라루크": [20000000,'https://i.imgur.com/Afsxae1.jpg'],
        "착취의 손아귀": [1,'https://i.imgur.com/cFFk2oA.jpg'],
        "고승환의 커터칼": [3, 'https://i.imgur.com/UBSG3DT.jpg']
    }

    n = randint(1,110)

    if n <= 5:
        fish = "fail"
        result = "fail"
        color = 0xff0000
        deg = "fail"
        url = 'https://i.imgur.com/q5ddg5Z.jpg'
    elif 5 < n < 50:
        fish = choice(normalList)
        result = normal[fish][0]
        color = 0x0067A3
        deg = "노말"
        url = normal[fish][1]
    elif 49 < n < 80:
        fish = choice(rareList)
        result = rare[fish][0]
        color = 0x81C147
        deg = "레어"
        if fish == "미끼":
            color = 0xFFC0CB
        url = rare[fish][1]
    elif 79 < n < 95:
        fish = choice(uniqList)
        result = uniq[fish][0]
        color = 0x8B00FF
        deg = "유니크"
        url = uniq[fish][1]
    elif 94 < n < 107:
        fish = choice(legendaryList)
        result = legendary[fish][0]
        color = 0xC27C0E
        deg = "레전더리"
        url = legendary[fish][1]
    else:
        fish = choice(ancientList)
        result = ancient[fish][0]
        color = 0x7F8C8D
        deg = "에인션트"
        if fish == "착취의 손아귀":
            color = 0x023020
        if fish == "고승환의 커터칼":
            color = 0xff0000
        url = ancient[fish][1]
    return fish, result, color, deg, url

def fishing():
    normalList = ["전어","고등어","굴비","붕어","정어리","넙치","꽁치","우럭","숭어","홍어","부서진CD","갈치","오징어","문어"]
    normal = {
        "부서진CD": [-1000,'https://i.imgur.com/S5HraGt.png'],
        "전어": [25000,'https://i.imgur.com/SXSf8wf.jpg'],
        "고등어": [13000,'https://i.imgur.com/TikM1a9.jpg'],
        "굴비": [20000,'https://i.imgur.com/DsEImBQ.jpg'],
        "붕어": [10000,'https://i.imgur.com/S7duJaE.jpg'],
        "정어리": [10000,'https://i.imgur.com/4veznVy.jpg'],
        "넙치": [35000,'https://i.imgur.com/xA5tDsA.jpg'],
        "꽁치": [30000,'https://i.imgur.com/hpaSePl.jpg'], 
        "우럭": [55000,'https://i.imgur.com/jKZJGfV.jpg'],
        "숭어": [37000,'https://i.imgur.com/B3zg3qq.jpg'],
        "홍어": [-31000,'https://i.imgur.com/ILojN2x.jpg'],
        "갈치": [20000,'https://i.imgur.com/5elN7D7.jpg'],
        "오징어": [7000,'https://i.imgur.com/wV3NmAE.jpg'],
        "문어": [33000,'https://i.imgur.com/Dnl7TYm.jpg']
}

    rareList = ["킹크랩","광어","복어","볼락","참돔","재방어","붉바리","다금바리","낙지","술병","미끼","가오리"]
    rare = {
        "가오리": [250000,'https://i.imgur.com/LP3yIeQ.jpg'],
        "킹크랩": [110000,'https://i.imgur.com/rFYtiUh.png'],
        "복어": [106000,'https://i.imgur.com/3yOyqmH.jpg'],
        "볼락": [120000,'https://i.imgur.com/6FUAtPN.png'],
        "참돔": [100000,'https://i.imgur.com/4GeH5VK.jpg'],
        "재방어":[80000,'https://i.imgur.com/qCeoTcZ.jpg'],
        "붉바리": [140000,'https://i.imgur.com/VMpRCVd.jpg'],
        "다금바리": [100900,'https://i.imgur.com/M4DXnfl.jpg'],
        "낙지": [80000,'https://i.imgur.com/FCOjIzK.png'],
        "술병": [-25000,'https://i.imgur.com/TkW4eB1.jpg'],
        "미끼": [10,'https://i.imgur.com/P3vA4iV.jpg']
    }

    uniqList = ["상어","파랑비늘돔","돗돔","참치","줄가자미","악어", "피라냐"]
    uniq = {
        "피라냐": [-900000,'https://i.imgur.com/8F5eOzW.png'],
        "줄가자미": [290000,'https://i.imgur.com/H92UUtd.jpg'],
        "상어": [800000,'https://i.imgur.com/A4EQaYd.jpg'],
        "파랑비늘돔": [600000,'https://i.imgur.com/SSUjkhO.jpg'],
        "돗돔": [400000,'https://i.imgur.com/hlmX4aW.jpg'],
        "참치": [500000,'https://i.imgur.com/970HOkV.jpg'],
        "악어": [350000,'https://i.imgur.com/v7XGgg2.jpg']
    }

    legendaryList = ["수리남 홍어","리조두스 힙버티","엔코두스 아미크로두스","히네리아","에우스테노렙론","훼이크다 이 병신들아"]
    legendary = {
        "수리남 홍어": [-3100000,'https://i.imgur.com/Lbg46Ti.png'],
        "리조두스 힙버티": [1000000,'https://i.imgur.com/LFnQcXF.jpg'],
        "엔코두스 아미크로두스": [2500000,'https://i.imgur.com/tI3izI8.jpg'],
        "히네리아": [5000000,'https://i.imgur.com/Q7Cuj23.jpg'],
        "에우스테노렙론": [8000000,'https://i.imgur.com/FhtukM9.jpg'],
        "훼이크다 이 병신들아": [0,'https://i.imgur.com/wocEm6q.jpg']
    }

    ancientList = ["하이코우이크티스","실러캔스","착취의 손아귀","피라루크", "고승환의 커터칼"]
    ancient = {
        "하이코우이크티스": [50000000,'https://i.imgur.com/3iaJwT2.jpg'],
        "실러캔스": [37000000,'https://i.imgur.com/P8EyrL3.jpg'],
        "피라루크": [20000000,'https://i.imgur.com/Afsxae1.jpg'],
        "착취의 손아귀": [1,'https://i.imgur.com/cFFk2oA.jpg'],
        "고승환의 커터칼": [3, 'https://i.imgur.com/UBSG3DT.jpg']
    }

    n = randint(1,110)

    if n <= 10:
        fish = "fail"
        result = "fail"
        color = 0xff0000
        deg = "fail"
        url = 'https://i.imgur.com/q5ddg5Z.jpg'
    elif 10 < n < 56:
        fish = choice(normalList)
        result = normal[fish][0]
        color = 0x0067A3
        deg = "노말"
        url = normal[fish][1]
    elif 55 < n < 87:
        fish = choice(rareList)
        result = rare[fish][0]
        color = 0x81C147
        deg = "레어"
        if fish == "미끼":
            color = 0xFFC0CB
        url = rare[fish][1]
    elif 86 < n < 99:
        fish = choice(uniqList)
        result = uniq[fish][0]
        color = 0x8B00FF
        deg = "유니크"
        url = uniq[fish][1]
    elif 98 < n < 108:
        fish = choice(legendaryList)
        result = legendary[fish][0]
        color = 0xC27C0E
        deg = "레전더리"
        url = legendary[fish][1]
    else:
        fish = choice(ancientList)
        result = ancient[fish][0]
        color = 0x7F8C8D
        deg = "에인션트"
        if fish == "착취의 손아귀":
            color = 0x023020
        if fish == "고승환의 커터칼":
            color = 0xff0000
        url = ancient[fish][1]
    return fish, result, color, deg, url