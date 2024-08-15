########################################################
# Camp Couunselor (Jackie) blueprint of endpoints 
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

# Creating a Blueprint for camp_counselor routes
camp_counselor = Blueprint('camp_counselor', __name__)


# 2.1: Staff info lookup within a camp session
@camp_counselor.route('/camp_counselor/<c_ID>', methods=['GET'])
def predict_value(c_ID):
    # Get a database cursor to execute the query
    cursor = db.get_db().cursor()
    the_query = f'''
    SELECT s.firstName, s.lastName, s.role, s.phoneNumber, s.email
    FROM Staff s
    JOIN CampSession cs ON s.sessionID = cs.sessionID
    WHERE s.campID = {c_ID}
    ;
    '''
    # Execute the SQL query
    cursor.execute(the_query)
    # Fetching all results from query execution
    the_data = cursor.fetchall()
    # Creating a response object with the data
    the_response = make_response(the_data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# 2.2: Deleting activity
@camp_counselor.route('/camp_counselor/<activityID>', methods=['DELETE'])
def delete_schedule(activityID):
   # Get a database cursor to execute the query
   cursor = db.get_db().cursor()
   query = '''
   DELETE FROM Activity 
   WHERE activityID  = %s;
    '''	
   # Execute the SQL deletion query: note that deletions will not be saved
   # throughout different user sessions to prevent conflicts caused by deletions
   cursor.execute(query, (activityID,))
   # Return a success message 
   return jsonify({"message": "Activity deleted successfully!"}), 200


# 2.3: Updating an activity description for a camp session
@camp_counselor.route('/camp_counselor/<activityID>', methods=['PUT'])
def update_activity(activityID):
    # Get a database cursor to execute the query
    new_description = request.get_json
    query = '''
    UPDATE Activity
    SET description = %s
    WHERE activityID = %s;
    '''
    # Execute the SQL update query
    cursor = db.get_db().cursor()
    cursor.execute(query, (new_description, activityID))
    db.get_db().commit()
    return jsonify({"message": "Activity updated successfully!"}), 200
