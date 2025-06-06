from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bonus = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='players')
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, blank=True, null=True, related_name='players')
    skills = models.ManyToManyField(Skill, blank=True, related_name='players')

    def __str__(self):
        return self.nickname
