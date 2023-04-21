from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView



from .forms import PersonForm

from django.shortcuts import render
from .forms import PersonForm
from django.http import JsonResponse
import json
from .models import Branch,Person



# Create your views here.

# class PersonCreateView(CreateView):
#     model=Person
#     form_class = PersonForm
#     success_url = reverse_lazy('/')


def index(request):
    return render(request,'index.html')

def newpage(request):
    return render(request,'newpage.html')




def person(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, "add.html", {"form": form})

#
# def profile(request):
#     form = PersonForm()
#     if request.method == "POST":
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     return render(request, "profilehome.html", {"form": form})

def branch(request):
    data = json.loads(request.body)
    branch = Branch.objects.filter(district__id=data['user_id'])
    print(branch)
    return JsonResponse(list(branch.values("id", "name")), safe=False)

#
# def profile(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         dob=request.POST.get('dob')
#         age=request.POST.get('age')
#         email=request.POST.get('email')
#         address=request.POST.get('address')
#         phone=request.POST.get('phone')
#         gender=request.POST.get('gender')
#
#         district=request.POST.get('district')
#         branch=request.POST.get('branch')
#         account=request.POST.get('account')
#         materials=request.POST.get('materials')
#         # state=State.objects.get(name=name)
#         # person=Person.objects.get(name=name,state=state)
#
#         person=Person(name=name,dob=dob,age=age,email=email,address=address,phone=phone,gender=gender,district=district,branch=branch,account=account,materials=materials)
#         person.save()
#
#         return redirect('/')
#         # return redirect('/profile')
#
#     return render(request,'profilehome.html')

# def getstate(request):
#     state = State.objects.all()
#     if request.method=='POST':
#         name=request.POST['name']
#         state=State(name=name)
#         state.save()
#
#     return render(request,'profilehome.html',{'state':state})
#
# def getdist(request,state):
#     district = District.objects.all()
#     return render(request,'profilehome.html',{'district':district})

# def getbranch(request,district):
#     branch = Branch.objects.filter(district=district)
#     return render(request,'profilehome.html',{'branch':branch})
#
#
#
# def add(request):
#     person=Person
#     if request.method == 'POST':
#         form = PersonForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             pass
#
#     return render(request,'add.html',{'form':form,'person':person})


# def get_branches(request):
#     state=State.objects.all('state')
#     district=District.objects.all('district')
#     if state =='Kerala':
#         district=['Palakkad','Kottayam','Thrissur','Kannur']
#         if district=='Palakkad':
#             branch=['Ottapalam','Lakkidi','Pathiripala']
#         elif district=='Kottayam':
#             branch=['Pala','Changanacheri']
#     elif state=='Tamilnanu':
#         district=['Coimpatore','Selam']
#         if district=='Selam':
#             branch=['Madhura','theni']
#         elif district=='Coimpatore':
#             branch=['Ukkadam','Madhukara']
#     return render(request,'')
#
#
