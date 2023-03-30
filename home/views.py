from django.http import JsonResponse
from .models import employees
from .serializers import employeesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET", "POST"])
def employees_list(request):
    if request.method == 'GET':
        employee = employees.objects.all()
        serializer = employeesSerializer(employee, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        employee = employees.objects.create(
            emp_name = request.data['emp_name'],
            email = request.data['email'],
            gender = request.data['gender'],
            dept = request.data['dept'],
            country = request.data['country'],
            salary = request.data['salary']
        )
        serializer = employeesSerializer(employee, many = False)
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def employee_detail(request, pk):

    employee = employees.objects.get(pk = pk)
    
    if request.method == "GET":
        serializer =  employeesSerializer(employee, many = False)
        return Response(serializer.data)
    
    if request.method == "PUT":
        employee.emp_name = request.data['emp_name'],
        employee.email = request.data['email'],
        employee.gender = request.data['gender'],
        employee.dept = request.data['dept'],
        employee.country = request.data['country'],
        employee.salary = request.data['salary']
        employee.save()
        serializer =  employeesSerializer(employee, many = False)
        return Response(serializer.data)

    if request.method == "DELETE":
        employee.delete()
        return Response("User was deleted")