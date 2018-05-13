from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """A view that renders the contents of cart page"""
    return render(request, 'cart.html')


# Need to change from quantity to specified amount
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    contribution=int(request.POST.get('contribution'))
    
    cart=request.session.get('cart', {})
    cart[id] = cart.get(id, contribution)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))

# Need to change from quantity to specified amount
def adjust_cart(request, id):
    """Adjudt the quantity of the specified product to the specififed amount"""
    contribution = int(request.POST.get('contribution'))
    cart = request.session.get('cart', {})
    
    if contribution > 0:
        cart[id] = contribution
    
    else: 
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))