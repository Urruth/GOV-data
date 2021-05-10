import requests as rq 
import pandas as pd  
#import json

restapi = rq.get('https://servicodados.ibge.gov.br/api/v1/paises/BR|AR/indicadores/77818')
x = restapi.json()

#loads(x) 


#df=pd.read_json(x)
 
#df