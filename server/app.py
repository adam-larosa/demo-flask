from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource
from flask_migrate import Migrate

from models import db, Doctor

app = Flask( __name__ )
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///meow.db'
migrate = Migrate( app, db )
db.init_app( app )
api = Api( app )

class Doctors( Resource ):
    def get( self ):
        doctors = []
        for d in Doctor.query.all():
            d_dict = {
                'id': d.id,
                'name': d.name,
                'department': d.department
            }
            doctors.append( d_dict )
        return make_response( jsonify(doctors), 200 )

api.add_resource( Doctors, '/doctors' )


if __name__ == '__main__':
    app.run( port = 8000, debug = True )