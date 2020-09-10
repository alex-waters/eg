import requests
import pickle
import pandas as pd

ENDPOINT = 'https://api.postcodes.io/postcodes/'

users = pd.read_csv('egl_typed.csv')
postcodes = list(set(users['postcode.1']))

lat = []
long = []
ccg = []
loc_code = []

for pc in postcodes:
    try:
        send = requests.get(ENDPOINT+pc)
        receive = send.json()
        rlt = receive['result']['latitude']
        rlo = receive['result']['longitude']
        rccg = receive['result']['ccg']
        rlc = receive['result']['codes']['admin_district']
        
        lat.append(rlt)
        long.append(rlo)
        ccg.append(rccg)
        loc_code.append(rlc)
    except:
        lat.append(None)
        long.append(None)
        ccg.append(None)
        loc_code.append(None)

try:
    geo_data = pd.DataFrame({
        'postcode': postcodes,
        'lat': lat,
        'long': long,
        'ccg': ccg,
        'loc_code': loc_code
    })
    geo_data.to_csv('geo_data_1.csv')
except:
    pickle.dump([lat, long, ccg, loc_code, postcodes], open('received_gep.p', 'wb'))
    