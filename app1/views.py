from django.shortcuts import render
from .models import Todo
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TodoSerializer

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-id")
    return render(request, 'main/index.html', {
        "todo_items": todo_items
    })


def add_todo(request):
    print(request.POST['options'])
    if request.POST['options'] =='Open':
        Todo.objects.create(title=request.POST['title'], desc=request.POST['desc'], added_date=request.POST['date'],
                            comment=request.POST['content'])
    elif request.POST['options']== 'Closed':
        Todo.objects.create(title=request.POST['title'], desc=request.POST['desc'], added_date=request.POST['date'],
                            comment="No Comments")

    return HttpResponseRedirect("/")

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")

#creating json file
class TodoList(APIView):

    def get(self,request):
        todo1 = Todo.objects.all()
        serializer = TodoSerializer(todo1,many=True)
        return Response(serializer.data)
    def post(self):
        pass