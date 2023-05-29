from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import *
from .serializers import EmployeeSerializer, PayStubSerializer, TimeOffRequestSerializer
from django.http import JsonResponse
from django.shortcuts import render
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
# class EmployeeUpdateAPIView(APIView):
def EmployeeUpdateAPIPostView(request):
    try:
        if request.method == 'POST':
            try:
                body = request.body
                bodyObj = json.loads(body)
                id = bodyObj['id']
                fName = bodyObj['fName']
                lName = bodyObj['lName']
                email = bodyObj['email']
                desig = bodyObj['desig']
                add = bodyObj['add']

                userUpdate = Employee(id = id,first_name = fName, last_name = lName,email = email,designation = desig, address= add)
                userUpdate.save()
                return JsonResponse({"status":"success"})
            except Exception as ex:
                return JsonResponse({"status":"failed"})
    except Exception as ex:
        return ex

def PayStubCreateAPIView(request):
    try:
        if request.method == "POST":
            try:     
                bdy = request.body
                bdyObj = json.loads(bdy)
                id = bdyObj['id']
                emp = bdyObj['emp']
                stdate = bdyObj['stdate']
                enddate = bdyObj['enddate']
                grossearning = bdyObj['grossearning']
                ot = bdyObj['ot']

                pretax = bdyObj['pretax']
                ot = bdyObj['ot']
                fdincome = bdyObj['fdincome']
                stincome = bdyObj['stincome']
                posttax = bdyObj['posttax']
                emplrcontrbtn = bdyObj['emplrcontrbtn']
                netpay = bdyObj['netpay']
                usr = Paystub1(id = id, employee=emp, pay_period_start=stdate, pay_period_end=enddate, gross_earnings=grossearning, overtime_earnings=ot, pre_tax_deductions=pretax, federal_income_tax=fdincome, state_income_tax=stincome,post_tax_deductions=posttax,employer_contribution=emplrcontrbtn,net_pay=netpay)
                usr.save()
                return JsonResponse({"status":"success"})
            except Exception as ex:
                return JsonResponse({"status":"failed"})
             
    except Exception as ex: 
        print(ex)
    

@csrf_exempt
def TimeOffRequestCreateAPIView(request):

    try:
        if request.method == "POST":
            try:  
                timeoff = request.body
                timeoffrequest = json.loads(timeoff)
                id = timeoff['id']
                emp = timeoff['emp']
                startdate = timeoff['startdate']
                enddate = timeoff['enddate']
                approved = timeoff['approved']
                reason = timeoff['reason']

                timeoffrequest = Employee(id = id, employee = emp,start_date = startdate, end_date = enddate, reason = reason, is_approved = approved)  
                timeoffrequest.save()
                return JsonResponse({"status":"success"})
            except Exception as ex:
                return JsonResponse({"status":"failed"})
             
    except Exception as ex: 
        print(ex)



        # form = TimeOffRequestForm(request.POST)
        # if form.is_valid():
        #     time_off_request = form.save(commit=False)
        #     time_off_request.employee_id = 1  # Assuming 1 is the employee ID
        #     time_off_request.save()
        #     return JsonResponse({'status': 'success', 'message': 'Time off request created successfully'})
        # else:
        #     return JsonResponse({'status': 'error', 'message': form.errors}, status=400)

# def my_view(request):
#     employee_form = EmployeeForm()
#     paystub_form = PayStubForm()
#     timeoff_form = TimeOffRequestForm()
    
#     context = {
#         'employee_form': employee_form,
#         'paystub_form': paystub_form,
#         'timeoff_form': timeoff_form,
#     }
    
#     return render(request, 'template.html', context)