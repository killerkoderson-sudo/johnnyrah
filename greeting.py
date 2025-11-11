from flask import Flask
from flask import request
app = Flask(__name__)
@app.route("/")#URL leading to method
def hello(): # Name of the method
 return("Hello World!")
@app.route("/greetme")#different URL

@app.route("/greetjohn")#URL leading to method
def helloyo(): # Name of the method
 return("Hello john!")


@app.route("/greetme")#different URL
def helloall(): # different method name
 name = request.args.get('name')#retrieve GET parameters
 return("Hello {}!".format(name))#Python’s string.format
 
if __name__ == "__main__":
 app.run(host='0.0.0.0',port='8080') #Run the flask app at port 8080
