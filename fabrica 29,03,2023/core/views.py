from rest_framework import 
from app.serializers import ToDoSerializers
from app.models import Todo

class ToDoViewSet(viewsets.ModeViewSet):
    queryset = ToDo.obijects.all()
    Serializers_class = ToDoSerializers
