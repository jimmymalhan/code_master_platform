from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with

app=Flask(__name__)
api=Api(app)

DOCTORS = {
    1: {'first_name': 'Hibbert', 'last_name': 'Julius', 'appointments': {1: {'patient_first_name': 'Sterling', 'patient_last_name': 'Archer', 'date': '05/09/2018', 'time': '8:00 AM', 'kind': 'New Patient'}, 2: {'patient_first_name': 'Cyril', 'patient_last_name': 'Figis', 'date': '05/09/2018', 'time': '8:30 AM', 'kind': 'Follow-up'}, 3: {'patient_first_name': 'Ray', 'patient_last_name': 'Gilette', 'date': '05/09/2018', 'time': '9:00 AM', 'kind': 'Follow-up'}}},


    2: {'first_name': 'Krieger', 'last_name': 'Algernop', 'appointments': {1: {'patient_first_name': 'Lana', 'patient_last_name': 'Kane', 'date': '05/09/2018', 'time': '9:30 AM', 'kind': 'New Patient'}, 2: {'patient_first_name': 'Pam', 'patient_last_name': 'Poovey', 'date': '05/09/2018', 'time': '10:00 AM', 'kind': 'New Patient'}}},

    3: {'first_name': 'Riviera', 'last_name': 'Nick', 'appointments': {1: {'patient_first_name': 'Sterling', 'patient_last_name': 'Archer', 'date': '05/09/2018', 'time': '8:00 AM', 'kind': 'New Patient'}, 2: {'patient_first_name': 'Cyril', 'patient_last_name': 'Figis', 'date': '05/09/2018', 'time': '8:30 AM', 'kind': 'Follow-up'}, 3: {'patient_first_name': 'Ray', 'patient_last_name': 'Gilette', 'date': '05/09/2018', 'time': '9:00 AM', 'kind': 'Follow-up'}}}}


APPOINTMENTS = {
    1: {'patient_first_name': 'Sterling', 'patient_last_name': 'Archer', 'date': '05/09/2018', 'time': '8:00 AM', 'kind': 'New Patient'},
    2: {'patient_first_name': 'Cyril', 'patient_last_name': 'Figis', 'date': '05/09/2018', 'time': '8:30 AM', 'kind': 'Follow-up'},
    3: {'patient_first_name': 'Ray', 'patient_last_name': 'Gilette', 'date': '05/09/2018', 'time': '9:00 AM', 'kind': 'Follow-up'}
}

class Doctor(Resource):
    def get(self, id):
        abort_if_doctor_doesnt_exist(id)
        return DOCTORS[id]
    def delete(self, id): # delete a doctor
        abort_if_doctor_doesnt_exist(id)
        del DOCTORS[id]
        return '', 204
    def put(self, id): # update a doctor
        parser = reqparse.RequestParser()
        parser.add_argument('first_name')
        parser.add_argument('last_name')
        args = parser.parse_args()
        DOCTORS[id] = {'first_name': args['first_name'], 'last_name': args['last_name']}
        return DOCTORS[id], 201


class DoctorList(Resource): # doctor list class
    def get(self):
        return DOCTORS
    def post(self): # create a new doctor
        parser = reqparse.RequestParser()
        parser.add_argument('first_name')
        parser.add_argument('last_name')
        args = parser.parse_args()
        id = len(DOCTORS) + 1
        DOCTORS[id] = {'first_name': args['first_name'], 'last_name': args['last_name']}
        return DOCTORS[id], 201


class DoctorAppointments(Resource): 
    def get(self, id):
        abort_if_doctor_doesnt_exist(id)
        return DOCTORS[id]['appointments']

    def post(self, id): # post a new appointment
        parser = reqparse.RequestParser()
        parser.add_argument('patient_first_name')
        parser.add_argument('patient_last_name')
        parser.add_argument('date')
        parser.add_argument('time')
        parser.add_argument('kind')
        args = parser.parse_args()
        if args['time'] not in DOCTORS[id]['appointments']: # if the time interval doesn't exist, create it
            DOCTORS[id]['appointments'][args['time']] = {'patient_first_name': args['patient_first_name'], 'patient_last_name': args['patient_last_name'], 'date': args['date'], 'time': args['time'], 'kind': args['kind']}
            return DOCTORS[id]['appointments'][args['time']], 201
        else:
            return '', 409 # 409 means conflict

    def abort_if_time_interval_not_valid(self, time_interval): # check if the time interval is valid
        if time_interval not in APPOINTMENTS:
            abort(404, message="Time interval {} doesn't exist".format(time_interval))

    
    def abort_if_appointment_more_than_3_atSameTime(self, id, time_interval): # check if the appointment is more than 3 at the same time
        if len(DOCTORS[id]['appointments'][time_interval]) > 3:
            abort(409, message="Appointment at {} is full".format(time_interval))

    def delete(self, id, time_interval): # delete an appointment
        abort_if_doctor_doesnt_exist(id)
        abort_if_time_interval_not_valid(time_interval)
        del DOCTORS[id]['appointments'][time_interval]
        return '', 204

    def put(self, id, time_interval): # update an appointment
        parser = reqparse.RequestParser()
        parser.add_argument('patient_first_name')
        parser.add_argument('patient_last_name')
        parser.add_argument('date')
        parser.add_argument('time')
        parser.add_argument('kind')
        args = parser.parse_args()
        abort_if_doctor_doesnt_exist(id)
        abort_if_time_interval_not_valid(time_interval)
        abort_if_appointment_more_than_3_atSameTime(id, time_interval)
        DOCTORS[id]['appointments'][time_interval] = {'patient_first_name': args['patient_first_name'], 'patient_last_name': args['patient_last_name'], 'date': args['date'], 'time': args['time'], 'kind': args['kind']}
        return DOCTORS[id]['appointments'][time_interval], 201


class AppointmentList(Resource):
    def get(self):
        return APPOINTMENTS
    def post(self): # create a new appointment
        parser = reqparse.RequestParser()
        parser.add_argument('patient_first_name')
        parser.add_argument('patient_last_name')
        parser.add_argument('date')
        parser.add_argument('time')
        parser.add_argument('kind')
        args = parser.parse_args()
        appointment_id = len(APPOINTMENTS) + 1
        APPOINTMENTS[appointment_id] = {'patient_first_name': args['patient_first_name'], 'patient_last_name': args['patient_last_name'], 'date': args['date'], 'time': args['time'], 'kind': args['kind']}
        return APPOINTMENTS[appointment_id], 201


def abort_if_doctor_doesnt_exist(id): # check if the doctor exists
    if id not in DOCTORS:
        abort(404, message="Doctor {} doesn't exist".format(id))


api.add_resource(DoctorList, '/doctors')
api.add_resource(Doctor, '/doctors/<int:id>')
api.add_resource(DoctorAppointments, '/doctors/<int:id>/appointments')
api.add_resource(AppointmentList, '/appointments')


if __name__ == '__main__':
    app.run(debug=True)