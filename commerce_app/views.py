from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import View
from .models import Product, Cart , Subscribe, NewsletterModel, AddressBook, OrderPlacedFormModel, OrderPlacement, FAQ
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import RegisterForm, LoginForm, NewsletterForm, SubscribeForm, ContactForms, OrderPlacedForm, FAQForms
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate




# Create your views here.
class HomeView(View):
    def get(self, request):
        mens_item = Product.objects.filter(category="Mens")
        mens_count = mens_item.count()
        womens_item = Product.objects.filter(category="Women")
        womens_count = womens_item.count()
        babys_item = Product.objects.filter(category="Baby")
        babys_count = babys_item.count()
        shirts_item = Product.objects.filter(category="Shirts")
        shirts_count = shirts_item.count()
        jeans_item = Product.objects.filter(category="Jeans")
        jeans_count = jeans_item.count()
        sweater_item = Product.objects.filter(category="Sweater")
        sweater_count = sweater_item.count()
        shoes_item = Product.objects.filter(category="Shoes")
        shoes_count = shoes_item.count()
        accerssories_item = Product.objects.filter(category="Accerssories")
        accerssories_count = accerssories_item.count()
        bags_item = Product.objects.filter(category="Bags")
        bags_count = bags_item.count()
        
        
        trenday_products = Product.objects.filter(trandy_products=True)
        jarrived_products = Product.objects.filter(just_arrived=True)
        
        return render(request, 'Shop/home.html', {'mens_item': mens_item, 'womens_item': womens_item, 'mens_count': mens_count, 'womens_count': womens_count, 'babys_count': babys_count, 'shirts_count': shirts_count, 'jeans_count': jeans_count, 'sweater_count': sweater_count, 'shoes_count': shoes_count, 'accerssories_count': accerssories_count, 'bags_count': bags_count, 'trenday_products': trenday_products, 'jarrived_products': jarrived_products})
    

def Winter_Collection(request):
    winter_collection = Product.objects.filter(win_collection=True)
    return render(request, 'Shop/winter-colletion.html', {'winter_collection': winter_collection})

def Spring_collection(request):
    spring_product = Product.objects.filter(spring_collection=True)
    return render(request, 'Shop/spring_collection.html', {'spring_product': spring_product})
    
    # def get(self, request):
    #     mens_item = Product.objects.filter(category="Mens")
    #     means_count = mens_item.count()
    #     return render(request, 'Shop/home.html', {'means_count': means_count})
    
    # def get(self, request):
    #     womens_item = Product.objects.filter(category="Women")
    #     womens_count = womens_item.count()
    #     return render(request, 'Shop/home.html', {'womens_count': womens_count})
    
    
    
class ShopProductsView(View):
    def get(self, request):
        allproducts = Product.objects.all()
        paginator = Paginator(allproducts, 15)
        page = request.GET.get('page')
        try:
            items = paginator.page(page)

        except PageNotAnInteger:
                  items = paginator.page(1)

        except EmptyPage:
                  items = paginator.page(paginator.num_pages)

        # Get cart product IDs for current user
        cart_product_ids = []
        if request.user.is_authenticated:
            cart_product_ids = list(Cart.objects.filter(user=request.user).values_list('product_id', flat=True))

        return render(request, 'Shop/shop.html', {'items': items, 'cart_product_ids': cart_product_ids})


class ShopProductsViewS(View):
     def get(self, request):
        allproducts = Product.objects.filter(is_active='True')
        return render(request, 'Shop/shop.html', {'allproducts': allproducts})
      
class MensItem(View):
    def get(self, request):
        mens_item = Product.objects.filter(category="Mens")
        return render(request, 'Shop/mens.html', {'mens_item': mens_item})
      
class WomensItem(View):
    def get(self, request):
        womens_item = Product.objects.filter(category="Women")
        return render(request, 'Shop/womens.html', {'womens_item': womens_item})
      
class BabysItem(View):
    def get(self, request):
        babys_item = Product.objects.filter(category="Baby")
        return render(request, 'Shop/babys.html', {'babys_item': babys_item})
      
class ShirtsItem(View):
    def get(self, request):
        shirts_item = Product.objects.filter(category="Shirts")
        return render(request, 'Shop/shirts.html', {'shirts_item': shirts_item})
      
class JeansItem(View):
    def get(self, request):
        jeans_item = Product.objects.filter(category="Jeans")
        return render(request, 'Shop/jeans.html', {'jeans_item': jeans_item})
      
class JacketsItem(View):
    def get(self, request):
        jackets_item = Product.objects.filter(category="Jackets")
        return render(request, 'Shop/jackets.html', {'jackets_item': jackets_item})
      
class ShoesItem(View):
    def get(self, request):
        total_product = 0
        shoes_item = Product.objects.filter(category="Shoes")
        products_count = shoes_item.count()
        return render(request, 'Shop/shoes.html', {'shoes_item': shoes_item, 'total_product': total_product, 'products_count': products_count})
      
      
class SweaterItem(View):
    def get(self, request):
        sweater_item = Product.objects.filter(category="Sweater")
        return render(request, 'Shop/sweater.html', {'sweater_item': sweater_item})


class RegisterFormView(View):
    def get(self, request):
        regi_form = RegisterForm()
        return render(request, 'Shop/register.html', {'regi_form': regi_form})
    
    def post(self, request):
        regi_form = RegisterForm(request.POST)
        if regi_form.is_valid():
            regi_form.save()
            messages.success(request, "Congratulation! Your Register Successfully Done..!!")
        return render(request, 'Shop/register.html', {'regi_form': regi_form})  
 
    
# class ProductDetailsView(View):
#         def get(self, request, pk):
#             products = Product.objects.get(pk=pk)
#             return render(request, 'Shop/shop-details.html', {'products': products})

    
class ProductDetailsView(View):
    def get(self, request, pk):
        products = Product.objects.get(pk=pk)

        # Check if product is in user's cart
        in_cart = False
        if request.user.is_authenticated:
            in_cart = Cart.objects.filter(user=request.user, product=products).exists()

        return render(request, 'Shop/shop-details.html', {'products': products, 'in_cart': in_cart})



# class AllProductCartView(View):
#     def get(self, request, pk):
#         cart_product = Product.objects.get(pk=pk)
#         Cart(user=request.user, product=cart_product).save()
#         return redirect('/cart')

class AllProductCartView(View):
    def get(self, request, pk):
        cart_product = Product.objects.get(pk=pk)

        # Check if product already exists in cart
        existing_cart = Cart.objects.filter(user=request.user, product=cart_product).first()
        if existing_cart:
            # If exists, increment quantity
            existing_cart.quantity += 1
            existing_cart.save()
        else:
            # If not exists, create new cart entry
            Cart(user=request.user, product=cart_product).save()

        referer = request.META.get('HTTP_REFERER')
        if not referer:
            return redirect('home')
        return redirect(referer)



def AddToCart(request):
    user = request.user
    prod_id = request.GET.get('product_id')
    product = Product.objects.get(id=prod_id)

    # Check if product already exists in cart
    existing_cart = Cart.objects.filter(user=user, product=product).first()
    if existing_cart:
        # If exists, increment quantity
        existing_cart.quantity += 1
        existing_cart.save()
    else:
        # If not exists, create new cart entry
        Cart(user=user, product=product).save()

    return redirect('/cart')

        
def CartCheckOut(request):
    if request.user.is_authenticated:
        user = request.user
        cart_item = Cart.objects.filter(user=user)

        amount = 0.0
        Shipping_fee = 100.0
        total = 0.0
        cart_product = [product for product in Cart.objects.all() if product.user == user]
        if cart_product:
            for product in cart_product:
                cart_amount = (product.quantity)*(product.product.discount_price)
                amount += cart_amount
                totalamount = amount+Shipping_fee
            return render(request, 'Shop/cart.html', {'cart_item': cart_item, 'amount': amount, 'totalamount': totalamount})

        else:
            return render(request, 'Shop/empty_cart.html')
    else:
        # Redirect to login page if user is not authenticated
        return redirect('login')


def plus_Cart(request):
    if request.method == 'GET':
        prod_id = request.GET['product_id']
        cart = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        cart.quantity += 1
        cart.save()

        amount = 0.0
        Shipping_fee = 100.0
        cart_product = [product for product in Cart.objects.all() if product.user == request.user]
        for product in cart_product:
            cart_amount = (product.quantity)*(product.product.discount_price)
            amount += cart_amount
            total_amount = amount+Shipping_fee

        # Calculate item amount for this specific product
        item_amount = cart.quantity * cart.product.discount_price

        data = {
               'quantity': cart.quantity,
               'item_amount': item_amount,
               'amount': amount,
               'totalamount': total_amount
        }
        return JsonResponse(data)
    
def minus_Cart(request):
    if request.method == 'GET':
        prod_id = request.GET['product_id']
        cart = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))

        # Check if quantity is greater than 1 before decreasing
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            # If quantity is 1, remove the item from cart
            cart.delete()
            amount = 0.0
            Shipping_fee = 100.0
            cart_product = [product for product in Cart.objects.all() if product.user == request.user]
            for product in cart_product:
                cart_amount = (product.quantity)*(product.product.discount_price)
                amount += cart_amount
            total_amount = amount + Shipping_fee

            data = {
                'quantity': 0,
                'item_amount': 0,
                'amount': amount,
                'totalamount': total_amount,
                'removed': True
            }
            return JsonResponse(data)

        amount = 0.0
        Shipping_fee = 100.0
        cart_product = [product for product in Cart.objects.all() if product.user == request.user]
        for product in cart_product:
            cart_amount = (product.quantity)*(product.product.discount_price)
            amount += cart_amount
            total_amount = amount+Shipping_fee

        # Calculate item amount for this specific product
        item_amount = cart.quantity * cart.product.discount_price

        data = {
               'quantity': cart.quantity,
               'item_amount': item_amount,
               'amount': amount,
               'totalamount': total_amount,
               'removed': False
        }
        return JsonResponse(data)
    
    
def remove_Cart(request):
    if request.method == 'GET':
        prod_id = request.GET['product_id']
        cart = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        cart.delete()
        
        amount = 0.0
        Shipping_fee = 100.0
        cart_product = [product for product in Cart.objects.all() if product.user == request.user]
        for product in cart_product:
            cart_amount = (product.quantity)*(product.product.discount_price)
            amount += cart_amount
            total_amount = amount+Shipping_fee
            
            
        data = {
               'amount': amount,
               'totalamount': total_amount
        }
        return JsonResponse(data)
    
    
def SubscribeView(request):
    subscribe_form = SubscribeForm()
    if request.method == "POST":
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            eml = subscribe_form.cleaned_data['email']
            subs_data = Subscribe(email=eml)
            subs_data.save()
            return redirect('home')
            # return render(request, 'Shop/home.html', {'subscribe_form': subscribe_form})
    else:
        subscribe_form = SubscribeForm()
        return redirect('home')

    
def NewsletterView(request):
    newsletter = NewsletterForm()
    if request.method == 'POST':
        newsletter = NewsletterForm(request.POST)
        if newsletter.is_valid():
            user = newsletter.cleaned_data['username']
            el = newsletter.cleaned_data['email']
            newsle_data = NewsletterModel(username=user, email=el)
            newsle_data.save()
            print('news data', newsle_data)
            return redirect('home')
        return render(request, 'Shop/home.html', {'newsletter': newsletter})

    else:
        newsletter = NewsletterForm()
        return redirect('home')


class ContactView(View):
    def get(self, request):
        contact_form = ContactForms()
        contact_profile = AddressBook.objects.filter(user=request.user)
        return render(request, 'Shop/contact.html', {'contact_form': contact_form, 'contact_profile': contact_profile})
    
    def post(self, request):
        contact_form = ContactForms(request.POST)
        if contact_form.is_valid():
            usr = request.user
            nm = contact_form.cleaned_data['name']
            pvnce = contact_form.cleaned_data['province']
            city = contact_form.cleaned_data['city']
            email = contact_form.cleaned_data['email']
            phn = contact_form.cleaned_data['phone']
            area = contact_form.cleaned_data['area']
            add = contact_form.cleaned_data['address']
            addbooks = AddressBook(user=usr, name=nm, province=pvnce, city=city, email=email, phone=phn, area=area, address=add)
            addbooks.save()
        return render(request, 'Shop/contact.html', {'contact_form': contact_form})
    
    
# def ContactProfile(request):
#     contact_profile = AddressBook.objects.filter(user=request.user) 
#     return render(request, 'Shop/contact.html', {'contact_profile': contact_profile})   

def FaqsView(request):
    return render(request, 'Shop/FAQs.html')



class OrderPlacedView(View):
    def get(self, request):
        orderplaced_form = OrderPlacedForm()
        addbook = AddressBook.objects.filter(user=request.user)
        cart_item = Cart.objects.filter(user=request.user)
        amount = 0.0
        shipping = 100.0
        total_amount = 0.0
        cart_product = [product for product in Cart.objects.all() if product.user == request.user]
        if cart_product:
            for product in cart_product:
                sub_amount = (product.quantity)*(product.product.discount_price)
                amount += sub_amount
                totalamount = amount+shipping
            return render(request, 'Shop/checkout.html', {'orderplaced_form': orderplaced_form, 'amount': amount, 'cart_item': cart_item, 'totalamount': totalamount, 'addbook': addbook})

    def post(self, request):
        # Get selected address
        add_id = request.POST.get('add_id')
        if not add_id:
            messages.error(request, 'Please select a delivery address')
            return redirect('checkout')

        # Store address ID in session and redirect to payment page
        request.session['selected_address_id'] = add_id
        request.session['payment_method'] = request.POST.get('payment', 'card')

        return redirect('payment_demo')
    


def order(request):
    add_order = OrderPlacement.objects.filter(user=request.user)  
    add_book = AddressBook.objects.filter(user=request.user)  
    return render (request, 'Shop/orders.html', {'add_order': add_order, 'add_book': add_book})


class FAQView(View):
    def get(self, request):
        faq_forms = FAQForms()
        return render(request, 'Shop/FAQs.html', {'faq_forms': faq_forms})
    
    def post(self, request):
        faq_forms = FAQForms(request.POST)
        if faq_forms.is_valid():
            ques_title = faq_forms.cleaned_data['question_title']
            ques_description = faq_forms.cleaned_data['question_description']
            
            faq_data = FAQ(question_title=ques_title, question_description=ques_description)
            faq_data.save()
        return render(request, 'Shop/FAQs.html', {'faq_forms': faq_forms})


class HelpSupportView(View):
    def get(self, request):
        return render(request, 'Shop/help_and_support.html')


def payment_demo(request):
    """Display demo payment gateway page"""
    if not request.user.is_authenticated:
        return redirect('login')

    # Calculate cart totals
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items.exists():
        return redirect('cart')

    amount = 0.0
    shipping = 100.0
    for item in cart_items:
        amount += item.quantity * item.product.discount_price
    total_amount = amount + shipping

    selected_address_id = request.session.get('selected_address_id')

    return render(request, 'Shop/payment_demo.html', {
        'amount': amount,
        'total_amount': total_amount,
        'selected_address_id': selected_address_id
    })


def process_payment(request):
    """Process demo payment and create order"""
    if request.method != 'POST' or not request.user.is_authenticated:
        return redirect('checkout')

    user = request.user
    cart_items = Cart.objects.filter(user=user)

    if not cart_items.exists():
        messages.error(request, 'Your cart is empty')
        return redirect('cart')

    # Get payment details (Demo - Not storing sensitive data)
    cardholder_name = request.POST.get('cardholder_name', 'Demo User')
    card_number_last4 = request.POST.get('card_number', '')[-4:] if request.POST.get('card_number') else '****'

    # Create payment info record (without storing full card details)
    payment_info = OrderPlacedFormModel(
        user=user,
        cardholder_name=cardholder_name,
        card_number=f"****-****-****-{card_number_last4}",  # Only store last 4 digits
        cvv_code='***',  # Never store CVV
        billing_address='Demo Payment',
        month='01',
        year='2025'
    )
    payment_info.save()

    # Get selected address
    address_id = request.session.get('selected_address_id')
    try:
        address = AddressBook.objects.get(id=address_id, user=user)
    except AddressBook.DoesNotExist:
        messages.error(request, 'Please select a valid address')
        return redirect('checkout')

    # Create orders for each cart item
    for cart_item in cart_items:
        order = OrderPlacement(
            user=user,
            addressbook=address,
            payment_info=payment_info,
            product=cart_item.product,
            quantity=cart_item.quantity,
            status='Accepted'
        )
        order.save()

    # Clear cart
    cart_items.delete()

    # Clear session
    request.session.pop('selected_address_id', None)
    request.session.pop('payment_method', None)

    messages.success(request, 'Payment successful! Your order has been placed.')
    return redirect('payment_success')


def payment_success(request):
    """Display payment success page"""
    if not request.user.is_authenticated:
        return redirect('login')

    # Get the most recent order
    latest_orders = OrderPlacement.objects.filter(user=request.user).order_by('-order_date')[:5]

    return render(request, 'Shop/payment_success.html', {
        'orders': latest_orders
    })