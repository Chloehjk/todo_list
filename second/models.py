from django.db import models

# Create your models here.
class FavoriteGroup(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    memo = models.TextField()
    reg_date = models.DateField(auto_now_add=True)
    group = models.ForeignKey(FavoriteGroup, on_delete=models.CASCADE)

class TodoGroup(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)
    del_yn = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Todo(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    reg_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    del_yn = models.BooleanField(default=False)
    group = models.ForeignKey(TodoGroup, on_delete=models.CASCADE)
