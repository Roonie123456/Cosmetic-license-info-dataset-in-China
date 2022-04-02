import requests

#Get id of every page
post_url="http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}
id_list=[]
for page in range(1,387):
  page=str(page)
  data={
    'on': 'true',
    'page': page,
    'pageSize': '15',
    'productName':'',
    'conditionType': '1',
    'applyname':'',
    'applysn':''
  }
  try:
    response=requests.post(post_url,data=data,headers=headers)
    if response.content:
        data=response.json()
        for item in data['list']:
            id_list.append(item['ID'])
  except:
    print('error parsing')