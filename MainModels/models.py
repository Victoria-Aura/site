from django.db import models

# Create your models here.




def path_ava(instance, filename):
    return '/'.join(['ava', str(instance.img_id), filename])
class Gallery(models.Model):
    img_id = models.AutoField(primary_key=True)
    file = models.ImageField(upload_to=path_ava)

class Countrys(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
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
    country = models.ForeignKey(Countrys,on_delete=models.CASCADE)
    date_of_becoming_an_esportsman = models.DateField(auto_now=False, auto_now_add=False)
    main_game = models.ForeignKey('GameDiscipline',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ava = models.ForeignKey(Gallery,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()
    info = models.TextField(blank=True)
    type_user = models.CharField(
        max_length=2,
        choices=TYPE_USER,
        default=PLAYER,
    )
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользовательли'

class Team(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=5)
    ava = models.ForeignKey(Gallery,on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    tournaments = models.ManyToManyField('Tournament',blank=True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

class GameDiscipline(models.Model):
    name = models.CharField(max_length=100)
    ava = models.ForeignKey(Gallery,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
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
    ava = models.ForeignKey(Gallery,on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)
    data_start = models.DateField()
    data_end = models.DateField()
    schedule = models.ManyToManyField(Match)
    def __str__(self):
        return self.name