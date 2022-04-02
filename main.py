from Scrap import id_list
import requests
import json

#fetch info from each webpage and store them in Json file
if __name__=='__main__':
    final_data = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    #Get the XHR package of every page, which is a fixed URL plus id
    inner = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id
        }
        try:
            detail = requests.post(inner, data=data, headers=headers)
            if detail.content:
                temp=detail.json()
            final_data.append(temp)
        except:
            print("Error parsing")

    #Save data as json file
    fp=open("./finaldata.json","w",encoding="utf-8")
    json.dump(final_data,fp=fp,ensure_ascii=False)

