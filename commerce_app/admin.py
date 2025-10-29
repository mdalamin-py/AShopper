from django.contrib import admin
from .models import (
    AddressBook,
    Product,
    Cart,
    OrderPlacement,
    FAQ,
    Help,
    Review,
    Subscribe,
    NewsletterModel, 
    OrderPlacedFormModel
)


# Register your models here.

@admin.register(AddressBook)
class AddressBook_admin(admin.ModelAdmin):
        list_display = ['user', 'name', 'province', 'city', 'email', 'phone', 'area', 'address']
    
    
@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    list_display = ['title', 'selling_price', 'discount_price', 'category', 'brand', 'description', 'images', 'sizes', 'win_collection', 'trandy_products', 'just_arrived', 'spring_collection', 'fashionable_dress', 'reasonable_price']
    
    
@admin.register(Cart)
class Cart_admin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']
    
    

@admin.register(OrderPlacement)
class OrderPlacement_admin(admin.ModelAdmin):
    list_display = ['user', 'product', 'addressbook', 'payment_info', 'quantity', 'order_date', 'status']
    
    
@admin.register(OrderPlacedFormModel)
class OrderPlacementform_admin(admin.ModelAdmin):
    list_display = ['user','cardholder_name', 'month', 'year', 'card_number', 'cvv_code', 'billing_address']
    
    
@admin.register(FAQ)
class Faq_admin(admin.ModelAdmin):
    list_display = ['question_title', 'question_description']
    
    
@admin.register(Help)
class Help_admin(admin.ModelAdmin):
    list_display = ['user', 'select_topic', 'first_name', 'last_name', 'phone', 'email', 'messages']
    
    
@admin.register(Review)
class Review_admin(admin.ModelAdmin):
    list_display = ['user', 'your_rating', 'your_review', 'your_name', 'your_email', 'created_at']
    
    
@admin.register(Subscribe)
class Subscribe_admin(admin.ModelAdmin):
    list_display = ['email']
    
@admin.register(NewsletterModel)
class NewsletterModel_admin(admin.ModelAdmin):
    list_display = ['username', 'email']


