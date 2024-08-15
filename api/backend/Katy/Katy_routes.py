########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

guardian = Blueprint('guardian', __name__)

# 1.1 Inserting medical needs for a child
@guardian.route('/guardian', methods=['POST'])
def med_needs():
    # Collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)
    # Extracting the variable
    c_id = the_data['camperID']
    m_id = the_data['medID']
    # Constructing the query
    query = 'insert into MedNeeds (camperID, medID) values ("'
    query += c_id + '", '
    query += m_id + ')'
    current_app.logger.info(query)
    # Executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    # Committing the changes to the database
    db.get_db().commit()
    # Returning a success message
    return 'Success!'


# 1.2 Getting required items for a given day
@guardian.route('/guardian/<c_date>', methods=['GET'])
def day_info(c_date):
    # Get a database cursor to execute the query
    cursor = db.get_db().cursor()
    the_query = '''
    SELECT ds.date, ri.requiredItems
    FROM DailySchedule ds
        JOIN ScheduleActivity sa ON ds.scheduleID = sa.scheduleID
        JOIN Activity a ON sa.activityID = a.activityID
        JOIN RequiredItems ri ON a.activityID = ri.activityID
    WHERE ds.date = %s;
    '''
    # Execute the SQL query with the given c_date
    cursor.execute(the_query, (c_date,))
    # Fetching all results from query execution
    the_data = cursor.fetchall()
    # Return error message if no data is found
    if not the_data:
        return make_response(jsonify({"error": "No data found for this date"}), 404)
    # Create a response object with the data
    the_response = make_response(jsonify(the_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response

# 1.3 Getting a child's counselor's contact info
@guardian.route('/guardian/CC/<c_id>', methods=['GET'])
def camper_info(c_id):
    # Get a database cursor to execute the query
    cursor = db.get_db().cursor()
    the_query = '''
    SELECT Staff.firstName, Staff.lastName, phoneNumber, email
    FROM Camper
        JOIN Staff ON Camper.staffID = Staff.staffID
    WHERE Camper.camperID = %s;
    '''
    # Execute the SQL query with the given c_id
    cursor.execute(the_query, (c_id,))
    # Fetching all results from query execution
    the_data = cursor.fetchall()
    # Return error message if no data is found
    if not the_data:
        return make_response(jsonify({"error": "No data found for this date"}), 404)
    # Create a response object with the data
    the_response = make_response(jsonify(the_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    
    return the_response

