from django.db import models

class User(models.Model):
    objects = models.Manager()
    ID = models.CharField(primary_key=True, max_length=20)
    PW = models.TextField(max_length=15, default='spaceadmin')

    def __str__(self):
        return self.ID

class Record(models.Model):
    objects = models.Manager()
    RecordNum = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # 기본키 제거, 유저가 삭제되면 같이 삭제
    Date = models.DateField()
    Score = models.IntegerField(default=0)
    def __int__(self):
        return self.RecordNum