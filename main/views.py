from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item,Daily
from django.urls import reverse
import datetime
from datetime import datetime
from django.contrib.auth.decorators import login_required




# Create your views here.


def index(response, id):
    ls =ToDoList.objects.get(id=id)
    today=datetime.now().date()
    if ls in response.user.todolist.all():
    
    
        if ls in response.user.todolist.all():
            if response.method == "POST":
                if response.POST.get("saver"):
                    for item in ls.item_set.all():
                        if response.POST.get("c" + str(item.id)) == "clicked" and item.complete==False:
                            item.complete = True
                            item.due_date=today
                            
                        elif response.POST.get("c" + str(item.id)) != "clicked" and item.complete==True:
                            item.complete = False
                            item.due_date=None
                            

                        item.save()

                elif response.POST.get("newItem"):
                    txt = response.POST.get("new")

                    if len(txt) > 2:
                            ls.item_set.create(text=txt, complete=False)
                    else:
                        print("invalid")
                elif response.POST.get("delete"):
                    item_id=response.POST.get("delete")
                    ls.item_set.get(id=int(item_id)).delete()
      
        return render(response, "main/list.html", {"ls": ls})
    return render(response, "main/home.html", {})


def daily(response):
    
    # num=response.user.daily.count()
    # print(num)
    if response.method =="POST":
        dl = response.user.daily.all()
    
        if response.POST.get("delete"):
            td_id=response.POST.get("delete")
            Daily(id=int(td_id)).delete()
        elif response.POST.get("create"):
            n = response.POST["name"]
            if len(n)>2:
                d = Daily(name=n)
                
                d.due_date=response.POST["time"]
                print(d.due_date)
                
                d.complete=False    
                d.save()
                response.user.daily.add(d)
                
            else:
                print("invalid")

        elif response.POST.get("save"):
              for item in dl:
                  
                  if response.POST.get("d" + str(item.id)) == "clicked":
                     item.complete = True
                     
                    
                  else:
                      item.complete = False
                  item.save()
                      
        elif response.POST.get("reset"):
            for item in dl:
                item.complete=False
                item.save()

    
            
            
                      
            
    return render(response, "main/daily.html", {})


def home(response):
    return render(response, "main/home.html", {})
    
     
def lists(response):
    
    if response.method =="POST":
        if response.POST.get("delete"):
            td_id=response.POST.get("delete")
            ToDoList(id=int(td_id)).delete()
            
        elif response.POST.get("create"):
            n = response.POST["name"]
            if len(n)>2:
                t = ToDoList(name=n)
                t.save()
                response.user.todolist.add(t)
            else:
                print("invalid")
            
    return render(response, "main/lists.html", {})
    #return HttpResponseRedirect("/%i" % td_id)


