from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import TodoItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(["GET", "POST"])
def index(request):
    if request.method=="POST":
        title=request.POST.get("title")
        item=TodoItem(title=title)
        item.save()
        return Response({"id":item.id,"title":item.title,"completed":item.completed})
    items=TodoItem.objects.all()
    tods=[]
    for item in items:
        tods.append({"id":item.id,"title":item.title,"completed":item.completed})
    return Response(tods,safe=False)


@api_view([ "PUT", "DELETE"])
def update(request,id):
    item=TodoItem.objects.get(id=id)
    if request.method=="PUT":
        title=request.POST.get("title")
        item.title=title
        item.save()
        return Response({"id":item.id,"message":"updated"},status=200)
    if request.method=="DELETE":
        item.delete()
        return Response({"message":"deleted"},status=200)

