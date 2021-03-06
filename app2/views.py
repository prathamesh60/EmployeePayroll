from django.shortcuts import render,redirect
from app2.forms import *
from app2.models import *

# def religion(request):
#     if request.method == "POST":
#       form1= ReligionForm(request.POST)
#       if form1.is_valid():
#           try:
#               form1.save()
#               return redirect("/religion")
#           except:
#               pass
#     else:
#         form1= ReligionForm()
#         religion1 = Religion.objects.all()
#         return render(request,"religion/register.html", {"form1":form1, "religion1": religion1})



# def show_religion(request):
#     religion1 = Religion.objects.all()

#     return render(request, "religion/index.html", {"religion1": religion1} )
# def edit(request,id):
#     religion2 = Religion.objects.get(RELIGION_NO=id)
#     return render(request, "religion/edit.html", { 'religion2':religion2})
# def modify_religion(request,id):
#     religion2 =Religion.objects.get(RELIGION_NO=id)
#     form1 = ReligionForm(request.POST, instance = religion2)
#     # religion2.RELIGION_NO = form1.RELIGION_NO
#     # religion2.RELIGION_NAME = form1.RELIGION_NAME
#     # form1.RELIGION_NO = religion2.A.value#religion2.RELIGION_NO
#     # form1.RELIGION_NAME = religion2.B.value#religion2.RELIGION_NAME
#     if form1.is_valid():
#         form1.save()
#         return redirect("/religion")
#     return render(request, "religion/edit.html", { 'form1':religion2})
# def delete_religion(request,id):
#     religion3 =Religion.objects.get(id=id)
#     religion3.delete()
#     return redirect("/show_religion")
# Create your views here.

# class ClassName(object):
#     # """docstring for ."""
#     model=

from django.views.generic.edit import UpdateView,CreateView
from django.views.generic.list import ListView
from django.shortcuts import render,redirect
from app2.forms import *
from app2.models import *

#start for religion model
def religion(request):
    if request.method == "POST":
      form1= ReligionForm(request.POST)
      if form1.is_valid():
          try:
              form1.save()
              return redirect("/religion")
          except:
              pass
    else:
        form1= ReligionForm()
        religion1 = Religion.objects.all()
        return render(request,"religion/register.html", {"form1":form1, "religion1": religion1})



def show_religion(request):
    religion1 = Religion.objects.all()

    return render(request, "religion/index.html", {"religion1": religion1} )

class ReligionUpdateView(UpdateView):
    # specify the model you want to use
    model = Religion

    # specify the fields
    fields = [
        "RELIGION_NO",
        "RELIGION_NAME"
    ]

    success_url ="religion"

def delete_religion(request,id):
    religion3 =Religion.objects.get(id=id)
    religion3.delete()
    return redirect("/religion")

#End for religion model

#caste

class CasteCreateView(CreateView):
    # specify the model you want to use
    model = Caste
    # specify the fields
    fields = "__all__"
    # can specify success url
    # url to redirect after sucessfully
    # updating details
    success_url ="show_caste"

class CasteUpdateView(UpdateView):
    # specify the model you want to use
    model = Caste

    # specify the fields
    fields = [
        "CASTE_NO",
        "CASTE_NAME"
    ]

    success_url ="caste"

def delete_caste(request,id):
    caste3 =Caste.objects.get(id=id)
    caste3.delete()
    return redirect("/caste")
#End of caste

def suplhead(request):
    if request.method == "POST":
      form1= SuplHeadForm(request.POST)
      if form1.is_valid():
          try:
              form1.save()
              return redirect("/suplhead")
          except:
              pass
    else:
        form1=SuplHeadForm()
        suplhead1 = SuplHead.objects.all()
        return render(request,"caste/register.html", {"form1":form1, "caste1": suplhead1})

class SuplHeadUpdateView(UpdateView):
    # specify the model you want to use
    model = SuplHead

    # specify the fields
    fields = [
        "SUPLNO",
        " SUPLHEAD_NAME"
    ]

    success_url ="suplhead"

def delete_suplhead(request,id):
    suplhead3 =SuplHead.objects.get(id=id)
    suplhead3.delete()
    return redirect("/suplhead")




# title

#start for title model
def title(request):
    if request.method == "POST":
      form1= TitleForm(request.POST)
      if form1.is_valid():
          try:
              form1.save()
              return redirect("/title")
          except:
              pass
    else:
        form1= TitleForm()
        title1 = Title.objects.all()
        return render(request,"title/register.html", {"form1":form1, "title1": title1})


#show title
def show_title(request):
    title1 = Title.objects.all()

    return render(request, "title/index.html", {"title1": title1} )

#update title
class TitleUpdateView(UpdateView):
    # specify the model you want to use
    model = Title

    # specify the fields
    fields = [
        "TITLE_NO",
        "TITLE_NAME"
    ]

    success_url ="title"

#delete title
def delete_title(request,id):
    title3 =Title.objects.get(id=id)
    title3.delete()
    return redirect("/title")


#category

#start for title model
def category(request):
    if request.method == "POST":
      form1= CategoryForm(request.POST)
      if form1.is_valid():
          try:
              form1.save()
              return redirect("/category")
          except:
              pass
    else:
        form1= CategoryForm()
        category1 = Category.objects.all()
        return render(request,"category/register.html", {"form1":form1, "category1": category1})


#show category
def show_category(request):
    category1 = Category.objects.all()

    return render(request, "category/index.html", {"category1": category1} )

#update category
class CategoryUpdateView(UpdateView):
    # specify the model you want to use
    model = Title

    # specify the fields
    fields = [
        "CATEGORY_NO",
        "CATEGORY_NAME"
    ]

    success_url ="category"

#delete category
def delete_category(request,id):
    category3 =Category.objects.get(id=id)
    category3.delete()
    return redirect("/category")

class MainDept_create(CreateView):

    # specify the model for create view
    model = MainDept

    # specify the fields to be displayed

    fields = ['DEPT_NO', 'DEPT_NAME', 'SDEPT']

    success_url ="MainDeptShowView"

class MainDeptShowView(ListView):
    # specify the model you want to use
    model = MainDept

    # specify the fields
    # fields = ['DEPT_NO', 'DEPT_NAME', 'SDEPT']

    # success_url ="MainDept"

class MainDesignation_create(CreateView):

    # specify the model for create view
    model = MainDesignation

    # specify the fields to be displayed

    fields = "__all__"

    success_url ="MainDesignationShowView"

class MainDesignationShowView(ListView):
    # specify the model you want to use
    model = MainDesignation

    # specify the fields
    # fields = ['DEPT_NO', 'DEPT_NAME', 'SDEPT']

    # success_url ="MainDept"

class Staff_create(CreateView):

    # specify the model for create view
    model = Staff

    # specify the fields to be displayed

    fields = "__all__"

    success_url ="StaffShowView"

class StaffShowView(ListView):
    # specify the model you want to use
    model = Staff

    # specify the fields
    # fields = ['DEPT_NO', 'DEPT_NAME', 'SDEPT']

    # success_url ="MainDept"

class Scale_create(CreateView):

    # specify the model for create view
    model = Scale

    # specify the fields to be displayed

    fields = "__all__"

    success_url ="ScaleShowView"

class ScaleShowView(ListView):
    # specify the model you want to use
    model = Scale

    # specify the fields
    # fields = ['DEPT_NO', 'DEPT_NAME', 'SDEPT']

    # success_url ="MainDept"

class TypeTranCreateView(CreateView):
    # specify the model you want to use
    model = TypeTran
    # specify the fields
    fields ="__all__"

    # can specify success url
    # url to redirect after sucessfully
    # updating details
    success_url ="show_typetran"

class TypeTranListView(ListView):

    # specify the model for list view
    model = TypeTran

class AppointmentCreateView(CreateView):
    # specify the model you want to use
    model = Appointment
    # specify the fields
    fields = "__all__"
    # can specify success url
    # url to redirect after sucessfully
    # updating details
    success_url ="show_appointment"

class AppointmentListView(ListView):

    # specify the model for list view
    model = Appointment

class UnderCollegeCreateView(CreateView):
    # specify the model you want to use
    model = UnderCollege
    # specify the fields
    fields = "__all__"
    # can specify success url
    # url to redirect after sucessfully
    # updating details
    success_url ="show_undercollege"

class UnderCollegeListView(ListView):

    # specify the model for list view
    model = UnderCollege

class BankCreateView(CreateView):
    # specify the model you want to use
    model = Bank
    # specify the fields
    fields = "__all__"
    # can specify success url
    # url to redirect after sucessfully
    # updating details
    success_url ="show_bank"

class BankListView(ListView):

    # specify the model for list view
    model = Bank

class CityCreateView(CreateView):
    # specify the model you want to use
    model = City
    # specify the fields
    fields = "__all__"
    # can specify success url
    # url to redirect after sucessfully
    # updating details
    success_url ="show_city"

class CityListView(ListView):

    # specify the model for list view
    model = City

class SubDeptCreateView(CreateView):
    # specify the model you want to use
    model = SubDept
    # specify the fields
    fields = "__all__"
    # can specify success url
    # url to redirect after sucessfully
    # updating details
    success_url ="show_subdept"

class SubDeptListView(ListView):

    # specify the model for list view
    model = SubDept

class InstallCreateView(CreateView):
    # specify the model you want to use
    model = InstallmentType
    # specify the fields
    fields = "__all__"
    # can specify success url
    # url to redirect after sucessfully
    # updating details
    success_url ="show_install"

class InstallListView(ListView):

    # specify the model for list view
    model = InstallmentType

class SUBDESIGCreateView(CreateView):
    # specify the model you want to use
    model = SubDesignation
    # specify the fields
    fields = "__all__"
    # can specify success url
    # url to redirect after sucessfully
    # updating details
    success_url ="show_subdesig"

class SUBDESIGListView(ListView):

    # specify the model for list view
    model = SubDesignation

class DesignatureCreateView(CreateView):
    # specify the model you want to use
    model = Designature
    # specify the fields
    fields = "__all__"
    # can specify success url
    # url to redirect after sucessfully
    # updating details
    success_url ="show_designature"

class DesignatureListView(ListView):

    # specify the model for list view
    model = Designature
    
    
 


#crud operations

#create profile (http://127.0.0.1:8000/crud_create)
def crud_create(request):
    if request.method == 'POST':
        #validate and save the created profile
        form = EmployeeInformationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("111111111111111111111111111")
            #valid form ,therefore save it in database
            #WRITE A FUNCTION TO GENERATE ID AND SEQUENCE NUMBER
            #form.instance.ID_NUMBER='11111'
            form.save()
            return HttpResponse("PROFILE CREATED")

        else:
            #invalid form(user is redirected to create_profile.html form and displayed the relevant erors) 
            title=Title.objects.all()
            designation_nature=Designation_Nature.objects.all()
            under=Under.objects.all()
            designation=MainDesignation.objects.all()
            department=MainDept.objects.all()
            staff_type=StaffType.objects.all()
            appointment=Appointment.objects.all()
            vacational=Vacational.objects.all()
            bank_name=Bank_Name.objects.all()
            level=Level.objects.all()
            rule=Rule.objects.all()
            gender=Gender.objects.all()
            return render(request,'info/create_profile.html',{'title':title ,'designation_nature':designation_nature ,'under':under , 'designation':designation ,
            'department':department , 'staff_type':staff_type ,'appointment':appointment ,'vacational':vacational ,'bank_name':bank_name ,
            'level':level ,'rule':rule ,'gender':gender ,'messages':form.errors})

    else:
        #enter details of the profile to create
        title=Title.objects.all()
        designation_nature=Designation_Nature.objects.all()
        under=Under.objects.all()
        designation=MainDesignation.objects.all()
        department=MainDept.objects.all()
        staff_type=StaffType.objects.all()
        appointment=Appointment.objects.all()
        vacational=Vacational.objects.all()
        bank_name=Bank_Name.objects.all()
        level=Level.objects.all()
        rule=Rule.objects.all()
        gender=Gender.objects.all()
        messages=''
        return render(request,'info/create_profile.html',{'title':title ,'designation_nature':designation_nature ,'under':under , 'designation':designation ,
        'department':department , 'staff_type':staff_type ,'appointment':appointment ,'vacational':vacational ,'bank_name':bank_name ,
        'level':level ,'rule':rule ,'gender':gender,'messages':messages })


#read profile (http://127.0.0.1:8000/crud_read)
def crud_read(request):
    if request.method=='POST':
        #verify the id of profile and display the relevant information of the profile
        id=request.POST['ID_NUMBER']
        try:
            obj= EmployeeInformation.objects.get(ID_NUMBER=id)
            if obj.SEQUENCE_NUMBER!=request.POST['SEQUENCE_NUMBER']:
                return HttpResponse("object not found")
                
        except EmployeeInformation.DoesNotExist:
            return HttpResponse("Object does not exist")
       
        return render(request, 'info/read_profile.html', { 'obj': obj })


    else:
        #acccept id of profile to read
        return render(request,'info/ask_id_for_read.html')


#update profile (http://127.0.0.1:8000/crud_update)
def ask_id_for_update(request):
    print("11111111111111111111111111111")
    if request.method=='POST':
        print("222222222222222222222222222")
        #verify the id of profile and display the relevant information of the profile
        id=request.POST['ID_NUMBER']
        try:
            obj= EmployeeInformation.objects.get(ID_NUMBER=id)
            if obj.SEQUENCE_NUMBER!=request.POST['SEQUENCE_NUMBER']:
                return HttpResponse("object not found")
                
        except EmployeeInformation.DoesNotExist:
            return HttpResponse("Object does not exist")
        
        #id is correct , therefore display details of profile as default and editable
        title=Title.objects.all()
        designation_nature=Designation_Nature.objects.all()
        under=Under.objects.all()
        designation=MainDesignation.objects.all()
        department=MainDept.objects.all()
        staff_type=StaffType.objects.all()
        appointment=Appointment.objects.all()
        vacational=Vacational.objects.all()
        bank_name=Bank_Name.objects.all()
        level=Level.objects.all()
        rule=Rule.objects.all()
        gender=Gender.objects.all()
        messages=''
        return render(request, 'info/update_profile.html', { 'obj': obj ,'title':title ,'designation_nature':designation_nature ,'under':under , 'designation':designation ,
        'department':department , 'staff_type':staff_type ,'appointment':appointment ,'vacational':vacational ,'bank_name':bank_name ,
        'level':level ,'rule':rule ,'gender':gender,'messages':messages})

    else:
        print("333333333333333333333333333333")
        #acccept id of profile to update
        return render(request,'info/ask_id_for_update.html')


#update profile(called from form )
#CANNOT ACCESS DIRECTLY FROM URL   
def crud_update(request):
    
    if request.method == 'POST':
        
        #check if updated profile is valid and update accordingly
        id=request.POST['ID_NUMBER']
        try:
            
            obj= EmployeeInformation.objects.filter(ID_NUMBER=id).get()
            
            if obj.SEQUENCE_NUMBER!=request.POST['SEQUENCE_NUMBER']:
                 return HttpResponse("object not found")

            
            form = EmployeeInformationForm(request.POST, instance=obj)

            if form.is_valid():   
                form.save()
                return HttpResponse("data saved")

            else:
                print(form.errors)
                return HttpResponse("not updated")
                
        except EmployeeInformation.DoesNotExist:
            return HttpResponse("Object does not exist")
