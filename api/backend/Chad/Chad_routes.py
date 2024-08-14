########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db


camp_director = Blueprint('camp_director', __name__)

@camp_director.route('/camp_director', methods=['GET'])
def understaffed_cabins(): 
    cursor = db.get_db().cursor()
    the_query = '''SELECT ca.cabinName, ca.cabinID 
                    FROM Cabin ca 
                        JOIN Camper cam on ca.cabinID = cam.cabinID 
                    WHERE ca.StaffID IS NULL 
                    GROUP BY ca.cabinName, ca.cabinID;
    '''
    cursor.execute(the_query)
    the_Data = cursor.fetchall()
    the_response = make_response(the_Data)  
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response 

@camp_director.route('/camp_director<camperID>', methods=['GET'])
def guardian_info(camperID):
    cursor = db.get_db().cursor() 
    the_query = '''
    SELECT g.firstName, g.lastName, g.phone, g.email FROM Guardian g JOIN Camper c ON g.guardianID = c.guardianID WHERE c.camperID = camperID;
    '''.format(camperID)
    cursor.execute(the_query)
    the_Data = cursor.fetchall()
    the_response = make_response(the_Data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    
    return the_response 


@camp_director.route('/camp_director', methods=['GET'])
def unpaid_guardians(): 
    cursor = db.get_db().cursor()
    the_query = '''SELECT g.firstName, g.lastName, g.phone FROM Guardian g WHERE g.paid = FALSE ORDER BY g.lastName ASC;
    '''
    cursor.execute(the_query)
    the_Data = cursor.fetchall()
    the_response = make_response(the_Data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response
