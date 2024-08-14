########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db


camp_director = Blueprint('camp_director', __name__)

@camp_director.route('/camp_director/<staffID>', methods=['GET'])
def staff_cabins(staffID): 
    cursor = db.get_db().cursor()
    the_query = f'''
        SELECT ca.cabinName, ca.cabinID 
	    FROM Cabin ca 
	    WHERE ca.staffID = {staffID}; 

    '''
    cursor.execute(the_query)
    the_Data = cursor.fetchall()
    the_response = make_response(the_Data)  
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response 

@camp_director.route('/camp_director/G/<camperID>', methods=['GET'])
def guardian_info(camperID):
    cursor = db.get_db().cursor() 
    the_query = f'''
    SELECT g.guardianID, g.firstName, g.lastName, g.phone, g.email 
        FROM Guardian g JOIN Camper c ON g.guardianID = c.guardianID 
        WHERE c.camperID = {camperID};
    '''
    cursor.execute(the_query)
    the_Data = cursor.fetchall()
    the_response = make_response(the_Data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    
    return the_response 


@camp_director.route('/camp_director/unpaid', methods=['GET'])
def unpaid_guardians(): 
    cursor = db.get_db().cursor()
    the_query = '''SELECT g.firstName, g.lastName, g.phone FROM Guardian g WHERE g.paid = 0 ORDER BY g.lastName ASC;
    '''
    cursor.execute(the_query)
    the_Data = cursor.fetchall()
    the_response = make_response(the_Data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response

