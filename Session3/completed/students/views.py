from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "students/list.html",
        {"students": students}
    )

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