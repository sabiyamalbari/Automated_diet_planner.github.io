from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
#from django.contrib
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from diets.models import Diet,BodyMassIndex,Calories
from . import views
import subprocess

def index(request):
    return render(request, 'diets/index.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user.is_staff == False:
            login(request, user)
            messages.success(request, ('You have been successfully logged in !'))
            return redirect('input')
        elif user.is_staff == True:
            return redirect('adminpanel')

        else:
            messages.success(request, ('You have failed to login !'))
            return redirect('login_user')
    else:
        return render(request, 'diets/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ('You have successfullylogout...'))
    return redirect('login_user')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if  form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You have registered !'))
            return redirect('input')

    else :
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'diets/signup.html',context)

def input(request):
    if request.method == "POST":
        users= request.user.username
        age = request.POST["age"]
        height = request.POST["height"]
        gender= request.POST["gender"]
        activity= request.POST["activity"]
        diabetes= request.POST["diabetes"]
        heart= request.POST["heart"]
        kidney= request.POST["kidney"]

        weight = request.POST ["weight"]
        ins = Diet(users=users,age=age,height=height,gender=gender,activity=activity,weight=weight)
        ins.save()
        abc= weight * 22
        defg = abc * 2

        

        
        import pandas as pd
        from sklearn.tree import DecisionTreeRegressor
        from sklearn.model_selection import train_test_split
        #from sklearn.preprocessing import OneHotEncoder
        from sklearn.preprocessing import LabelEncoder
        from sklearn import metrics

        #from numpy import argmax
        import numpy as np
        #import sklearn.cross_validation as cross_validation
        print('k')
        diet_file_path = '/home/sabiya/Desktop/diet/diets/train1.csv'
        diet_data = pd.read_csv(diet_file_path) 
        #print(diet_data)
        y=diet_data.iloc[:,12]
        #print(y)
        x = diet_data.iloc[:,[-8,-9,-10,-2]]
        #print(x)
        #x=diet_data.iloc[:,[3,4,5,11]]
        print(type(diet_data))
        print(type(x))
        print(type(y))
        #ohc1=pd.get_dummies(val_x)
        #print(x)
        new_diet_data = pd.read_csv('/home/sabiya/Desktop/diet/diets/test.csv')
        nx=new_diet_data.iloc[:,4]
        ny=new_diet_data.iloc[:,[0,1,2,3]]
        train_x,val_x,train_y,val_y=train_test_split(ny,nx,test_size=0.50,random_state = 0)
        '''ohc=pd.get_dummies(train_x)
        ohc2=pd.get_dummies(val_x)
        ohc3=pd.get_dummies(train_y)
        ohc4=pd.get_dummies(val_y)'''




        print("==========================transformation===========================")

        le=LabelEncoder()
        '''================================kidney_disease=================='''
        kd=diet_data.iloc[:,-10]
        nkd=np.array(kd)
        print(type(nkd))
        le.fit(nkd)
        tkd=le.transform(nkd)

        pd.DataFrame(tkd).to_csv("/home/sabiya/Desktop/diet/diets/formatted.csv",index = False)
        print(type(tkd))
        print(tkd)
        reversetkd=le.inverse_transform(tkd)
        '''================================kidney_disease=================='''
        #print(reversex)
        '''================================heart_disease=================='''
        hd=diet_data.iloc[:,-8]
        nhd=np.array(hd)
        le.fit(nhd)
        #list(le.classes)
        thd=le.transform(nhd)
        pd.DataFrame(thd).to_csv("/home/sabiya/Desktop/diet/diets/formatted2.csv",index = False)
        print(thd)
        reversethd=le.inverse_transform(thd)
        '''================================heart_disease=================='''
        '''================================diabetes=================='''
        dia=diet_data.iloc[:,-9]
        ndia=np.array(dia)
        le.fit(ndia)
        #list(le.classes)
        tdia=le.transform(ndia)
        pd.DataFrame(tdia).to_csv("/home/sabiya/Desktop/diet/diets/formatted3.csv",index = False)
        print(tdia)
        reversetdia=le.inverse_transform(tdia)
        '''================================diabetes=================='''

        print("==========================transformation complete !===========================")
        #dec=enc.dot(OHC.active_features_).astype(int)
        #print(dec)
        #print(ohc1)
        #print(val_x)
        my_model=DecisionTreeRegressor(random_state=1)
        my_model.fit(train_x,train_y)

        #print("The predictions are")
        #pred=my_model.predict(val_x)

        pred=my_model.predict([[1,0,1,3600]])
        gt = np.array(train_y)
        #print(pred)
        #print(pred)

        #fpr,tpr,threshold = metrics.roc_curve(gt,pred,pos_label=2)
        #acc = metrics.auc(fpr, tpr)
        #print(acc)
   
        return render(request, 'diets/input.html', {'input':defg,'users':users})
    else:    
        return render(request, 'diets/input.html')

    
    return render(request, 'diets/input.html')


def adminpanel(request):
    return render(request,'diets/admin_base.html')



def bmi(request):
    if request.method=="POST":
        height=request.POST['height']
        height=float(height)
        weight=request.POST['weight']
        weight=int(weight)
        pip=pow(height,height)
        BMI = weight / pip
        inss=BodyMassIndex(BMI=BMI)
        inss.save()
    
        if BMI <= 18.5:
            return render(request, 'diets/bmi.html', {'xyz':'Your BMI is', 'bmi':f'{BMI:.4}', 'abc':'And  You are Under weight'})
        elif 18.5 < BMI <= 25 :
            return render(request, 'diets/bmi.html', {'xyz':'Your BMI is', 'bmi':f'{BMI:.4}', 'abc':'And You are Normal Weight'})
        elif 25 < BMI <= 29.9 :
            return render(request, 'diets/bmi.html', {'xyz':'Your BMI is', 'bmi':f'{BMI:.4}', 'abc':'And  You are Over Weight'})
        else : BMI >=30 
        return render(request, 'diets/bmi.html', {'xyz':'Your BMI is', 'bmi':f'{BMI:.4}', 'abc':'And You are Obese Weight'})
        return render(request, 'diets/bmi.html', {'bmi':BMI})
        

        
    else:
        return render(request, 'diets/bmi.html')
         
def calorie(request):
    if request.method == "POST":
        activity = request.POST["activity"]
        print("heeeelelxcvkxdvjfuk")
        #print(get_type("activity"))
        weight = request.POST['weight']
        weight = int(weight)
        abc = weight * 22
        if activity == "Senedarty":
            defg = abc * 1.6
        elif activity == "Lightly Active":
            defg = abc * 1.8
        elif activity == "Moderately Active":
            defg = abc * 2.0
        else:
            defg = abc * 2.2
        inx = Calories(defg=defg)
        inx.save()
        return render(request, 'diets/calorie.html', {'xyz':'Your Daily Required Calories Is = ','calories':round(defg)})
        '''return render(request, 'diets/calorie.html', {'xyz':'Your Daily Required Calories Is = ', 'calories':f'{defg:.2}')'''
    return render(request, 'diets/calorie.html')

def detail(request):
    dobj = Diet.objects.all()
    dobjs = BodyMassIndex.objects.all()
    dobjss = Calories.objects.all()
    lll = zip(dobj,dobjs,dobjss)
    return render(request,'diets/detail.html',{'lll':lll})

    

def your_view_name(request):
  if request.method == 'GET':
    form = your_form_name() 
  else:
    if form.is_valid():
      info = request.POST['info_name']
      output = script_function(info) 
      #Here you are calling script_function, 
      #passing the POST data for 'info' to it;
      return render(request, 'diets/input.html', {'info': info, 'output': output, })
  return render(request, 'diets/input.html', {'form': form})

def script_function( post_from_form ) :
  post_from_form
  return subprocess.check_call(['/home/sabiya/Desktop/project/train.py', post_from_form])