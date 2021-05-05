from mongoengine import Document, IntField, StringField

# Application layer
class PeopleData:
	def __init__(self, startX, startY, endX, endY, confidence, color):
		self.startX = startX
		self.startY = startY
		self.endX = endX
		self.endY = endY
		self.confidence = confidence
		self.color = color

	def __str__(self):
		return "Data: " + str(self.getHeight())

	def getHeight(self):
		return self.endY - self.startY


# Mongo DB 'layer', name matches collection name... so Data is its name
class Data(Document):
	description=StringField(required=True, max_length=50)
	value=IntField(required=True)