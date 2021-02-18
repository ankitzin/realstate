from django.shortcuts import render,get_object_or_404
from .models import Listings
from django.core.paginator import Paginator
from listings.choices import bedroom_choices, price_choices, state_choices
# Create your views here.

def index(request):
    listings = Listings.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'listings':page_obj
    }
    return render(request, 'listings/listings.html',context)

def listing(request,listing_id):
    listing = get_object_or_404(Listings,pk=listing_id)

    context= {
        "listing":listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    context = {
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices,
        'price_choices':price_choices
    }
    return render(request, 'listings/search.html', context)