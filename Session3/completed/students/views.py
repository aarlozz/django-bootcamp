from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

@login_required
def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "students/list.html",
        {"students": students}
    )
@login_required
def student_create(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("student-list")

    else:
        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {"form": form}
    )
@login_required
def student_update(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":
        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect("student-list")

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "students/student_form.html",
        {"form": form}
    )
@login_required
def student_delete(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":
        student.delete()
        return redirect("student-list")

    return render(
        request,
        "students/student_confirm_delete.html",
        {"student": student}
    )

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(
        request,
        "registration/register.html",
        {"form": form}
    )