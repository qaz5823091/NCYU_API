from flask import Flask, render_template, json, jsonify
from flask_cors import CORS

app = Flask(__name__)
# app.config['DEBUG'] = True
app.config['JSON_AS_ASCII'] = False
cors = CORS(app, resources={r"/*": {"origins": "*"}})

with open('./department.json') as file:
    department = json.load(file)

with open('./1102_class_of_department.json') as file:
    class_of_department = json.load(file)

with open('./1102_class_of_general.json') as file:
    class_of_general = json.load(file)

@app.route('/')
def home():
    return '<h1>Welcome to NCYU API!</h1>'

@app.route('/departments')
def deptAll():
    return jsonify(department)

@app.route('/department/<id>')
def dept(id):
    is_exist = False
    if id != None:
        for item in department:
            if id == item['id']:
                is_exist = True
                result = item
                break

    if is_exist:
        return jsonify(item)
    else:
        return jsonify(department)

@app.route('/course/departments')
def classOfDepartment():
    return jsonify(class_of_department)

@app.route('/course/department/<id>')
def classOfDepartmentById(id):
    is_exist = False
    if id != None:
        for item in class_of_department:
            if id == str(item['id']):
                is_exist = True
                result = item
                break

    if is_exist:
        return jsonify(result)
    else:
        return 404

@app.route('/course/generals')
def classOfGeneral():
    return jsonify(class_of_general)

@app.route('/course/general/<id>')
def classOfGeneralById(id):
    is_exist = False
    if id != None:
        for item in class_of_general:
            if id == str(item['id']):
                is_exist = True
                result = item
                break

    if is_exist:
        return jsonify(result)
    else:
        return 404

if __name__ == '__main__':
    app.run(host = 'localhost', debug = True)
