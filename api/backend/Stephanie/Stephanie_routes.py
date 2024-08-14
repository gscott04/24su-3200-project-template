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
        
        # Print raw data for debugging
        current_app.logger.info(f"Raw data fetched for adminID {adminID}: {the_Data}")
        current_app.logger.info(f"Type of the_Data: {type(the_Data)}")
        if the_Data:
            current_app.logger.info(f"Type of first item in the_Data: {type(the_Data[0])}")
        
        # Check if the_Data is empty
        if not the_Data:
            return jsonify({"message": f"No data found for admin ID {adminID}"}), 404
        
        # Convert the data to a list of dictionaries, handling different data structures
        the_response = []
        for row in the_Data:
            if isinstance(row, dict):
                the_response.append({"campDirectorID": row.get('campDirectorID')})
            elif isinstance(row, (list, tuple)):
                the_response.append({"campDirectorID": row[0] if row else None})
            else:
                the_response.append({"campDirectorID": row if row is not None else None})
        
        # Print formatted response for debugging
        current_app.logger.info(f"Formatted response: {the_response}")
        
        return jsonify(the_response), 200
    except Exception as e:
        # Log the full error traceback
        current_app.logger.error(f"An error occurred for adminID {adminID}: {str(e)}")
        current_app.logger.error(traceback.format_exc())
        
        # In development, return detailed error info
        if current_app.debug:
            return jsonify({
                "error": str(e),
                "traceback": traceback.format_exc()
            }), 500
        # In production, return a generic error message
        else:
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