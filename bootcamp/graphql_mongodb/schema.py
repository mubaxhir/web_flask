import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField,MongoengineObjectType
from model import Task as task_model
# from model import Id as Idmodel
# from model import TITLE as Model_title
# from model import Description as Modle_description
# from model import Done as Model_done

class Task(MongoengineObjectType):
    class Meta:
        model = task_model
        interfaces = (Node,)

# class Id(MongoengineObjectType):
#     class Meta:
#         model = Idmodel
#         interfaces = (Node,)

# class TITLE(MongoengineObjectType):
#     class Meta:
#         model = Model_title
#         interfaces = (Node,)

# class Description(MongoengineObjectType):
#     class Meta:
#         model = Modle_description
#         interfaces = (Node,)

# class Done(MongoengineObjectType):
#     class Meta:
#         model = Model_done
#         interfaces = (Node,)

class Query(graphene.ObjectType):
    node = Node.Field()
    allTask= MongoengineConnectionField(Task)
    # allId = MongoengineConnectionField(Id)
    # allTitle = MongoengineConnectionField(TITLE)
    # allDescription = MongoengineConnectionField(Description)
    # allDone = MongoengineConnectionField(Done)

schema = graphene.Schema(query=Query,types=[Task])
