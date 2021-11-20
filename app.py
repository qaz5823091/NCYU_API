from flask import Flask, render_template, json, jsonify

app = Flask(__name__)
# app.config['DEBUG'] = True
app.config['JSON_AS_ASCII'] = False

with open('./department.json') as file:
    department = json.load(file)

with open('./classOfDepartment.json') as file:
    class_of_department = json.load(file)

with open('./classOfGeneral.json') as file:
    class_of_general = json.load(file)

@app.route('/')
def home():
    return '<h1>Welcome to NCYU API!</h1>'

@app.route('/dept')
def deptAll():
    return jsonify(department)

@app.route('/dept/<id>')
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

if __name__ == '__main__':
    app.run(host = 'localhost', debug = True)
