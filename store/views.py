from django.shortcuts import render, redirect
from store.models import Product
# Create your views here.
def cartItems(cart):
    items=[]
    for item in cart:
        items.append(Product.objects.get(id=item))
    return items

def cart(request):
    cart=request.session['cart']
    request.session.set_expiry(0)
    ctx={
    'cart':cart,
    'cart_size':len(cart),
    'cart_items':cartItems(cart),
    'total':priceCart(cart)
    }

    return(render(request,"cart.html",ctx))

def priceCart(cart):
    cart_items=cartItems(cart)
    price=0
    for item in cart_items:
        price+=item.price
    return price





def catalog(request):
    if 'cart' not in request.session:
        request.session['cart']=[]
    cart = request.session['cart']
    request.session.set_expiry(0)

    store_items = Product.objects.all()

    ctx={
    'store_items' : store_items,
    'cart_size' : len(cart),
    }

    if request.method =="POST":
        cart.append(int(request.POST['obj_id']))
        return redirect("catalog")

    return render(request,"catalog.html",ctx)


def removeFromCart(request):
    request.session.set_expiry(0)
    obj_to_remove= int((request.POST['obj_id'])[0])
    obj_index=request.session['cart'].index(obj_to_remove)

    request.session['cart'].pop(obj_index)
    return redirect('cart')
