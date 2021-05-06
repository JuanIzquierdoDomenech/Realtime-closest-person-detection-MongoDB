from flask import Flask
from mongoengine import connect
from model import Data as QueriedData
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/closest_person')
def get_closest_person_data():
	value = -1
	for doc in QueriedData.objects(description="User proximity value"):
		value = doc.value
	return str(value)

if __name__ == "__main__":
	connect(db="ssexpo", host="localhost", port=27017) 	# Connect to MongoDB 
	subprocess.Popen([									# Launch video recognition
		"python", 
		"detect_and_write_to_mongo.py", 
		"--prototxt", "MobileNetSSD_deploy.prototxt.txt", 
		"--model", "MobileNetSSD_deploy.caffemodel"])
	app.run() 											# Launch flask server



#python detect_and_write_to_mongo.py \
#        --prototxt MobileNetSSD_deploy.prototxt.txt \
#        --model MobileNetSSD_deploy.caffemodel