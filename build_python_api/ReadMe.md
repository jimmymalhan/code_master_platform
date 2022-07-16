## Install requriements
- pip install -r requirements.txt

```virtalenv - notable```

## Run the file
```python flask_restful_api.py```

#### create a new doctor
- curl  -X POST -H "Content-Type: application/json" -d '{"first_name": "Hibbert", "last_name": "Julius"}' http://localhost:5000/doctors

#### get all doctors
- curl  -X GET http://localhost:5000/doctors 

#### get doctor 1
- curl  -X GET http://localhost:5000/doctors/1 

#### get doctor 1 appointments
- curl  -X GET http://localhost:5000/doctors/1/appointments 

#### create a new appointment
- curl  -X POST -H "Content-Type: application/json" -d '{"patient_first_name": "Sterling", "patient_last_name": "Archer", "date": "05/09/2018", "time": "11:15 AM", "kind": "New Patient"}' http://localhost:5000/appointments 

####get all appointments
- curl  -X GET http://localhost:5000/appointments

#### check if the doctor exists
- curl  -X GET http://localhost:5000/doctors/100


## Troubleshooting
#### Already running port
- lsof -i:5000
#### Kill forcefully
- kill -9 <49554>