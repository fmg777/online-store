from django.shortcuts import render, get_object_or_404
from .models import Content,Caregory
from cart.forms import CartAddProductForm



def content_list (request, category_slug=None):
    category = None
    categories = Caregory.objects.all()
    contents = Content.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Caregory,slug=category_slug)
        contents = contents.filter(category=category)
    return render(request, 'shop/list1.html', {'category': category, 'categories': categories, 'content': contents})




# def contant_detail(request,id,slug):
#     content = get_object_or_404(Content, id=id, slug=slug, available=True)
#     return render(request,'shop/detail.html', {'content': content})




def contant_detail(request, id, slug):
    content = get_object_or_404(Content,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/detail.html', {'content': content,
                                                        'cart_product_form': cart_product_form})