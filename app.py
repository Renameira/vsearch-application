import requests
from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def movieapp():
 
   return 'Web App with Python Flask!'
 
if __name__ == '__main__':
   app.run(debug=False, host='0.0.0.0')
