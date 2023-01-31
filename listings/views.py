from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm


# Create your views here.

# CRUD - create, retrieve, update, delete, list


def listing_list(request):
    listings = Listing.objects.all()  # Fetch all the listings
    context = {  # Create a dictionary with our key pointing to this database call
        "listings": listings
    }
    return render(request, "listings.html", context)


def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)


def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)  # Populating the form with all the request data
        if form.is_valid():
            form.save()  # Saves data into database
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)


def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing, files=request.FILES)  # Updating a specific listing with second parameter
        if form.is_valid():
            form.save()  # Saves data into database
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)


def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")
