from django.shortcuts import render, redirect, reverse
from featuretickets.models import FeatureTicket


def view_cart(request):
    """
    Display feature ticket review page
    """
    return render(request, 'cart.html')


def add_to_cart(request, id):
    """
    Enable the user to add tickets to their order
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
    Adjust the quantity of tickets ordered
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else: 
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))