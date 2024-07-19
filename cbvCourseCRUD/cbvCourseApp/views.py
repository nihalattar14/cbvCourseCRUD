from django.shortcuts import render
from cbvCourseApp.models import Course
from django.urls import reverse_lazy
from django.views.generic import *

# Create your views here.

class CourseListView(ListView):
    model = Course
    print(model)

class CourseDetailView(DetailView):
    model = Course

class CourseCreateView(CreateView):
    model = Course
    fields = ('name','description','instructor','rating')

class CourseUpdateView(UpdateView):
    model = Course
    fields = ('instructor','rating',)

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses')