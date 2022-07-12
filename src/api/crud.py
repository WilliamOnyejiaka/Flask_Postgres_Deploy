from flask import Blueprint,request,jsonify
from src.modules.Company import Company

crud = Blueprint('crud',__name__,url_prefix='/api/crud')


@crud.post('/create')
def create_table():
    company = Company()
    company.create_table()
    company.close()
    return jsonify({'error':False,'message':"created"}),200

@crud.delete("/drop")
def drop():
    company = Company()
    company.drop_table()
    company.close()
    return jsonify({'error':False,'message':"dropped"}),200

@crud.post('/insert')
def insert_value():
    name = request.get_json().get('name',"None")
    dept_id = request.get_json().get('dept_id', "None")
    try:
        salary = int(request.get_json().get('salary', 5000))
    except Exception as err:
        return jsonify({'error':False,'message':"salary int conversion"}),400

    company = Company()
    company.insert_one((name,salary,dept_id))
    company.close()
    return jsonify({'error':False,'message':"inserted"}),200

@crud.get("/get_all")
def get_all():
    company = Company()
    data = company.find()
    company.close()
    return jsonify({'error':False,'data':data}),200

@crud.get("/get_one/<id>")
def get_one(id):
    company = Company()
    data = company.find_one(id)
    company.close()
    return jsonify({'error':False,'data':data}),200
