from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

#Task 3 and 5
@app.route('/students')
def get_students():
    result = []
    pref = request.args.get('pref') # get the parameter from url
    if pref:
       for student in data: # iterate dataset
         if student['pref'] == pref: # select only the students with a given meal preference
           result.append(student) # add match student to the result
       return jsonify(result) # return filtered set if parameter is supplied
    return jsonify(data) # return entire dataset if no parameter supplied

# Task 4
@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)

#Lab task
@app.route('/hello/<string:firstname>/<string:lastname>')
def hello(firstname, lastname):
  return "Hello " + firstname + " " + lastname

#Exercise 1
@app.route('/stats')
def get_stats():
    chicken = 0
    fish = 0
    vegetarian = 0
    csm = 0
    css = 0
    itm = 0
    its = 0
    
    for student in data:
        if student['pref'] == "Chicken":
            chicken += 1
        elif student['pref'] == "Fish":
            fish += 1
        else:
            vegetarian += 1

        if student['programme'] == "Computer Science (Major)":
            csm += 1
        elif student['programme'] == "Computer Science (Special)":
            css += 1
        elif student['programme'] == "Information Technology (Major)":
            itm += 1
        else:
            #student['programme'] == "Information Technology (Special)":
            its += 1

    output = {"Chicken": chicken, 
              "Fish": fish, 
              "Vegetarian": vegetarian, 
              "Computer Science (Major)": csm, 
              "Computer Science (Special)": css, 
              "Information Technology (Major)": itm, 
              "Information Technology (Special)": its}
    
    return jsonify(output)

#Exercise 2
@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return "The added values are: " + str(a + b)

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    return "The subtract value is: " + str(a - b)

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return "The product value is: " + str(a * b)

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    return "The result value is: " + str(a / b)

app.run(host='0.0.0.0', port=8080, debug=True)
