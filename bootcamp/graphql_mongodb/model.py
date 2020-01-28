from mongoengine import Document
from mongoengine.fields import ReferenceField,StringField,IntField,DictField

class Task(Document):
    meta = {"id":2,
    "Title":" ",
    "Description":" ",
    "Done":" "
    }
    task = DictField()
    # id = IntField()
    # title =StringField()
    # description =StringField()
    # done = StringField()

# class TITLE(Document):
#     meta = {"TASK":"title"}
#     name = StringField()

# class Description(Document):
#     meta = {"TASK":"description"}
#     name = StringField()

# class Done(Document):
#     meta = {"TASK":"done"}
#     name = StringField()