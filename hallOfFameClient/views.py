import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View, generic
from django.views.generic.list import ListView

from hallOfFameClient.db_manager import getFullGroupData
from hallOfFameClient.models import Subject, Student, Lecturer, Group

class TabView(View):
    template_name = 'hallOfFameClient/tab.html'
    subject = Subject.objects.first()

    groups = subject.groups.all()

    groupsCtx = {}
    for group in groups:
        groupsCtx[group.pk] = {}
        groupsCtx[group.pk]["name"] = group.name
        groupsCtx[group.pk]["scores"] = {}

        exercises = group.exercises.all()
        students = group.students.all()
        groupsCtx[group.pk]["exercises"] = exercises.values()
        groupsCtx[group.pk]["students"] = students.values()

        groupsCtx[group.pk]["scores"]["sum"] = {}
        for student in group.students.all():
            groupsCtx[group.pk]["scores"][student.pk] = {}
            groupsCtx[group.pk]["scores"]["sum"][student.pk] = 0

        groupsCtx[group.pk]["max_score"] = 0
        for exercise in exercises:
            groupsCtx[group.pk]["max_score"] += exercise.max_score
            for score in exercise.scores.all():
                groupsCtx[group.pk]["scores"][score.student.pk][score.exercise.pk] = score.value
                groupsCtx[group.pk]["scores"]["sum"][score.student.pk] += score.value

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'groupsCtx': self.groupsCtx, "subject": self.subject})


class DashboardStudentView(ListView):
    template_name = 'hallOfFameClient/dashboard_student.html'
    student = Student.objects.filter(album_number=213700).first()
    model = Subject

    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.student.name + " " + self.student.surname
        context[
            'diagramUrl'] = "https://media.discordapp.net/attachments/689977881535053839/701202475906236456/unknown.png"
        context['myAverage'] = "88"
        context['semesterAverage'] = "76"
        return context

class DashboardLecturerView(ListView):
    template_name = 'hallOfFameClient/dashboard_lecturer.html'
    lecturer = Lecturer.objects.filter(name__exact="Szymon").first()
    model = Group
    subjects = Subject.objects.all()

    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.lecturer.name + " " + self.lecturer.surname
        context['subjects'] = self.subjects
        context[
            'diagramUrl'] = "https://media.discordapp.net/attachments/689977881535053839/701202475906236456/unknown.png"
        context['myAverage'] = "88"
        context['semesterAverage'] = "76"
        return context
