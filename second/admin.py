from django.contrib import admin
from .models import FavoriteGroup, Favorite, TodoGroup, Todo

# Register your models here.
@admin.register(FavoriteGroup)
class FavoriteGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass

@admin.register(TodoGroup)
class FavoriteAdmin(admin.ModelAdmin):
    pass

@admin.register(Todo)
class FavoriteAdmin(admin.ModelAdmin):
    pass