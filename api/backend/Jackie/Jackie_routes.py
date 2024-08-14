########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

camp_counselor = Blueprint('camp_counselor', __name__)

@camp_counselor.route('/activity/<c_ID>', methods=['GET'])
def predict_value(c_ID):
    cursor = db.get_db().cursor()
    the_query = f'''
    SELECT s.firstName, s.lastName, s.phoneNumber, s.email
    FROM Staff s
    JOIN CampSession cs ON s.sessionID = cs.sessionID
    WHERE s.campID = {c_ID} 
    AND cs.startDate <= 7/10/2024 
    AND cs.endDate >= 8/5/2024;
    ;
    '''
    cursor.execute(the_query)
    the_data = cursor.fetchall()
    the_response = make_response(the_data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Get all customers from the DB
@customers.route('/customers', methods=['GET'])
def get_customers():
    current_app.logger.info('customer_routes.py: GET /customers')
    cursor = db.get_db().cursor()
    cursor.execute('select id, company, last_name,\
        first_name, job_title, business_phone from customers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@customers.route('/customers', methods=['PUT'])
def update_customer():
    current_app.logger.info('PUT /customers route')
    cust_info = request.json
    # current_app.logger.info(cust_info)
    cust_id = cust_info['id']
    first = cust_info['first_name']
    last = cust_info['last_name']
    company = cust_info['company']

    query = 'UPDATE customers SET first_name = %s, last_name = %s, company = %s where id = %s'
    data = (first, last, company, cust_id)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'customer updated!'

# Get customer detail for customer with particular userID
@customers.route('/customers/<userID>', methods=['GET'])
def get_customer(userID):
    current_app.logger.info('GET /customers/<userID> route')
    cursor = db.get_db().cursor()
    cursor.execute('select id, first_name, last_name from customers where id = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response