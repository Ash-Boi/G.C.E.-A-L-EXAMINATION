import requests
import json


token='Bot ගෙ api key එක මෙතනට දාන්න'
method='sendMessage'

def get_data(index_no):
    try:
        r=requests.get('https://www.doenets.lk/result/service/AlResult/'+str(index_no))
        jsondata = json.loads(r.text)
        if jsondata['year']==None:
            print(str(index_no)+' is not valid')
        else:
            
            year=str(jsondata['year'])
            name=jsondata['name']
            indexNo=str(jsondata['indexNo'])
            nic=str(jsondata['nic'])
            districtRank=str(jsondata['districtRank'])
            islandRank=str(jsondata['islandRank'])
            zScore=str(jsondata['zScore'])
            stream=jsondata['stream']
            Sub1name=jsondata['subjectResults'][0]['subjectName']
            Sub1result=jsondata['subjectResults'][0]['subjectResult']
            Sub2name=jsondata['subjectResults'][1]['subjectName']
            Sub2result=jsondata['subjectResults'][1]['subjectResult']
            Sub3name=jsondata['subjectResults'][2]['subjectName']
            Sub3result=jsondata['subjectResults'][2]['subjectResult']
            Sub4name=jsondata['subjectResults'][3]['subjectName']
            Sub4result=jsondata['subjectResults'][3]['subjectResult']
            Sub5name=jsondata['subjectResults'][4]['subjectName']
            Sub5result=jsondata['subjectResults'][4]['subjectResult']
            S1=('Year')
            S2=('Name')
            S3=('Index No')
            S4=('NIC No')
            S5=('District Rank')
            S6=('Island Rank')
            S7=('Z-Score')
            S8=('Subject Stream')
            S9=('SUB1')
            S10=('SUB2')
            S11=('SUB3')
            S12=('✅')
            S13=('✅🇱🇰script edit by @ash_boi🇱🇰✅')
            S14=('මුළු මෙව්ව එක')
            
            print(S1)
            print(S2)
            print(S3)
            print(S4)
            print(S5)
            print(S6)
            print(S7)
            print(S8)
            print(S9)
            print(S10)
            print(S11)
            print(S12)
            print(S13)
            print(year)
            print(name)
            print(indexNo)
            print(nic)
            print(districtRank)
            print(islandRank)
            print(zScore)
            print(stream)
            print(Sub1name)
            print(Sub1result)
            print(Sub2name)
            print(Sub2result)
            print(Sub3name)
            print(Sub3result)
            print(Sub4name)
            print(Sub4result)
            print(Sub5name)
            print(Sub5result)
	
            msg=S1+' 👉 '+year+''+S12+'\n'+S2+' 👉 '+name+'\n'+S3+' 👉 '+indexNo+'\n'+S4+' 👉 '+nic+'\n'+S5+' 👉 '+districtRank+'\n'+S6+' 👉 '+islandRank+'\n'+S7+' 👉 '+zScore+'\n''\n'+S8+' 👉 '+stream+'\n''\n'+S9+' 👉 '+Sub1name+' ➡️ '+Sub1result+'\n'+S10+' 👉 '+Sub2name+' ➡️ '+Sub2result+'\n'+S11+' 👉 '+Sub3name+' ➡️ '+Sub3result+'\n''\n'+Sub4name+' ➡️ '+Sub4result+'\n'+Sub5name+' ➡️ '+Sub5result+'\n''\n'+S14+' 👉 '+Sub1result+' '+Sub2result+' '+Sub3result+'\n'+S13

            response = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(token, method),
            data={'chat_id':-Channel ID එක, 'text': msg}
            ).json() 
    except:
        print('err')


for i in range(1000000,9999999):
	get_data(i)

response = requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(token, method),
        data={'chat_id':-Channel ID එක, 'text': 'Done start again'}
        ).json()
