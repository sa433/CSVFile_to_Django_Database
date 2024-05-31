from django.shortcuts import render, redirect
from django.core.management import call_command
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "stud.html")

def import_student(request):
    if request.method == "POST":
        try:
            call_command('student')
            messages.success(request, 'Successfully imported')
        except Exception as e:
            messages.error(request, f'Error importing student {e}')
        return redirect('/')
    else:
        return redirect("/")