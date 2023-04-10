
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Doctor( db.Model, SerializerMixin ):
    __tablename__ = 'doctors'
    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String )
    department = db.Column( db.String )
    appointments = db.relationship( 'Appointment', backref = 'doctor' )

class Appointment( db.Model, SerializerMixin ):
    __tablename__ = 'appointments'
    id = db.Column( db.Integer, primary_key = True )
    note = db.Column( db.String )
    doctor_id = db.Column( db.Integer, db.ForeignKey( 'doctors.id' ) )
    patient_id = db.Column( db.Integer, db.ForeignKey( 'patients.id' ) )

class Patient( db.Model, SerializerMixin ):
    __tablename__ = 'patients'
    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String )
    address = db.Column( db.String )
    appointments = db.relationship( 'Appointment', backref = 'patient' )