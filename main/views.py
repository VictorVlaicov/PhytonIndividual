from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Review, Apartment, Client


def default(request):
    reviews = Review.objects.all()
    return render(request, 'main/main.html', {'reviews': reviews})


def main(request):
    reviews = Review.objects.all()
    return render(request, 'main/main.html', {'reviews': reviews})


def main_sorted(request):
    reviews = Review.objects.order_by('-datetime')
    return render(request, 'main/main.html', {'reviews': reviews})


def apartments(request):
    list_apartments = Apartment.objects.all()
    return render(request, 'main/apartments.html', {'apartments': list_apartments})


def sort_ap(request):
    list_apartments = Apartment.objects.order_by('price')
    return render(request, 'main/apartments.html', {'apartments': list_apartments})


def ap_detail(request, ap_id):
    try:
        apartment = Apartment.objects.get(id=ap_id)
    except:
        raise Http404('Apartment not found')
    apartment_list = [apartment]
    return render(request, 'main/apartments.html', {'apartments': apartment_list})


@csrf_exempt
def add_review(request):
    try:
        a = Apartment.objects.get(id=request.POST['ap_id'])
    except:
        raise Http404('Apartment not found')
    client = Client.objects.get_or_create(firstName=request.POST['clientFirstName'],
                                          lastName=request.POST['clientLastName'],
                                          email=request.POST['clientEmail'])
    review = Review(
        client=client[0],
        apartment=a,
        content=request.POST['content'],
        datetime=timezone.datetime.now()
    )
    review.save()
    reviews = Review.objects.all()
    return render(request, 'main/main.html', {'reviews': reviews})

