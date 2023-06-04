from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.models import User
from .forms import ExamForm
from .models import Exam, Bookings


# Create your views here.
def list_exams(request):
    exams = Exam.objects.all()
    is_admin_user = request.user.is_admin
    is_challenged_user = request.user.is_physically_challenged_user
    print(is_admin_user)
    context = {"exams": exams, "is_admin_user": is_admin_user, "is_challenged_user": is_challenged_user, }
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


def list_scrib(request, exam_id):
    scribs = User.objects.filter(is_volunteer=True)
    current_event_content_id = exam_id
    is_challenged_user = request.user.is_physically_challenged_user
    context = {"scribs": scribs, "is_challenged_user": is_challenged_user, "exam_id": current_event_content_id}
    return render(request, template_name='exam_event/list-scribes.html', context=context)


def book_scribe(request, exam_id, volunteer_id):
    exam_volunteer = User.objects.get(id=volunteer_id)
    exam_attendee = User.objects.get(id=request.user.id)
    exam_event = Exam.objects.get(id=exam_id)
    bookings = Bookings()
    bookings.exam = exam_event
    bookings.volunteer = exam_volunteer
    bookings.exam_attendee = exam_attendee
    bookings.save()
    message = f"<h2>Your Event has been booked with {exam_volunteer.username} </h2>"
    return HttpResponse(message)
