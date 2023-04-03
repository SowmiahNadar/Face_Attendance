import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# Fetch the service account key JSON file contents
cred = credentials.Certificate('faceattendancerealtime-45fd2-firebase-adminsdk-rjc0b-b4ce7e8443.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://faceattendancerealtime-45fd2-default-rtdb.firebaseio.com/'
})

# Get a database reference
ref = db.reference('/')

# Export the data to a JSON file
data = ref.get()
with open('firebase_data.json', 'w') as f:
    json.dump(data, f, indent=4)
