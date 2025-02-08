from django.shortcuts import render
from .models import Diplom, HeroBlock, About

def home(request):

    about_block = About.objects.first()

    diploms = Diplom.objects.all()

    hero_block = HeroBlock.objects.first()

    context = {
        'hero_block': hero_block,
        'about_block': about_block,
        'diploms': diploms, 

    }

    return render(request, 'main/index.html', context)

