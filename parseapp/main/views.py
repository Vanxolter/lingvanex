from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main.models import Parse_data


def main_page(request):
    context = Parse_data.objects.all()
    paginator = Paginator(context, 10)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        apps = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        apps = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        apps = paginator.page(paginator.num_pages)
    return render(request,
                  'main_page.html',
                  {'page': page,
                   'apps': apps,
                   })