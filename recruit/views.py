from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import  Sith,  Test, Recruit, Answer, PassedTest
import random
from .forms import NewRecruitForm
from django.views.generic import View
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')


class RecruitCreate(View):
    def get(self, request):
        form = NewRecruitForm()
        return render(request, 'recruit.html', {'form': form})

    def post(self, request):
        bound_form = NewRecruitForm(request.POST)

        if bound_form.is_valid():
            new_recruit = bound_form.save()
            return redirect('test', recruit=new_recruit)
        return render(request, 'recruit.html', {'form': bound_form})


one_test = random.choice(Test.objects.all())  # Рандом объекта теста, не придумал как сделать иначе


def test(request, recruit):
    if request.method == 'POST':
        passed_test = PassedTest.objects.create(
            recruit=Recruit.objects.get(name='{}'.format(recruit))
            )
        for test in one_test.tasks.all():
            answer = request.POST.get('{}'.format(test.pk))
            new_answer = Answer.objects.create(
                question=test.description,
                answer=answer)
            passed_test.answers.add(new_answer)
        return redirect('success')
    return render(request, 'test.html', {'user': recruit, 'test': one_test})


def choose_sith(request):
    siths = Sith.objects.all()
    return render(request, 'sith.html', {'siths': siths})


class ChooseRecruit(View):
    def get(self, request, pk):
        sith = get_object_or_404(Sith, pk=pk)
        siths = Sith.objects.all()
        recruits = PassedTest.objects.all()
        return render(request, 'choose_recruits.html', {'sith': sith, 'recruits': recruits, 'siths': siths})

    def post(self, request, pk):
        recruit = Recruit.objects.get(name='{}'.format(request.POST['Shadowhand']))
        passed = PassedTest.objects.get(recruit=recruit)
        Sith.objects.get(pk=pk).shadowhand.add(passed)
        send_mail('Hello {}!'.format(recruit.name),
                  'We are writing you from RecruiteMe Platform. According to your answers we glad to inform you that you have been chosen by {}! Congratulations!'.format(Sith.objects.get(pk=pk).name),
                  'gordeykodesign@gmail.com',
                  ['{}'.format(recruit.mail)],
                  fail_silently=False)

        return render(request, 'success.html',)


def success(request):
    return render(request, 'success.html')