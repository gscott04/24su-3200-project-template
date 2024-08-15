########################################################
# App Admin (Stephanie) blueprint of endpoints
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

# Creating a Blueprint for app_admin routes
app_admin = Blueprint('app_admin', __name__)

# 4.1: Getting director ID
@app_admin.route('/app_admin/CD/<adminID>', methods=['GET'])
def get_directors(adminID):
    try:
        # Get a database cursor to execute the query
        cursor = db.get_db().cursor()
        the_query = '''
        SELECT campDirectorID FROM Admin a
        JOIN Location l ON a.adminID = l.adminID
        JOIN CampLoc cl ON l.locationID = cl.locationID
        JOIN Camp c ON cl.campID = c.campID
        WHERE a.adminID = %s;
        '''
        # Execute the SQL query with provided adminID
        cursor.execute(the_query, (adminID,))
        # Fetching all results from query execution
        the_Data = cursor.fetchall()
        # Return error message if no data is found
        if not the_Data:
            return jsonify({"message": f"No data found for admin ID {adminID}"}), 404
        # Prepare the response data
        the_response = []
        for row in the_Data:
            # Handle different possible row structures 
            if isinstance(row, dict):
                the_response.append({"campDirectorID": row.get('campDirectorID')})
            elif isinstance(row, (list, tuple)):
                the_response.append({"campDirectorID": row[0] if row else None})
            else:
                the_response.append({"campDirectorID": row if row is not None else None})
        # Return the response as JSON with 200 OK status 
        return jsonify(the_response), 200
    except Exception as e:
        # If an error occurs, return a 500 Internal Server Error
        return jsonify({"error": "An internal server error occurred"}), 500


# 4.2: Getting guardian contact info
@app_admin.route('/app_admin/<adminID>', methods=['GET'])
def get_contacts(adminID):
    # Get a database cursor to execute the query
    cursor = db.get_db().cursor()
    the_query = f'''
    SELECT g.email, g.phone
    FROM Admin a
    JOIN Location l ON a.adminID = l.adminID
    JOIN CampLoc cl ON l.locationID = cl.locationID
    JOIN Camp c ON cl.campID = c.campID
    JOIN Camper cm ON c.campID = cm.campID
    JOIN Guardian g ON cm.guardianID = g.guardianID
    WHERE a.adminID = {adminID}
    LIMIT 10;
    '''
    # Execute the SQL query
    cursor.execute(the_query) 
    # Fetching all results from query execution
    the_Data = cursor.fetchall()
    # Create a response object 
    the_response = make_response(the_Data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response  


# 4.3: Getting camp contact info
@app_admin.route('/app_admin/AC/<adminID>', methods=['GET']) 
def admin_contacts(adminID): 
    # Get a database cursor to execute the query
    cursor = db.get_db().cursor()
    the_query = '''
    SELECT c.phone, c.email, a.adminID FROM Admin a
    JOIN Location l ON a.adminID = l.adminID
    JOIN CampLoc cl ON l.locationID = cl.locationID
    JOIN Camp c ON cl.campID = c.campID 
    WHERE a.adminID = %s;
    '''
    # Execute the SQL query with the provided adminID
    cursor.execute(the_query, (adminID,)) 
    # Fetching all results from query execution
    the_Data = cursor.fetchall()
    # Prepare the response data
    the_response = []
    for row in the_Data:
        # Handle different possible row structures
        if isinstance(row, dict):
            the_response.append({"phone": row.get('phone'), "email": row.get('email')})
        elif isinstance(row, (list, tuple)):
            the_response.append({"phone": row[0] if len(row) > 0 else None, "email": row[1] if len(row) > 1 else None})
        else:
            the_response.append({"phone": row, "email": row})
    # Return the response as a JSON
    return jsonify(the_response), 200