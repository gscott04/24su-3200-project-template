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


# 2.2: Deleting a daily schedule for a camp session
@camp_counselor.route('/camp_counselor/<campID>/<sessionID>', methods=['DELETE'])
def delete_schedule(campID, sessionID):
   # Get a database cursor to execute the query
   cursor = db.get_db().cursor()
   the_query = f'''
   DELETE FROM DailySchedule 
   USING DailySchedule
   WHERE DailySchedule.date = 7/27/2024
				AND DailySchedule.campID = {campID}
				AND DailySchedule.sessionID = {sessionID};
                '''	
   # Execute the SQL deletion query	
   cursor.execute(the_query (campID, sessionID))
   # Commit the changes to the database
   db.get_db.commit() 
   # Return a success message 
   return jsonify({"message": "Daily schedule deleted successfully"}), 200


# 2.3: Updating an activity description for a camp session
@camp_counselor.route('/camp_counselor', methods=['PUT'])
def update_activity():
    # Log the incoming request
    current_app.logger.info('PUT /camp_counselor route')
    # Get the JSON data from the request
    camp_info = request.json
    # Extract the activity description from the JSON data
    camp_info = camp_info['description']
    query = f'''
    UPDATE Activity
    SET Activity.description = '%s'
    FROM Activity
    JOIN ScheduleActivity ON Activity.activityId = ScheduleActivity.activityId
    JOIN DailySchedule ON ScheduleActivity.scheduleId = DailySchedule.scheduleId
    WHERE DailySchedule.date = 8/5/2024
    AND DailySchedule.campID = 16
    AND DailySchedule.sessionID = 24;
    '''
    # Execute the update query with new activity description
    data = (camp_info)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    # Commit the updates to the database 
    db.get_db().commit()
    # Return a success message 
    return 'activity updated!'
