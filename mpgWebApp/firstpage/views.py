from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd


# Create your views here.

import joblib

reloadModel=joblib.load('/Users/hritik/Car mileage/mpgWebApp/model/RFModelforMPG.pk1')

def index(request):
    context={'a':''}
    return render(request,'index.html',context)
    #return HttpResponse({'a':1})

def predictMPG(request):
    print (request)
    if request.method == 'POST':
        temp={}
        temp['cylinders']=request.POST.get('cylinderVal')
        temp['displacement']=request.POST.get('dispVal')
        temp['horsepower']=request.POST.get('hrsPwrVal')
        temp['weight']=request.POST.get('weightVal')
        temp['acceleration']=request.POST.get('accVal')
        temp['model_year']=request.POST.get('modelVal')
        temp['origin']=request.POST.get('originVal')

        temp2=temp.copy()
        temp2['model year']=temp['model_year']
        print (temp.keys(),temp2.keys())

    testDtaa=pd.DataFrame({'x':temp2}).transpose()   
    scoreval=reloadModel.predict(testDtaa)[0]
    context={'scoreval':scoreval}
    return render(request,'index.html',context)