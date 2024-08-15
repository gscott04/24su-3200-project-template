########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

# Creating a Blueprint for camp_director routes
camp_director = Blueprint('camp_director', __name__)

# 3.1: Return the cabin name for a staffID
@camp_director.route('/camp_director/<staffID>', methods=['GET'])
def staff_cabins(staffID):
    # Get a database cursor to execute the query 
    cursor = db.get_db().cursor()
    the_query = f'''
        SELECT ca.cabinName, ca.cabinID 
	    FROM Cabin ca 
	    WHERE ca.staffID = {staffID}; 
    '''
    # Execute the SQL query
    cursor.execute(the_query)
    # Fetching all results from query execution
    the_Data = cursor.fetchall()
    # Creating a response object with the data
    the_response = make_response(the_Data)  
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response 

# 3.2: Return the guardian information for a camperID
@camp_director.route('/camp_director/G/<camperID>', methods=['GET'])
def guardian_info(camperID):
    # Get a database cursor to execute the query
    cursor = db.get_db().cursor() 
    the_query = f'''
    SELECT g.guardianID, g.firstName, g.lastName, g.phone, g.email 
        FROM Guardian g JOIN Camper c ON g.guardianID = c.guardianID 
        WHERE c.camperID = {camperID};
    '''
    # Execute the SQL query
    cursor.execute(the_query)
    # Fetching all results from query execution
    the_Data = cursor.fetchall()
    # Creating a response object with the data
    the_response = make_response(the_Data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    
    return the_response 

# 3.3: Get all the unpaid guardians 
@camp_director.route('/camp_director/unpaid', methods=['GET'])
def unpaid_guardians(): 
    # Get a database cursor 
    cursor = db.get_db().cursor()
    the_query = '''SELECT g.firstName, g.lastName, g.phone FROM Guardian g WHERE g.paid = 0 ORDER BY g.lastName ASC;
    '''
    # Execute the SQL query
    cursor.execute(the_query)
    # Fetching all results from query execution
    the_Data = cursor.fetchall()
    # Creating a response object with the data
    the_response = make_response(the_Data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response