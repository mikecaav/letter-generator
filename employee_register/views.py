from django.shortcuts import render, redirect
from reportlab.pdfgen import canvas
from django.http import FileResponse

from .forms import EmployeeForm
from .models import Employee


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        else:
            print("Form was not valid")
        return redirect('/employee/list')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')


def report(request, id):
    employee = Employee.objects.get(pk=id)
    p = canvas.Canvas('report.pdf')
    i = 800
    columns = ["name", "last_name", "enterprise", "street", "street_number", "suite_number", "neighborhood", "municipality",
     "state", "postal_code", "number", "email", "position_id"]
    for column in columns:
        p.drawString(10, i, f"{column}: {str(employee.__getattribute__(column))}")
        i -= 20
    p.showPage()  # Create the PDF
    p.save()

    return FileResponse(open('report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
