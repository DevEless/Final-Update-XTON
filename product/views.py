from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def updateProduct(request, id):
    edit = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('back_product')
    else:
        form = ProductForm(instance=edit)
    return render(request, 'Projet_Final/back/back_edit.html', {'form': form})

def destroy_Product(request, id):
    destroy = Product.objects.get(id=id)
    destroy.delete()
    return redirect('back_product')

def createProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('back_product')
    else:
        form = ProductForm()
    return render(request, 'Projet_Final/back/back_edit.html', {"form": form})


def get_default_km(kms, selected_km):
    available_kms = ['0-10,000 km', '10,000-30,000 km', '30,000-50,000 km', '50,000-70,000 km', '70,000+ km']

    if selected_km in kms and selected_km in available_kms:
        return selected_km
    else:
        for km in available_kms:
            if km in kms:
                return km

    return available_kms[0]


def readProduct(request, id):
    notes = Note.objects.all().filter(product=id)
    show = Product.objects.get(id=id)
    kms = [km for km in show.stock.keys() if show.get_stock_quantity(km) > 0]
    wishlist_products = None

    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()

    selected_km = request.GET.get('km', '0-10,000 km')  # Récupère le kilométrage sélectionné dans l'URL (par défaut '0-10,000 km')

    # Mettre à jour le "selected_km" en fonction du stock disponible
    selected_km = get_default_km(kms, selected_km)

    stock_quantity = show.get_stock_quantity(selected_km)

    # Tri des kilométrages dans l'ordre spécifié
    kms = sorted(kms, key=lambda x: ['0-10,000 km', '10,000-30,000 km', '30,000-50,000 km', '50,000-70,000 km', '70,000+ km'].index(x))

    return render(request, 'Projet_Final/front/products-type-1.html', {"show": show, "notes": notes, "kms": kms, "selected_km": selected_km, "stock_quantity": stock_quantity, 'wishlist_products': wishlist_products})


def comment_create(request, id):

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        titre = request.POST.get('review-title')
        text = request.POST.get('texte')

        if request.user.is_authenticated:
            current_note = Note.objects.create(
                author=request.user,
                product=product,
                titre=titre,
                text=text
            )
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')

            anonymous_user = AnonymousUser.objects.create(
                name=name,
                email=email
            )

            current_note = Note.objects.create(
                anonymous_author=anonymous_user,
                product=product,
                titre=titre,
                text=text
            )

        return redirect('detail_Product', id=id)

    return render(request, 'Projet_Final/front/products-type-1.html')
