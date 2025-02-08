from django.contrib import admin
from .models import Diplom, HeroBlock, About

@admin.register(HeroBlock)
class HeroBlockAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(About)

admin.site.register(Diplom)

