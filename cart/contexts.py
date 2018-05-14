from django.shortcuts import get_object_or_404
from featuretickets.models import FeatureTicket

def cart_contents(request):
    """
    Make cart contents available on each page
    """
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    feature_count = 0
    
    for id, quantity in cart.items():
        feature = get_object_or_404(FeatureTicket, pk=id)
        print(feature)
        total += quantity * feature.contribution
        feature_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'feature': feature})
    
    return { 'cart_items': cart_items, 'total': total, 'feature_count': feature_count }
    