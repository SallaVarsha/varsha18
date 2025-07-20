from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.shortcuts import render, get_object_or_404
from .models import Product


# ✅ Product List View
def product_list(request):
    category_id = request.GET.get('category')
    query = request.GET.get('q')

    products = Product.objects.all()
    categories = Category.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)

    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'catalog/product_list.html', {
        'products': products,
        'categories': categories,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})
# ✅ Add to Cart
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')

# ✅ Remove from Cart
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('view_cart')

# ✅ View Cart
def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        subtotal = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })
        total_price += subtotal

    return render(request, 'catalog/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

# ✅ Order History Placeholder
def order_history(request):
    return render(request, 'catalog/order_history.html')

# ✅ Signup Placeholder
def signup(request):
    return render(request, 'catalog/signup.html')

# ✅ Logout (optional if using Django built-in LogoutView)
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('product_list')
