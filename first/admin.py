from django.contrib import admin
from .models import Students, Score

# Register your models here.
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass