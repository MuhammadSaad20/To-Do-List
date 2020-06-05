from django.shortcuts import render,HttpResponse,redirect
from To_do_list_app.models import List
from To_do_list_app.forms import ListForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        form=ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            # -> remember all_item it creates object
            messages.success(request,('Item has been added to List!'))
            return render(request,'index.html',{'all_items':all_items})
        else:
            all_items = List.objects.all
            return render(request, 'index.html', {'all_items': all_items})

    return  render(request,'index.html')

def delete(request,list_id):

    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Items has been Deleted!'))
    return redirect('./')
    #return redirect('index.html')


def cross_off(request,list_id):

    item = List.objects.get(pk=list_id)
    item.completed=True
    item.save()
    messages.success(request, ('Items has been Crossed!'))
    return redirect('./')


def un_cross(request,list_id):

    item = List.objects.get(pk=list_id)
    item.completed=False
    item.save()
    messages.success(request, ('Items has been Uncrossed!'))
    return redirect('./')