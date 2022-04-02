import json
import pandas as pd

#open Json file
fp=open('./finaldata.json','r',encoding='utf-8')
file=json.load(fp=fp)

#Transfer to dataframe and drop null columns
df=pd.DataFrame.from_dict(file)
nocolumn=['cityCode','countyCode','creatUser','createTime','endTime','id','offDate','offReason','parentid','preid',
          'provinceCode','qfDate','startTime','warehouseAddress','xkCompleteDate','xkProject','xkRemark']
df.drop(columns=nocolumn,axis=1,inplace=True)
#print(df.iloc[:,3:8].info())
df.to_csv("data.csv",encoding="utf_8_sig")