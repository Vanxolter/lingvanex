from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from main.forms import YearSortedForm
from main.queries import filter_years


def sort_by_years(request, all_apps):
    """
    функция сортировки по году
    :param request:
    :type request:
    :param all_apps: Все прилажения
    :type all_apps:
    :return:
    :rtype:
    """
    sorted_form = YearSortedForm(request.GET)

    if sorted_form.is_valid():
        order_by = sorted_form.cleaned_data["order_by"]
        sort = filter_years(all_apps, order_by)
        context = {
            "sort": sort,
            "sorted_form": sorted_form
        }
        return paginator_f(request, context)


def paginator_f(request, context):
    '''


    :param request:
    :type request:
    :param context:
    :type context:
    :return:
    :rtype:
    '''
    paginator = Paginator(context["sort"], 10)
    page = request.GET.get('page')

    try:
        apps = paginator.page(page)
    except PageNotAnInteger:
        apps = paginator.page(1)
    except EmptyPage:
        apps = paginator.page(paginator.num_pages)

    return {"page": page, "apps": apps, "sorted_form": context["sorted_form"]}