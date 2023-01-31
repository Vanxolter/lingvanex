def filter_years(purchase, order_by):
    if order_by:
        if order_by == "-release_year":
            purchase = purchase.order_by("-release_year")
        if order_by == "release_year":
            purchase = purchase.order_by("release_year")
    return purchase