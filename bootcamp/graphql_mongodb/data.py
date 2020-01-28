from mongoengine import connect
from model import Task
from flask import jsonify,request

connect(host="mongodb+srv://mubi:1234@cluster001-avto2.mongodb.net/test?retryWrites=true&w=majority")

def initData():
    # id = Id(name="32452343242")
    # title = TITLE(name= "aman")
    # description = Description(name="abcdefghijklmnopqrstuvwxyz")
    # done = Done(name="true")
    # data={"id":id,"title":title,"description":description,"done":done}.save()
    inp={"id":32443,"Title":"aasjafadkfj","Description":"ajsbdsabfhjzbfjab","Done":True}
    data = Task(task=inp)
    data.save()





