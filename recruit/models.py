from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class Recruit(models.Model):
    name = models.CharField(max_length=50)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='recruits')
    age = models.IntegerField()
    mail = models.EmailField()

    def __str__(self):
        return self.name


class Task(models.Model):
    description = models.CharField(max_length=100, default='Enter a question')

    def __str__(self):
        return self.description


class Test(models.Model):
    order = models.IntegerField(unique=True)
    tasks = models.ManyToManyField(Task)


class Answer(models.Model):
    question = models.CharField(max_length=256)
    answer = models.CharField(max_length=6)

    def __str__(self):
        return self.question


class PassedTest(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name='passedtests')
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.recruit.name


class Sith(models.Model):
    name = models.CharField(max_length=30)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='siths')
    shadowhand = models.ManyToManyField(PassedTest, related_name='siths')

    def __str__(self):
        return self.name