from django.shortcuts import get_object_or_404
from featuretickets.models import FeatureTicket

def cart_contents(request):
    """
    Make cart contents available on each page
    """
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    

    for id, contribution in cart.items():
        feature = get_object_or_404(FeatureTicket, pk=id)
        contribution = feature.contribution
        total += contribution
        cart_items.append({'id': id, 'contribution': contribution, 'feature': feature})
    
    return { 'cart_items': cart_items, 'total': total }