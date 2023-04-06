import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
 
cred = credentials.Certificate("faceattendancerealtime-fd2-firebase-adminsdk-rjc0b-b4ce7e8443.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-fd2-default-rtdb.firebaseio.com/"
})
 
ref = db.reference('Students')
 
data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": null,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": null,
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": null,
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1420":
        {
          "name":"Samir Sengupta",
          "major":"Data Science",
          "starting_year":2021,
          "total_attendance":8,
          "standing":null,
          "year":3,
          "last_attendance_time":"2023-3-11 00:54:34"
        },
    "2721":
        {
          "name":"Sowmiah Nadar",
          "major":"Data Science",
          "starting_year":2021,
          "total_attendance":7,
          "standing":null,
          "year":3,
          "last_attendance_time":"2023-3-11 00:54:34"
        },
    "1567":
        {
          "name":"Sundar Pichai",
          "major":"Data Science",
          "starting_year":2021,
          "total_attendance":4,
          "standing":null,
          "year":3,
          "last_attendance_time":"2023-3-11 00:54:34"
        },
    "6543":
        {
          "name":"MS Dhoni",
          "major":"Data Science",
          "starting_year":2021,
          "total_attendance":0,
          "standing":null,
          "year":3,
          "last_attendance_time":"2023-3-11 00:54:34"
        },
    "423546":
        {
          "name":"Kaushalya Yadav",
          "major":"Data Science",
          "starting_year":2021,
          "total_attendance":5,
          "standing":null,
          "year":3,
          "last_attendance_time":"2023-3-11 00:54:34"
        },
    "83432":
        {
          "name":"Akansha Yadav",
          "major":"Data Science",
          "starting_year":2021,
          "total_attendance":5,
          "standing":null,
          "year":3,
          "last_attendance_time":"2023-3-11 00:54:34"
        },
    "160147":
        {
          "name":"Priti Yadav",
          "major":"Data Science",
          "starting_year":2021,
          "total_attendance":6,
          "standing":null,
          "year":3,
          "last_attendance_time":"2023-3-11 00:54:34"
        },
    "845315":
        {
          "name":"Vikas Pandey",
          "major":"Professor",
          "starting_year":2020,
          "total_attendance":20,
          "standing":null,
          "year":10,
          "last_attendance_time":"2023-3-11 00:54:34"
        },
    "1806133":
        {
          "name":"Hitesh Mishra",
          "major":"Professor",
          "starting_year":2022,
          "total_attendance":15,
          "standing":null,
          "year":10,
          "last_attendance_time":"2023-3-11 00:54:34"
        },
    "843364":
        {
          "name":"Dr.Vishesh shrivastava",
          "major":"Professor",
          "starting_year":2022,
          "total_attendance":15,
          "standing":null,
          "year":10,
          "last_attendance_time":"2023-3-11 00:54:34"
        },
    "68785":
        {
          "name":"Prashant Chaubey",
          "major":"Professor",
          "starting_year":2022,
          "total_attendance":15,
          "standing":null,
          "year":10,
          "last_attendance_time":"2023-3-11 00:54:34"
        },
    "578525":
        {
          "name":"Dr.Sanjay Mishra",
          "major":"Professor",
          "starting_year":2022,
          "total_attendance":15,
          "standing":null,
          "year":10,
          "last_attendance_time":"2023-3-11 00:54:34"
        },
    "587690":
        {
          "name":"Devang Thakar",
          "major":"Professor",
          "starting_year":2022,
          "total_attendance":15,
          "standing":null,
          "year":10,
          "last_attendance_time":"2023-3-11 00:54:34"
        },
    "66378":
        {
          "name":"Manish Singh",
          "major":"Professor",
          "starting_year":2022,
          "total_attendance":15,
          "standing":null,
          "year":10,
          "last_attendance_time":"2023-3-11 00:54:34"
        },
    "83467":
        {
          "name":"Mrunali Sawant",
          "major":"Professor",
          "starting_year":2022,
          "total_attendance":15,
          "standing":null,
          "year":10,
          "last_attendance_time":"2023-3-11 00:54:34"
        }
}

 
for key, value in data.items():
    ref.child(key).set(value)
