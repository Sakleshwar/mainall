from django.urls import path
from .views import *

# app_name = 'hrms'

urlpatterns = [
    path('employee/update', EmployeeUpdateAPIPostView, name='employee-update'),
    path('paystub/create', PayStubCreateAPIView, name='paystub-create'),
    path('timeoff/request', TimeOffRequestCreateAPIView, name='timeoff-request-create'),
]
