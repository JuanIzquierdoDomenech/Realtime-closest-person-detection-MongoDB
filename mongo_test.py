from mongoengine import connect
from mongoengine import Document, ListField, StringField, URLField

# Creating a model that resembles the MongoDB document structure (Same name as COLLECTION name, except start upercase)
class Tutorial(Document):
	title = StringField(required=True, max_length=70)
	author = StringField(required=True, max_length=20)
	contributors = ListField(StringField(max_length=20))
	url = URLField(required=True)

connect(db="rptutorial", host="localhost", port=27017)

# e.g. Saving a document into the collection
tutorial1 = Tutorial(
	title="Beautiful Soup: Build a Web Scraper With Python",
	author="Martin",
	contributors=["Aldren", "Geir Arne", "Jaya", "Joanna", "Mike"],
	url="https://realpython.com/beautiful-soup-web-scraper-python/"
)

tutorial1.save()

# e.g. Iterating all the documents in a collection
for doc in Tutorial.objects:
	print(doc.title)
	print(doc.contributors)

# e.g. Querying
for doc in Tutorial.objects(author="Jon"):
	print(doc.title)

# e.g. Updating a single document
Tutorial.objects(title="Beautiful Soup: Build a Web Scraper With Python").update_one(author="Pedro")