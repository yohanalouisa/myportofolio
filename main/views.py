from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Yohana Louisa Saragih",
        "npm": "2506584205",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "A Computer Science student at Universitas Indonesia interested "
            "in software development, product management, and education. Always curious and eager to improve." 
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Yohana Louisa Saragih",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)