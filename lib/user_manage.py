# https://firebase.google.com/docs/firestore/quickstart
# https://firebase.google.com/docs/firestore/query-data/get-data
# https://cloud.google.com/firestore/docs/samples/firestore-data-set-field#firestore_data_set_field-python

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from random import randint

cred = credentials.Certificate("./json/obungadiscordbot-firebase-adminsdk-mn0p0-3c97204428.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#=========================Account==================================
def checkUser(_name, _id):
    print("user.py - checkUser()")
    # DB에 없는 유저는 NameError가 발생합니다
    try:
        find_user = db.collection(u'users').document(_name)
        if _id == find_user.get().to_dict()['id']:
            return True
        else:
            return False
    except:
        return False

def checkUserNum():
    print("user.py - checkUserNum()")
    users_ref = db.collection(u'users')
    docs = users_ref.stream()
    count = 0
    print("유저 수 집계를 시작합니다")
    for i in docs: count += 1
    print(f"집계 완료 (총 {count}명입니다) ")
    return count

def signUp(_name, _id):
    print("user.py - signUp()")
    if checkUser(_name,_id):
        print("등록된 유저")
        return "이미 가입된 유저입니다"
    else: 
        print("미등록 유저 - 회원가입을 진행합니다")
        doc_ref = db.collection(u'users').document(_name)
        doc_ref.set({
            u'id' : _id,
            u'money' : 30000000,
            u'loss' : 0,
            u'level' : 0,
            u'exp' : 0,
            # foreignCurrency
            u'dollar' : 0,
            u'yen' : 0,
            u'yuan' : 0,
            u'euro' : 0,
            u'pound' : 0,
            u'real' : 0,
            u'ruble' : 0,
            u'rupee' : 0,
            # coin
            u'waves' : 0,
            u'btc' : 0,
            u'eth' : 0,
            u'doge' : 0,
            u'ltc' : 0,
            u'etc' : 0,
            u'lunc' : 0,
            u'sand' : 0,
            u'bnb' : 0,
            u'xrp' : 0,
            # item
            u'bait' : 0,
            u'graps' : 0,
            u'wisky' : 0,
            u'vitamin' : 0,
            u'bk' : 0,
            u'kc' : 0,
            u'rkc' : 0,
            u'ostrich' : 0
            })
        return "회원가입 성공, 등록해주셔서 감사합니다."

def userInfo(_name):
    print("user.py - checkUser()")
    user_info = db.collection(u'users').document(_name).get().to_dict()

    _lvl = user_info["level"]
    _exp = user_info["exp"]
    _money = user_info["money"]
    _loss = user_info["loss"]
    _dollar = user_info["dollar"]
    _yen = user_info["yen"]
    _yuan = user_info["yuan"]
    _euro = user_info["euro"]
    _pound = user_info["pound"]
    _real =user_info["real"]
    _ruble = user_info["ruble"]
    _rupee = user_info["rupee"]
    _waves = user_info["waves"]
    _btc = user_info["btc"]
    _eth = user_info["eth"]
    _doge =  user_info["doge"]
    _ltc = user_info["ltc"]
    _etc = user_info["etc"]
    _lunc =  user_info["lunc"]
    _sand =  user_info["sand"]
    _bnb = user_info["bnb"]
    _xrp = user_info["xrp"]

    print("조회 완료")
    return _lvl, _exp, _money, _loss, _dollar, _yen, _yuan, _euro, _pound, _real, _ruble, _rupee, _waves, _btc, _eth, _doge, _ltc, _etc, _lunc, _sand, _bnb, _xrp


#=========================Ranking==================================
def rankingLv():
    print("user.py - rankingLv()")

    userRanking = {}
    usersList = db.collection(u'users').stream()

    print("랭킹 집계 중...")
    for user in usersList:
        _name = user.id # collectionName
        _lvl = user.to_dict()['level']
        userRanking[_name] = _lvl
    print("랭킹 집계 완료")
    
    a = sorted(userRanking.items(), reverse=True, key=lambda item:item[1])
    result = []
    for items in a:
        result.append(items[0])
        result.append(items[1])
    print(result)
    print("")
    
    return result

def rankingMoney():
    print("user.py - rankingMoney()")

    userRanking = {}
    usersList = db.collection(u'users').stream()
    
    print("랭킹 집계 중...")
    for user in usersList:
        _name = user.id # collectionName
        _lvl = user.to_dict()['money']
        userRanking[_name] = _lvl
    print("랭킹 집계 완료")

    a = sorted(userRanking.items(), reverse=True, key=lambda item:item[1])
    result = []
    for items in a:
        result.append(items[0])
        result.append(items[1])
    print(result)
    print("")

    return result

def getLvRank(_name):
    print("user.py - getRank()")
    
    print(f'{_name}의 랭킹 조사')
    rank = rankingLv()
    result = int(rank.index(_name)/2)+1
    print("완료")

    return result

#=========================Level==================================
def levelUpCheck(_name):
    print("user.py - levelUpCheck()")

    name = _name
    exp = db.collection(u'users').document(_name).get().to_dict()["exp"]
    lvl = db.collection(u'users').document(_name).get().to_dict()["level"]
    print(f'{_name}의 현재 경험치 {exp}')
    print(f'{name}의 현재 레벨 {lvl}')

    amount_to_up = lvl^2 + lvl*6
    count = 0

    if exp >= amount_to_up:
        while(exp >= amount_to_up and exp >= 0):
            print("레벨업에 필요한 경험치 :", amount_to_up)
            print("현재 경험치: ", exp)

            print("충분한 경험치양을 확인")
            db.collection(u'users').document(_name).update({u'level': lvl + 1})
            count += 1
            print("레벨 데이터 수정")
            db.collection(u'users').document(_name).update({u'exp': exp - amount_to_up})
            print("경험치 초기화")

            exp = db.collection(u'users').document(_name).get().to_dict()["exp"]
            lvl = db.collection(u'users').document(_name).get().to_dict()["level"]
            amount_to_up = lvl*lvl + 6*lvl
        return True, lvl
    else:
        return False, lvl

def modifyExp(_name, _amount):
    print("user.py - modifyExp")

    name = _name
    exp = db.collection(u'users').document(_name).get().to_dict()["exp"]
    print(name, "의 경험치 획득량: ", _amount)

    db.collection(u'users').document(_name).update({u'exp': exp + _amount})
    print(name, "현재 경험치: ", db.collection(u'users').document(_name).get().to_dict()["exp"])

#=========================Money==================================
def getMoney(_name):
    print("user.py - getMoney()")

    print(_name, "의 돈을 탐색")

    result = db.collection(u'users').document(_name).get().to_dict()["money"]
    print(_name,"의 보유 자산: ", result)


    return result

def getForeignCurrency(_name, _target):
    print("user.py - geForeignCurrency()")

    print(_name, "의 외화를 탐색")
    result = db.collection(u'users').document(_name).get().to_dict()[_target]
    print(_target + " : " + str(result))


    return result

def modifyMoney(_target, _amount):
    print("user.py - modifyMoney()")

    print(_target, "의 자산데이터 수정")
    money = db.collection(u'users').document(_target).get().to_dict()["money"]
    print(_target, "의 자산: " + str(money))
    print("추가할 액수: ", _amount)
    db.collection(u'users').document(_target).update({u'money': money + _amount})

    print("자산데이터 수정 완료")
    print("수정된", _target, "의 자산: ", db.collection(u'users').document(_target).get().to_dict()["money"])

def remit(sender, receiver, _amount):
    print("user.py - remit()")
    
    print("보내는 사람: ", sender)
    print("받는 사람: ", receiver)
    print("보내는 돈: ", _amount)
    print("")

    modifyMoney(receiver,  int(_amount))
    modifyMoney(sender,  -int(_amount))
    print("수정 완료")
    print("")

def addLoss(_target, _amount):
    print("user.py - addLoss()")

    print(_target, "의 잃은 돈 추가")
    loss = db.collection(u'users').document(_target).get().to_dict()["loss"]
    print(_target, "의 잃은돈: " + str(loss))
    print("추가할 액수: ", _amount)
    db.collection(u'users').document(_target).update({u'loss': loss + _amount})

    print("잃은 돈 추가 완료")
    print(_target, "의 총 잃은 돈: ", db.collection(u'users').document(_target).get().to_dict()["loss"])

def tradeForeignCurrency(_target, _amount, _c):
    print("user.py - buyForeignCurrency()")

    print(_target, "의 외화 자산 데이터 수정")
    print("추가할 액수: ", _amount)
    current_money = db.collection(u'users').document(_target).get().to_dict()[_c]
    db.collection(u'users').document(_target).update({_c: current_money + _amount})

    print("자산데이터 수정 완료")
    
#=========================Coin==================================
def getDollar(_name):
    print("user.py - getDollar()")

    print(_name, "의 달러를 탐색")

    result = db.collection(u'users').document(_name).get().to_dict()['dollar']
    print(_name, "의 보유 달러: ", result)

    return result

def getCoin(_name, _coin):
    print("user.py - getCoin()")
    print(_name, "의 코인을 탐색")

    if _coin == "웨이브":
        result = db.collection(u'users').document(_name).get().to_dict()['waves']
        print(_name, "의 보유" + _coin + " : ", result)
    elif _coin == "비트코인":
        result = db.collection(u'users').document(_name).get().to_dict()['btc']
        print(_name, "의 보유" + _coin + " : ", result)
    elif _coin == "이더리움":
        result = db.collection(u'users').document(_name).get().to_dict()['eth']
        print(_name, "의 보유" + _coin + " : ", result)
    elif _coin == "도지":
        result = db.collection(u'users').document(_name).get().to_dict()['doge']
        print(_name, "의 보유" + _coin + " : ", result)
    elif _coin == "라이트":
        result = db.collection(u'users').document(_name).get().to_dict()['ltc']
        print(_name, "의 보유" + _coin + " : ", result)
    elif _coin == "이더리움클래식":
        result = db.collection(u'users').document(_name).get().to_dict()['etc']
        print(_name, "의 보유" + _coin + " : ", result)
    elif _coin == "루나클래식":
        result = db.collection(u'users').document(_name).get().to_dict()['lunc']
        print(_name, "의 보유" + _coin + " : ", result)
    elif _coin == "샌드박스":
        result = db.collection(u'users').document(_name).get().to_dict()['sand']
        print(_name, "의 보유" + _coin + " : ", result)
    elif _coin == "비엔비":
        result = db.collection(u'users').document(_name).get().to_dict()['bnb']
        print(_name, "의 보유" + _coin + " : ", result)
    elif _coin == "리플":
        result = db.collection(u'users').document(_name).get().to_dict()['xrp']
        print(_name, "의 보유" + _coin + " : ", result)
    else:
        return 0

    return result

def modifyDollar(_target, _amount):
    print("user.py - modifyDollar()")

    dollar =  db.collection(u'users').document(_target).get().to_dict()['dollar']

    print(_target, "의 달라데이터 수정")
    print(_target, "의 달라: " + str(db.collection(u'users').document(_target).get().to_dict()['dollar']))
    print("추가할 액수: ", _amount)
    db.collection(u'users').document(_target).update({u'dollar': dollar + _amount})

    print("자산데이터 수정 완료")
    print("수정된", _target, "의 자산: ",  db.collection(u'users').document(_target).get().to_dict()['dollar'])
    
def modifyCoin(_target, _amount, _coin):
    print("user.py - modifyCoin()")
    
    print(_target, "의 코인데이터 수정")
    print("추가할 액수: ", _amount)

    if _coin == "웨이브":
        coin = db.collection(u'users').document(_target).get().to_dict()['waves']
        db.collection(u'users').document(_target).update({u'waves': coin + _amount})
        print("자산데이터 수정 완료")
    elif _coin == "비트코인":
        coin = db.collection(u'users').document(_target).get().to_dict()['btc']
        db.collection(u'users').document(_target).update({u'btc': coin + _amount})
        print("자산데이터 수정 완료")
    elif _coin == "이더리움":
        coin = db.collection(u'users').document(_target).get().to_dict()['eth']
        db.collection(u'users').document(_target).update({u'eth': coin + _amount})
        print("자산데이터 수정 완료")
    elif _coin == "도지":
        coin = db.collection(u'users').document(_target).get().to_dict()['doge']
        db.collection(u'users').document(_target).update({u'doge': coin + _amount})
        print("자산데이터 수정 완료")
    elif _coin == "라이트":
        coin = db.collection(u'users').document(_target).get().to_dict()['ltc']
        db.collection(u'users').document(_target).update({u'ltc': coin + _amount})
        print("자산데이터 수정 완료")
    elif _coin == "이더리움클래식":
        coin = db.collection(u'users').document(_target).get().to_dict()['etc']
        db.collection(u'users').document(_target).update({u'etc': coin + _amount})
        print("자산데이터 수정 완료")
    elif _coin == "루나클래식":
        coin = db.collection(u'users').document(_target).get().to_dict()['lunc']
        db.collection(u'users').document(_target).update({u'lunc': coin + _amount})
        print("자산데이터 수정 완료")
    elif _coin == "샌드박스":
        coin = db.collection(u'users').document(_target).get().to_dict()['sand']
        db.collection(u'users').document(_target).update({u'sand': coin + _amount})
        print("자산데이터 수정 완료")
    elif _coin == "비엔비":
        coin = db.collection(u'users').document(_target).get().to_dict()['bnb']
        db.collection(u'users').document(_target).update({u'bnb': coin + _amount})
        print("자산데이터 수정 완료")
    elif _coin == "리플":
        coin = db.collection(u'users').document(_target).get().to_dict()['xrp']
        db.collection(u'users').document(_target).update({u'xrp': coin + _amount})
        print("자산데이터 수정 완료")
    else:
        return 0
    
#=========================ITEM==================================
def checkBait(_target):
    print("user.py - checkBait")
    print("미끼를 탐색")
    result = db.collection(u'users').document(_target).get().to_dict()['bait']
    print("보유 미끼 수량: ", result)
    # 미끼가 있을 경우
    if result:
        return False 
    return True

def checkGrap(_target):
    print("user.py - checkGrap")
    print("착취 개수 조회")
    result = db.collection(u'users').document(_target).get().to_dict()['graps']
    print("조회 완료")
    return result

def checkKC(_target):
    print("user.py - checkKC")
    print("협박 개수 조회")
    result = db.collection(u'users').document(_target).get().to_dict()['kc']
    print("조회 완료")
    return result

def countKC(_target):
    result = db.collection(u'users').document(_target).get().to_dict()['kc']
    return result

def checkRKC(_target):
    print("user.py - checRKC")
    print("협박 개수 조회")
    result = db.collection(u'users').document(_target).get().to_dict()['rkc']
    print("조회 완료")
    return result

def checkVita(_target):
    print("user.py - checkVita")
    print("비타민 조회")
    result = db.collection(u'users').document(_target).get().to_dict()['vitamin']
    print("조회 성공")
    return result

def checkBK(_target):
    print("user.py - checkBK")
    print("바지락칼국수 조회")
    result = db.collection(u'users').document(_target).get().to_dict()['bk']
    print("조회 성공")
    if result:
        return False 
    return True

def checkWIS(_target):
    print("user.py - checkWIS")
    print("위스키 조회")
    result = db.collection(u'users').document(_target).get().to_dict()['wisky']
    print("조회 성공")
    return result

def checkOE(_target):
    print("user.py - checkOE")
    print("타조알 조회")
    result = db.collection(u'users').document(_target).get().to_dict()['ostrich']
    print("조회 성공")
    return result

def modifyRKC(_target, _amount):
    print("user.py - modifyRKC()")
    rkc = db.collection(u'users').document(_target).get().to_dict()['rkc']
    db.collection(u'users').document(_target).update({u'': rkc + _amount})
    print("협박 당한 개수 수정 완료")

def openOE():
    n = randint(1,100)
    if 1 <= n <= 40:
        result = "fail"
        url = "https://i.imgur.com/1In7USq.png"
    elif 41 <= n <= 50:
        result = "낙동강타조알"
        url = "https://i.imgur.com/zzW8cHS.jpg"
    elif 51 <= n <= 57:
        result = "강동완의발포비타민"
        url = "https://i.imgur.com/TmLMVLP.jpg"
    elif 58 <= n <= 64:
        result = "바지락칼국수"
        url = "https://i.imgur.com/ejBBFJm.jpg"
    elif 65 <= n <= 66:
        result = "고승환의 커터칼"
        url = "https://i.imgur.com/UBSG3DT.jpg"
    elif 67 <= n <= 76:
        result = "빡친 타조"
        url = "https://i.imgur.com/YUeLEz6.jpg"
    elif 77 <= n <= 92:
        result = "미끼"
        url = "https://i.imgur.com/P3vA4iV.jpg"
    elif 93 <= n <= 99:
        result = "열구의위스키"
        url = "https://i.imgur.com/luLEIYm.jpg"
    else:
        result = "착취의 손아귀"
        url = "https://i.imgur.com/cFFk2oA.jpg"

    return result, url

def addItem(_target, _item, _amount):
    print("user.py - addItme")
    if _item == "미끼":
        item = db.collection(u'users').document(_target).get().to_dict()['bait']
        db.collection(u'users').document(_target).update({u'bait': item + _amount})
    if _item == "열구의위스키":
        item = db.collection(u'users').document(_target).get().to_dict()['wisky']
        db.collection(u'users').document(_target).update({u'wisky': item + _amount})
    if _item == "강동완의발포비타민":
        item = db.collection(u'users').document(_target).get().to_dict()['vitamin']
        db.collection(u'users').document(_target).update({u'vitamin': item + _amount})
    if _item == "바지락칼국수":
        item = db.collection(u'users').document(_target).get().to_dict()['bk']
        db.collection(u'users').document(_target).update({u'bk': item + _amount})
    if _item == "낙동강타조알":
        item = db.collection(u'users').document(_target).get().to_dict()['ostrich']
        db.collection(u'users').document(_target).update({u'ostrich': item + _amount})
    if _item == "착취의 손아귀":
        item = db.collection(u'users').document(_target).get().to_dict()['graps']
        db.collection(u'users').document(_target).update({u'graps': item + _amount})
    if _item == "고승환의 커터칼":
        item = db.collection(u'users').document(_target).get().to_dict()['kc']
        db.collection(u'users').document(_target).update({u'kc': item + _amount})
    print("추가 완료")

def rmItem(_target, _item):
    print("user.py - rmItem")
    if _item == "미끼":
        item = db.collection(u'users').document(_target).get().to_dict()['bait']
        db.collection(u'users').document(_target).update({u'bait': item - 1})
    if _item == "열구의위스키":
        item = db.collection(u'users').document(_target).get().to_dict()['wisky']
        db.collection(u'users').document(_target).update({u'wisky': item - 1})
    if _item == "강동완의발포비타민":
        item = db.collection(u'users').document(_target).get().to_dict()['vitamin']
        db.collection(u'users').document(_target).update({u'vitamin': item - 1})
    if _item == "바지락칼국수":
        item = db.collection(u'users').document(_target).get().to_dict()['bk']
        db.collection(u'users').document(_target).update({u'bk': item - 1})
    if _item == "낙동강타조알":
        item = db.collection(u'users').document(_target).get().to_dict()['ostrich']
        db.collection(u'users').document(_target).update({u'ostrich': item - 1})
    if _item == "착취의 손아귀":
        item = db.collection(u'users').document(_target).get().to_dict()['graps']
        db.collection(u'users').document(_target).update({u'graps': item - 1})
    if _item == "고승환의 커터칼":
        item = db.collection(u'users').document(_target).get().to_dict()['kc']
        db.collection(u'users').document(_target).update({u'kc': item - 1})
    print("제거 완료")