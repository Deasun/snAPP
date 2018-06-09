from django.shortcuts import render, redirect, reverse
from featuretickets.models import FeatureTicket


def view_cart(request):
    """
    A view that renders the contents page
    """
    return render(request, 'cart.html')


def add_to_cart(request, id):
    """
    Add a quantity of the specified product to the cart
    """
    quantity=int(request.POST.get('quantity'))
    
    cart=request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    if quantity > 0:
        cart[id] = quantity
    
    else: 
        cart.pop(id)
    
    feature = FeatureTicket.objects.get(pk=id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    

    
    
def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specififed amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    
    else: 
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))