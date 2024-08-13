########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

app_admin = Blueprint('app_admin', __name__)

@app_admin.route(‘/app_admin/<adminID>’, method[‘GET’]) 
def get_directors(adminID):
    cursor = db.get_db().cursor()
    the_query = 'SELECT campDirectorID FROM Admin NATURAL JOIN Location NATURAL JOIN CampLocation NATURAL JOIN Camp Where adminID = adminID;'.format(adminID) 
    cursor.execute(the_query) 
    the_Data = cursor.fetchall()
    the_response = make_response(the_Data)
    the_response.status_code = 200
    the_response.mimetype = ‘application/json’

    return the_response 

@app_admin.route(‘/app_admin/<adminID>’, method[‘GET’]) 
def contact_info(adminID): 
    cursor = db.get_db().cursor()
    the_query = 'SELECT campPhone, campEmail FROM Admin NATURAL JOIN Location NATURAL JOIN CampLocation NATURAL JOIN Camp Where adminID = adminID;'.format(adminID)
    cursor.execute(the_query) 
    the_Data = cursor.fetchall()
    the_response = make_response(the_Data)
    the_response.status_code = 200
    the_response.mimetype = ‘application/json’

    return the_response 

@app_admin.route(‘/app_admin/<admin_id>’, method[‘GET’]) 
def get_contacts(adminID) 
    cursor = db.get_db().cursor()
    the_query = 'SELECT guardianEmail, phoneNumber FROM Admin NATURAL JOIN Location NATURAL JOIN CampLocation NATURAL JOIN Camp NATURAL JOIN Camper NATURAL JOIN Guardian WHERE adminID = adminID Limit 10;'.format(adminID)
    cursor.execute(the_query) 
    the_Data = cursor.fetchall()
    the_response = make_response(the_Data)
    the_response.status_code = 200
    the_response.mimetype = ‘application/json’

    return the_response  