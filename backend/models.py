from django.db import models

from django.contrib.auth.models import AbstractUser

from functools import partial

def path_img(instance, filename):
    return '/'.join(['img',instance.type_img,filename])
class ImgFiles(models.Model):
    TYPE_IMG = [
        ('MN','Main img'),
        ('TO','Tournament'),
        ('NW','News'),
        ('US','User'),
        ('TM','Team'),
        ('CO','Countries'),
        ('GD','Game Discipline') 
    ]
    type_img = models.CharField(
        max_length=2,
        choices=TYPE_IMG,
        default="NW",
    )
    file = models.ImageField(upload_to=path_img)
    name = models.CharField(max_length=100,blank=True)
    def __str__(self) -> str:
        if self.name != self.file:
            return self.name
        return f'{self.file}'
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
class Countries(models.Model):
    ava = models.ForeignKey(ImgFiles,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f'c_{self.name}'
class GameDiscipline(models.Model):
    name = models.CharField(max_length=100)
    ava = models.ForeignKey(ImgFiles,on_delete=models.CASCADE,null=True)
    text_info = models.TextField()
    def __str__(self):
        return f'g_{self.name}'
class Team(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=5)
    ava = models.ForeignKey(ImgFiles,on_delete=models.CASCADE,null=True)
    users = models.ManyToManyField('User',related_name='users',blank=True)
    tournaments = models.ManyToManyField('Tournament',blank=True)
    def __str__(self) -> str:
        return f't_{self.name}'
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
    country = models.ForeignKey(Countries,on_delete=models.CASCADE,null=True)
    date_of_becoming_an_esportsman = models.DateField(auto_now=True, auto_now_add=False,blank=True)
    main_game = models.ForeignKey(GameDiscipline,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team',null=True)
    ava = models.ForeignKey(ImgFiles,on_delete=models.CASCADE,null=True)
    age = models.IntegerField(default=0)
    text_info = models.TextField(blank=True)
    type_user = models.CharField(
        max_length=2,
        choices=TYPE_USER,
        default=PLAYER,
    )
    def __str__(self) -> str:
        return f'u_{self.username}'
class News(models.Model):
    date = models.DateField()
    time = models.TimeField()
    img = models.ForeignKey(ImgFiles,on_delete=models.CASCADE,null=True,related_name='img')
    short_text = models.CharField(max_length=100)
    full_text = models.TextField()
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def __str__(self) -> str:
        return f'n_{self.slug}'
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
class Match(models.Model):
    name = models.CharField(max_length=100)
    img = models.ForeignKey(ImgFiles,on_delete=models.CASCADE,null=True)
    teams = models.ManyToManyField(Team,related_name='teams')
    winner = models.ForeignKey(Team,null=True,on_delete=models.CASCADE,related_name='winner')
    result = models.CharField(max_length=10)
    map_veto = models.TextField()
    date = models.DateField()
    text_info = models.JSONField()
    videofile = models.FileField(upload_to='videos/', null=True)
    def __str__(self):
        return f'm_{self.name}'
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    ava = models.ForeignKey(ImgFiles,on_delete=models.CASCADE,null=True)
    teams = models.ManyToManyField(Team)
    data_start = models.DateField()
    data_end = models.DateField()
    schedule = models.ManyToManyField(Match)
    def __str__(self):
        return f'tou_{self.name}'