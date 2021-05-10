import requests;
import json;
import pandas as pd;

response = requests.get("https://servicodados.ibge.gov.br/api/v1/paises/AR%7CBR/indicadores/77819%7C77820")

data = response.json()

aux2 = {}


for key in data:
    aux1 = {}
    for series in key['series']:    

        for pais in series['pais']['id']:   
            for entry in series['serie']:
    
                if any(entry.values()):
                    aux1[list(entry.keys())[0]] = list(entry.values())[0]
                    aux2[series['pais'].get('id')+" - "+str(key['id'])] =aux1


"""
for key in data:
    c = {}
    for series in key['series']:    
        #print("PAIS: ", series['pais']['id'])
        for entry in key['series'][0]['serie']:
            if any(entry.values()):
                c[list(entry.keys())[0]] = list(entry.values())[0]
                
            z[series['pais']['id']+" - "+key['id']] =c



"""
dados = pd.read_json(json.dumps(aux2))
dados.reset_index(level=0, inplace=True)
dados.rename(columns={'index': 'Data'}, inplace = True)
aux1 = list(dados.columns.values)
aux1.pop(0)
dados = pd.melt(dados, id_vars= 'Data', value_vars=aux1)
#dados = dados.set_index("Data")
dados['value'] = dados['value'].astype(str)
dados['value'] = dados['value'].str.replace('.', ',')
dados['value'] = dados['value'].astype(float)
print(dados)
"""
for key in data:
    print(key['id'])

    for ps in key['series']:    
        c = {}
        for pais in ps:   
            for entry in key['series'][0]['serie']:
                if any(entry.values()):
                    c['id','pais',list(entry.keys())[0]] = [key['id'],ps['pais'].get('id'),list(entry.values())[0]]
                    #c[list(entry.keys())[0]] = list(entry.values())[0]
                    print(ps['pais'].get('id'))

"""




