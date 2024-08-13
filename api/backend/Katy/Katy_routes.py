########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

guardians = Blueprint('guardians', __name__)

@guardians.route('/guardians/<c_date>', methods=['GET'])
def day_info(c_date):
    cursor = db.get_db().cursor
    the_query = '''
    SELECT date, requiredItems
        FROM DailySchedule NATURAL JOIN ScheduleActivity NATURAL JOIN Activity NATURAL JOIN RequiredItems
        WHERE date = c_date;
'''
    cursor.execute(the_query)
    the_data = cursor.fetchall()
    the_response = make_response(the_data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all customers from the DB
@guardians.route('/guardian/<c_id>', methods=['GET'])
def camper_info(c_id):
    cursor = db.get_db().cursor
    the_query = '''
    SELECT phoneNumber, email
        FROM Camper NATURAL JOIN Cabin NATURAL JOIN Staff
        WHERE Camper.camperID = c_id;

'''
    cursor.execute(the_query)
    the_data = cursor.fetchall()
    the_response = make_response(the_data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@guardians.route('/guardian', methods=['POST'])
def med_needs():
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    c_id = the_data['camperID']
    m_id = the_data['medID']
    
    # Constructing the query
    query = 'insert into MedNeeds (camperID, medID) values ("'
    query += c_id + '", "'
    query += m_id + ")"
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'
