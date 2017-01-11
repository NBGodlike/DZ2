from models import Course, Comment, User, Luser
from forms import CreateForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.urls import reverse
from django.views.generic import TemplateView,ListView
from django.views import View
from django.http import Http404
from django.views.generic.detail import DetailView


def index(request):
    return render(request, 'index.html')


def sub(request):
    luser = request.user.id
    course = Course.objects.get(pk=request.POST.get("id"))
    course.lusers.add(luser)
    return redirect('/')


def createcourse(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            course = Course()
            course.name = request.POST.get('name')
            course.duration = request.POST.get('duration')
            course.teacher = request.POST.get('teacher')
            course.value = request.POST.get('value')
            course.picture = request.FILES.get('picture')
            course.save()
            return redirect(reverse("Course", kwargs={"pk": course.pk}))
    else:
        form = CreateForm()
    return render(request, 'createcourses.html', {'form': form})


def login(request):
    errors = []
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors.append('Enter login')

        password = request.POST.get('password')
        if not password:
            errors.append('Enter password')

        user = authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect('/course/')
        else:
            errors.append('Incorrect login or password')
        return render(request, 'index1.html', {'errors': errors, 'username': username})

    return render(request, 'index1.html', {'errors': errors})


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


def registration(request):
    errors = []
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors.append('Enter login')

        if len(str(username)) < 5:
            errors.append('So small login (5)')

        password = request.POST.get('password')
        if len(str(password)) < 6:
            errors.append('So small password (6)')

        password2 = request.POST.get('password2')
        if password != password2:
            errors.append('Different passwords')

        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        if (not username) or (not password) or (not password2) or (not first_name) or (not last_name):
            errors.append('Fill all fields')
        else:
            if len(errors) == 0:
                users = User.objects.filter(username=username)
                if len(users) != 0:
                    errors.append('Login used')
                    return render(request, 'registrations1.html', {'errors': errors, 'username': username,
                                                                   'last_name': last_name, 'first_name': first_name})
                else:

                    u = User()
                    u.username = username
                    u.password = make_password(password)
                    u.last_name = last_name
                    u.first_name = first_name
                    u.is_active = True
                    u.is_superuser = False
                    u.save()

                    b = Luser()
                    b.username = username
                    b.password = make_password(password)
                    b.last_name = last_name
                    b.first_name = first_name
                    b.save()

            return HttpResponseRedirect('/course/')

        return render(request, 'registrations1.html', {'errors': errors, 'username': username,
                                                       'last_name': last_name, 'first_name': first_name})

    return render(request, 'registrations1.html', {'errors': errors})


class CourseListView(ListView):
    template_name = "course_list.html"
    model = Course
    context_object_name = "Courses"
    paginate_by = 10


class Online(CourseListView):
    template_name = 'course.html'


class PostView(DetailView):
    model = Course
    context_object_name = 'Course'
    template_name = 'onecourse.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        course_object = context[self.context_object_name]
        courses = course_object.lusers.all()
        context = dict(context, courses=courses)
        return context

    def get_object(self):
        object = super(PostView, self).get_object()
        if not self.request.user.is_authenticated():
            raise Http404
        return object
