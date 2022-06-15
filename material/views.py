from dataclasses import field
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from . import forms,models
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    return render (request,"material/home.html",{})

def program_specification(request):
    list1 = []
    level_list = ['one', 'two', 'three', 'four']
    list2 = []
    dict2 = {}
    for y in level_list: 
        course = models.Course.objects.filter(level=y)
        list2.clear()
        list1.clear()
        
        for i in course:
            for j in i.subjects.all():
                list1.append(j)
                
                list2 = [str(k) for k in list1]
                
        list3 = [x for x in list2 if list2.count(x) >=2]
        list3 = set(list3)
        list3 = list(list3)
        dict1 = {y:list3}
        dict2[y] = list3
    branche = models.Branch.objects.all()
    apdf = models.Academic_Program_Description_Forms.objects.all()
    context = {
        'branche':branche,
        'stages':dict2,
        'apdf':apdf,
    }
    
    return render (request,'material/program_specification.html',context)
    


def loginUser(request):
    return render(request, 'login_page.html')

def doLogin(request):
    
    username = request.GET.get('username')
    password = request.GET.get('password')
    # user_type = request.GET.get('user_type')
    
    #print(request.user)
    
    if not (username and password):
        messages.error(request, "Please provide all the details!!")
        return render(request, 'material/signin.html')

    user = User.objects.filter(username=username, password=password).first()
    if not user:
        messages.error(request, 'Invalid Login Credentials!!')
        return render(request, 'material/signin.html')

    login(request, user)

    if user:
        if  request.user.is_superuser:
            return redirect('basedashboard')
            
        return redirect('profile')

    return render(request, 'material/home.html')

    
def registration(request):
    return render(request, 'registration.html')
    

def doRegistration(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    username = request.GET.get('username')
    password = request.GET.get('password')
    confirm_password = request.GET.get('confirmPassword')

   
    if not (username and password and confirm_password):
        messages.error(request, 'Please provide all the details!!')
        return render(request, 'material/signup.html')
    
    if password != confirm_password:
        messages.error(request, 'Both passwords should match!!')
        return render(request, 'material/signup.html')

    is_user_exists = User.objects.filter(username=username).exists()

    if is_user_exists:
        messages.error(request, 'User with this email id already exists. Please proceed to login!!')
        return render(request, 'material/signup.html')

    #user_type = get_user_type_from_email(email_id)



    if User.objects.filter(username=username).exists():
        messages.error(request, 'User with this username already exists. Please use different username')
        return render(request, 'material/signup.html')

    user = User()
    user.username = username
    user.password = password
    user.first_name = first_name
    user.last_name = last_name
    user.save()
        
    return  redirect('signin')

    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')



def basedashboard(request) :

    branche = models.Branch.objects.all()
    context = {
        'branche':branche,
    }
    return render (request,'material/basedashboard.html',context)

def get_branche(request,branche_id) :
    
    branche = models.Branch.objects.get(id = branche_id)
    context = {
        'branche':branche,
    }
    return render (request,'material/branche_details.html',context)


def get_level(request,id,level):
    branch = models.Branch.objects.get(id = id)

    course = models.Course.objects.filter(branch =branch,level=level )
    return render(request, 'material/get_level.html', {'course':course,'branche':branch})


def questions_bank(request) :
    
    questions = models.Questions_Bank.objects.all()
    branches = models.Branch.objects.all()
    if request.method == "GET":
        questions = models.Questions_Bank.objects.filter(level = request.GET.get("level"),branch = models.Branch.objects.filter(id=request.GET.get("branch")).first() )
        
        
    if len(questions)<=0:
        questions = models.Questions_Bank.objects.all()
    
    if request.GET.get("branch") and request.GET.get("level") :
        
        title =  models.Branch.objects.filter(id=request.GET.get("branch")).first().name +" level "+ request.GET.get("level")
    else :
        title = "questions for all branches"
        
    context = {
        'questions':questions,
        'branches':branches,
        'title':title
    }
    return render (request,'material/questions_bank.html',context)



def get_branche_q(request,id) :
    
    branch = models.Branch.objects.get(id = id)
    questions = models.Questions_Bank.objects.filter(branch =branch )
    
    context = {
        'questions':questions,
        'branches':branches
    }
    return render (request,'material/questions_bank.html',context)

def teaching_staff(request) :
    list1 = []
    level_list = ['one', 'two', 'three', 'four']
    list2 = []
    dict2 = {}
    for y in level_list: 
        course = models.Course.objects.filter(level=y)
        list2.clear()
        list1.clear()
        
        for i in course:
            for j in i.subjects.all():
                list1.append(j)
                
                list2 = [str(k) for k in list1]
                
        list3 = [x for x in list2 if list2.count(x) >=2]
        list3 = set(list3)
        list3 = list(list3)
        dict1 = {y:list3}
        dict2[y] = list3
    
    
        
        branches = models.Branch.objects.all()
        for i in branches:
            for l in level_list:
                course2 = models.Course.objects.filter(branch = i,level = l)
                if len(course2)>=1: 
                    for m in course2.first().subjects.all():
                        #if m.name in dict["one"]:
                        #print(m)
                        pass

                                                                                                                                        
    teacher = models.Teacher.objects.all()
    context = {
        'teacher':teacher,
    }
    return render (request,'material/teaching_staff.html',context)


def teacher_profile(request,id):
    teacher = models.Teacher.objects.get(id = id)

    return render(request, 'material/teacher_profile.html', {'teacher':teacher})

def table(request) :
    #user1 = models.Student.objects.get(user=request.user)
    #course = models.Course.objects.filter(branch=user1.branch,level = user1.level)
    branche = models.Branch.objects.all()
    #print(" subjects ",course.first().subjects.first())
    context = {
        'branche':branche,
    }

    return render (request,'material/table.html',context)

def branches(request) :
    branche = models.Branch.objects.all()
    context = {
        'branche':branche,
    }

    return render (request,'material/table.html',context)





def signin(request) :
    return render (request,'material/signin.html',{})

def signup(request) :
    return render (request,'material/signup.html',{})

def student_form(request):
    if request.method == 'POST':

        form = forms.StudentExtraForm(request.POST )
        if form.is_valid():

            return redirect('basedashboard')
    else:
        form = forms.StudentExtraForm()

    return render (request,'material/student_form.html',{'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = forms.UserUpdateForm(request.POST, instance=request.user)
        p_form = forms.ProfileUpdateForm(request.POST,request.FILES,instance=request.user.student)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = forms.UserUpdateForm(instance=request.user)
        p_form = forms.ProfileUpdateForm(instance=request.user.student)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'material/profile.html', context)



""" def common_subject(request):
 """    
    


""" @login_required
def teacher_profile(request):


    context = {
        
    }

    return render(request, 'material/teacher_profile.html', context) """





"""
student = models.Student.objects.create(user = request.user,full_name = request.POST['full_name'],mobile=request.POST['mobile'],image=request.POST['image'],gender=request.POST['gender'],age=request.POST['age'],branch = models.Branch.objects.get(name = request.POST['branch']),level=request.POST['level'])
            student.save()
            
def table(request) :
    print(models.Student.objects.get(user=request.user).level)
    user1 = models.Student.objects.get(user=request.user)
    course = models.Course.objects.filter(branch=user1.branch,level = user1.level)
    print(" subjects ",course.first().subjects.first())
    context = {
        'course':course,
    }

    return render (request,'material/table.html',context)            
            
 """



