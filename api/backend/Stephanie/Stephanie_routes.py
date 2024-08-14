########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

app_admin = Blueprint('app_admin', __name__)

@app_admin.route('/app_admin/CD/<adminID>', methods=['GET'])
def get_directors(adminID):
    cursor = db.get_db().cursor()
    the_query = '''SELECT campDirectorID FROM Admin NATURAL JOIN Location NATURAL JOIN CampLoc NATURAL JOIN Camp Where adminID = %s;
    '''
    cursor.execute(the_query, (adminID,))
    the_Data = cursor.fetchall()
    
    # Convert the data to a list of dictionaries
    the_response = [{"campDirectorID": row[0]} for row in the_Data]
    
    return jsonify(the_response), 200

@app_admin.route('/app_admin/<adminID>', methods=['GET']) 
def admin_contacts(adminID): 
    cursor = db.get_db().cursor()
    the_query = '''SELECT c.phone, c.email, a.adminID FROM Admin a
                        JOIN Location l ON a.adminID = l.adminID
                        JOIN CampLoc cl ON l.locationID = cl.locationID
                        JOIN Camp c ON cl.campID = c.campID 
                        WHERE a.adminID = %s;
    '''
    cursor.execute(the_query, (adminID,)) 
    the_Data = cursor.fetchall()
    the_response = [{"phone": row[0], "email": row[1]} for row in the_Data]
    return jsonify(the_response), 200

@app_admin.route('/app_admin/<admin_id>', methods=['GET'])
def get_contacts(adminID):
    cursor = db.get_db().cursor()
    the_query = '''SELECT guardianEmail, phoneNumber FROM Admin NATURAL JOIN Location NATURAL JOIN CampLoc NATURAL JOIN Camp NATURAL JOIN Camper NATURAL JOIN Guardian WHERE adminID = adminID Limit 10;
    '''.format(adminID)
    cursor.execute(the_query) 
    the_Data = cursor.fetchall()
    the_response = make_response(the_Data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response  