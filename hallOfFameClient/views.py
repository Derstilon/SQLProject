import json

from django.core import serializers
from django.db.models import Sum, F
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View, generic
from django.views.generic.list import ListView

from hallOfFameClient.db_manager import getFullGroupData
from hallOfFameClient.models import Subject, Group, StudentScore, Student, Exercise


class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello world")


class TabView(View):
    template_name = 'hallOfFameClient/tab.html'

    def getCtx(self):
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
                    groupsCtx[group.pk]["scores"][score.student.pk][score.exercise.pk] = model_to_dict(score)
                    groupsCtx[group.pk]["scores"]["sum"][score.student.pk] += score.value
        return subject, groupsCtx

    def parse_score_name(self, score, value):
        (n, pk, s_id, e_id) = score.split('-')
        if value == '':
            value = 0
        return {"id": pk, "student": s_id, "exercise": e_id, "value": value}

    def filter_request(self, request):
        update_scores = []
        create_scores = []
        print(request.POST["change_info"])
        change_info = json.loads(request.POST["change_info"])
        for req, value in request.POST.items():
            if req[0:3] == "ss-" and change_info.get(req):
                if req[3:5] == "{}":
                    create_scores.append(self.parse_score_name(req, value))
                else:
                    update_scores.append(self.parse_score_name(req, value))
        return update_scores, create_scores

    def post(self, request, *args, **kwargs):

        update_scores, create_scores = self.filter_request(request)

        for score in update_scores:
            q = StudentScore.objects.get(pk=score["id"])
            q.value = score.get("value")
            q.save()

        for score in create_scores:
            student = Student.objects.get(pk=score.get("student"))
            exercise = Exercise.objects.get(pk=score.get("exercise"))
            StudentScore.objects.create(student=student, exercise=exercise,
                                        value=score.get("value"))

        print(update_scores, create_scores)
        msg = "SAVED"
        subject, groupsCtx = self.getCtx()
        return render(request, self.template_name,
                      {'groupsCtx': groupsCtx, "subject": subject, "msg": msg})

    def get(self, request, *args, **kwargs):
        subject, groupsCtx = self.getCtx()
        return render(request, self.template_name,
                      {'groupsCtx': groupsCtx, "subject": subject})


class StatView(View):
    template_name = 'hallOfFameClient/stat.html'
    stat = StudentScore.objects.values("exercise__group__subject", "exercise__group", "exercise", ).annotate(
        sum_value=Sum('value'),
        sum_max_score=Sum('exercise__max_score'))

    stat2 = StudentScore.objects.values("student", "exercise__group__subject", "exercise__group", ).annotate(
        sum_value=Sum('value'),
        sum_max_score=Sum('exercise__max_score'))

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      {"stat": self.stat, "stat2": self.stat2})


class SubjectListView(ListView):
    model = Subject

    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = "Michał Krawczyk"
        context[
            'diagramUrl'] = "https://media.discordapp.net/attachments/689977881535053839/701202475906236456/unknown.png"
        context['myAverage'] = "88"
        context['semesterAverage'] = "76"
        return context
