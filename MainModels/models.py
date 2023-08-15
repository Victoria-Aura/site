from django.db import models

from django.contrib.auth.models import AbstractUser


def path_ava(instance, filename):
    return '/'.join(['ava', str(instance.id), filename])
class Countries(models.Model):
    name = models.CharField(max_length=100)
    @classmethod
    def get_default_pk(cls):
        exam, created = cls.objects.get_or_create(
            name='default exam', 
        )
        return exam.pk
class GameDiscipline(models.Model):
    name = models.CharField(max_length=100)
    ava = models.ImageField(upload_to=path_ava)
    @classmethod
    def get_default_pk(cls):
        exam, created = cls.objects.get_or_create(
            name='default exam', 
        )
        return exam.pk
    def __str__(self):
        return self.name
class Team(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=5)
    ava = models.ImageField(upload_to=path_ava)
    users = models.ManyToManyField('User',related_name='users',blank=True)
    tournaments = models.ManyToManyField('Tournament',blank=True)
    @classmethod
    def get_default_pk(cls):
        exam, created = cls.objects.get_or_create(
            name='default exam', 
        )
        return exam.pk
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
class User(AbstractUser):
    COACH = 'CO'
    MANAGER = 'MA'
    CAPTAIN = 'CA'
    PLAYER = 'PL'
    TYPE_USER = [
        (CAPTAIN, 'Captain'),
        (PLAYER, 'Player'),
        (COACH,'Coach'),
        (MANAGER,'Manager') 
    ]
    country = models.ForeignKey(Countries,on_delete=models.CASCADE,default=Countries.get_default_pk)
    date_of_becoming_an_esportsman = models.DateField(auto_now=True, auto_now_add=False,blank=True)
    main_game = models.ForeignKey(GameDiscipline,on_delete=models.CASCADE,default=GameDiscipline.get_default_pk)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team',default=Team.get_default_pk)
    ava = models.ImageField(upload_to=path_ava)
    age = models.IntegerField(default=0)
    info = models.TextField(blank=True)
    type_user = models.CharField(
        max_length=2,
        choices=TYPE_USER,
        default=PLAYER,
    )
    def __str__(self) -> str:
        return self.username

class Match(models.Model):
    teams = models.ManyToManyField(Team,related_name='teams')
    winner = models.ForeignKey(Team,null=True,on_delete=models.CASCADE,related_name='winner')
    result = models.CharField(max_length=10)
    map_veto = models.TextField()
    data = models.DateField()
    info = models.JSONField()
    videofile= models.FileField(upload_to='videos/', null=True)
    def __str__(self):
        return f'{self.id}'
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    ava = models.ImageField(upload_to=path_ava)
    teams = models.ManyToManyField(Team)
    data_start = models.DateField()
    data_end = models.DateField()
    schedule = models.ManyToManyField(Match)
    def __str__(self):
        return self.name