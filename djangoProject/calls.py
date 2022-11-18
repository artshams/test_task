from django.http import JsonResponse
from djangoProject.models import Categories, Products


def get_categories(request):
    res = {}
    for cat in Categories.objects.all():
        res[cat.name] = [i.name for i in cat.prods.all()]
    return JsonResponse(res, safe=False)


def get_products(request):
    res = {}
    prods = Products.objects.all()
    for prod in prods:
        res[prod.name] = [i.name for i in prod.categories.all()]
    return JsonResponse(res, safe=False)


def get_pairs(request):
    pairs = Products.objects.values('name', 'categories')
    return JsonResponse(list(pairs), safe=False)
