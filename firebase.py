# Standard importations
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Function to post JSON data to Firebase
def postToFirebase(child, data): {
    ref.child(child).set(data)
}

# Reading private certificate
cred = credentials.Certificate('./auth/covid19br-dashboard-auth.json')

# Initializing the application based on given credential
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://covid19br-dashboard-default-rtdb.firebaseio.com/'
})

# Switching to the root of DB
ref = db.reference('/')

# Deleting previous data
ref.delete()

### READING DATA AND SENDING TO FIREBASE ###
state_list = ['AC', 'AP', 'AM', 'TO', 'PA', 'RR', 'RO', 'AL', 'BA', 'PB', 'PE', 'SE', 'PI', 'CE', 'MA', 'RN', 'MT', 'GO', 'MS', 'DF', 'SP', 'ES', 'RJ', 'MG',  'SC', 'RS', 'PR']

postToFirebase("national-data", pd.read_csv("./data/national/covid19-dataset-brasil.csv").to_dict())
postToFirebase("daily-data", pd.read_csv("./data/daily/covid19-dataset-today.csv").to_dict())
postToFirebase("epi-weeks-data", pd.read_csv('./data/extras/covid19-dataset-epi-weeks.csv').to_dict())

postToFirebase("regional-data/norte", pd.read_csv("./data/regions/covid19-Norte.csv").to_dict())
postToFirebase("regional-data/nordeste", pd.read_csv("./data/regions/covid19-Nordeste.csv").to_dict())
postToFirebase("regional-data/centro-oeste", pd.read_csv("./data/regions/covid19-Centro-Oeste.csv").to_dict())
postToFirebase("regional-data/sudeste", pd.read_csv("./data/regions/covid19-Sudeste.csv").to_dict())
postToFirebase("regional-data/sul", pd.read_csv("./data/regions/covid19-Sul.csv").to_dict())

for state in state_list:
    postToFirebase(f"state-data/{state}", pd.read_csv(f"./data/states/{state}/covid19-dataset-{state}.csv").to_dict())