from django.db import models
import time


class User(models.Model):
    objects = models.Manager()
    ID = models.CharField(primary_key=True, max_length=50)
    def __str__(self):
        return self.ID


class Record(models.Model):
    objects = models.Manager()
    RecordNum = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # 기본키 제거, 유저가 삭제되면 같이 삭제
    Date = models.DateField(default = time.strftime('%Y-%m-%d'))
    Stage = models.IntegerField(default=0)
    Score = models.IntegerField(default=0)

    def __int__(self):
        return self.RecordNum


class Logined(models.Model):
    objects = models.Manager()
    LoginedNum = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # 기본키 제거, 유저가 삭제되면 같이 삭제

    def __int__(self):
        return self.LoginedNum
