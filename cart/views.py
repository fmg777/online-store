from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Content
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, content_id):
    cart = Cart(request)
    content = get_object_or_404(Content, id=content_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(content=content,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, content_id):
    cart = Cart(request)
    content = get_object_or_404(Content, id=content_id)
    cart.remove(content)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})