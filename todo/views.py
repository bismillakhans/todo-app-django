from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def index(request):
    items=TodoItem.objects.all()
    tods=[]
    for item in items:
        tods.append({"id":item.id,"title":item.title,"completed":item.completed})
    return JsonResponse(tods,safe=False)


def create(request):
    title=request.POST.get("title")
    item=TodoItem(title=title)
    item.save()
    return JsonResponse({"message":"Item created","id":item.id})