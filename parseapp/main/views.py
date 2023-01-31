from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from main.forms import YearFilterForm
from main.models import Parse_data
from main.queries import filter_years


def main_page(request):
    all_apps = Parse_data.objects.all()

    filters_form = YearFilterForm(request.GET)
    if filters_form.is_valid():
        order_by = filters_form.cleaned_data["order_by"]
        context = filter_years(all_apps, order_by)

        paginator = Paginator(context, 10)
        page = request.GET.get('page')

        try:
            apps = paginator.page(page)
        except PageNotAnInteger:
            apps = paginator.page(1)
        except EmptyPage:
            apps = paginator.page(paginator.num_pages)

        return render(request,
                      'main_page.html',
                      {'page': page,
                       'apps': apps,
                       "filters_form": filters_form,
                       })