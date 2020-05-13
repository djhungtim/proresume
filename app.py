from flask import Flask, request, redirect
from flask.templating import render_template
app = Flask(__name__)
# print(__name__)
import csv

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/com')
# def com():
#     return render_template('components.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        mseeage = data["message"]
        file = database.write(f'\n{email},{subject},{mseeage}')

def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        mseeage = data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,mseeage]) 

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thenk.html')
        except:
            return 'something wrong'
    else:
        return 'wrong'

# @app.route('/blog')
# def hello_world():
#     return 'Hello, Tim!!!!!'