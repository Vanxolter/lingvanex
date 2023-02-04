from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from main.forms import YearSortedForm, SearchAppsForm
from main.functions import sort_by_years
from main.models import Parse_data
from main.queries import filter_years


def main_page(request):
    '''
    Вьюха отображения списка аппок

    :param request:
    :type request:
    :return:
    :rtype:
    '''
    if request.method == "POST":
        search_form = SearchAppsForm(request.POST)
        if search_form.is_valid():
            name_company: str = search_form.cleaned_data["name_company"]
            all_apps = Parse_data.objects.all()
            if name_company:
                all_apps = Parse_data.objects.filter(name_company=name_company).all()
            else:
                all_apps = Parse_data.objects.all()

            data = sort_by_years(request, all_apps)

            return render(request,
                          'main_page.html',
                          {'page': data["page"],
                           'apps': data["apps"],
                           "sorted_form": data["sorted_form"],
                           "search_form": search_form,

                           })
    else:

        search_form = SearchAppsForm()
        all_apps = Parse_data.objects.all()
        data = sort_by_years(request, all_apps)

        return render(request,
                      'main_page.html',
                      {'page': data["page"],
                       'apps': data["apps"],
                       "sorted_form": data["sorted_form"],
                       "search_form": search_form,

                       })
