from django.shortcuts import render, redirect

from main.models import Parse_data


def main_page(request):
    context = Parse_data.objects.filter().all
    return render(request, 'main_page.html', {"context": context})


