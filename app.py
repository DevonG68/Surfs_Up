#add flask dependencies
from flask import Flask

# #create new flask app instance
app = Flask(__name__)

# #create flask route with root as the highest level of hiearchy and function
@app.route('/')
def hello_world():
    return 'Hello world'

#main is the main app
if __name__ == '__main__':
    #refresh app 
    app.run(debug=True)