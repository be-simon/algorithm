import requests
import json

baseurl = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
token = '44c304af0bd0dcdf5c96a88655efb937'

req = requests.post(baseurl + '/start',headers={'X-Auth-Token':token} , params={'problem':2})
authkey = req.json()['auth_key']

headers={'Authorization':authkey}

print('>>> start -----------------')
print(authkey)

def getWaiting():
    req = requests.get(baseurl+'/waiting_line', headers=headers)
    return req.json()['waiting_line']

def getGameResult():
    req = requests.get(baseurl + '/game_result', headers=headers)
    return req.json()['game_result']

def getUserInfo():
    req = requests.get(baseurl+'/user_info', headers=headers)
    return req.json()['user_info']

def match(data_list):
    data = {"pairs": data_list}
    req = requests.put(baseurl + '/match', headers=headers, data=json.dumps(data))
    return req.json()

def changeGrade(commands):
    data = {"commands": commands}
    req = requests.put(baseurl + '/change_grade', headers=headers, data=json.dumps(data))

###


def orderByGrade(uinfo):
#     print('>>> order by grade')
    wlist = getWaiting()
    user_to_grade = dict()
        
    for u in wlist:
        uid = u['id']
        turn = u['from']
        ugrade = uinfo[uid-1]['grade']
        user_to_grade[uid] = (ugrade, turn)

    return sorted(user_to_grade.items(), key=lambda x: x[1])


def getMatchList(order_by_grade):
#     print('>>> get match list')
    match_list = []
    while order_by_grade:
        if len(order_by_grade) >= 2:
            u1, gt1 = order_by_grade.pop()
            ug1 = gt1[0]
            u2, gt2 = order_by_grade.pop()
            ug2 = gt2[0]
            
            if abs(ug1 - ug2) < 250:
                match_list.append([u1, u2])
            else:
                order_by_grade.append((u2, gt2))
        else:
            break

    return match_list


def simulateGame(uinfo):
    ordered = orderByGrade(uinfo)
    ml = getMatchList(ordered)

    res = match(ml)
    print(res)
    return res

def change(results, uinfo):
    commands = []
    for result in results:
        win = result['win']
        lose = result['lose']
        taken = result['taken']
        
        wg = uinfo[win-1]['grade']
        lg = uinfo[lose-1]['grade']

        delta = 1 / (1 + pow(10, abs(wg - lg) / 400))
        k = 500
        
        if taken > 10:
            commands.append({"id": win, "grade": wg + int(k * (1-delta))})
            commands.append({"id": lose, "grade": lg + int(k * (0-delta))})
    
    changeGrade(commands)


    
init_commands = [{"id": i, "grade": 5000} for i in range(1, 901)]
changeGrade(init_commands)

status = 1
i = 0
while status:
    if i % 3 == 0:
        uinfo = getUserInfo()
        res = simulateGame(uinfo)
        if res['status'] == 'ready':
            status = 1
        else:
            status = 0
    else:
        match([])
        
    result = getGameResult()
    if result:
        change(result, uinfo)
    
    i += 1


req = requests.get(baseurl + '/score', headers=headers)
print(req.json())
