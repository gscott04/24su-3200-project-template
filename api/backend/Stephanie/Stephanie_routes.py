########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

app_admin = Blueprint('app_admin', __name__)

import traceback
from flask import jsonify, current_app

@app_admin.route('/app_admin/CD/<adminID>', methods=['GET'])
def get_directors(adminID):
    try:
        cursor = db.get_db().cursor()
        the_query = '''SELECT campDirectorID FROM Admin a
                            JOIN Location l ON a.adminID = l.adminID
                            JOIN CampLoc cl ON l.locationID = cl.locationID
                            JOIN Camp c ON cl.campID = c.campID
                            WHERE a.adminID = %s;
        '''
        cursor.execute(the_query, (adminID,))
        the_Data = cursor.fetchall()
        
        if not the_Data:
            return jsonify({"message": f"No data found for admin ID {adminID}"}), 404
        
        the_response = []
        for row in the_Data:
            if isinstance(row, dict):
                the_response.append({"campDirectorID": row.get('campDirectorID')})
            elif isinstance(row, (list, tuple)):
                the_response.append({"campDirectorID": row[0] if row else None})
            else:
                the_response.append({"campDirectorID": row if row is not None else None})
        
        return jsonify(the_response), 200
    except Exception as e:
        return jsonify({"error": "An internal server error occurred"}), 500
    
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
   
    the_response = []
    for row in the_Data:
        if isinstance(row, dict):
            the_response.append({"phone": row.get('phone'), "email": row.get('email')})
        elif isinstance(row, (list, tuple)):
            the_response.append({"phone": row[0] if len(row) > 0 else None, "email": row[1] if len(row) > 1 else None})
        else:
            the_response.append({"phone": row, "email": row})
    
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