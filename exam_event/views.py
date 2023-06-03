from django.shortcuts import render, redirect

from .forms import ExamForm
from .models import Exam


# Create your views here.
def list_exams(request):
    exams = Exam.objects.all()
    is_admin_user = request.user.is_admin
    print(is_admin_user)
    context = {
        "exams": exams,
        "is_admin_user": is_admin_user
    }
    return render(request, template_name='exam_event/list-events.html', context=context)


def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam-list')
    else:
        form = ExamForm()
    return render(request, 'exam_event/create_exam.html', {'form': form})


def home(request):
    return render(request, 'exam_event/home.html')
