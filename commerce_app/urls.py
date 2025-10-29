from django.urls import path
from commerce_app import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, ChangesPasswordForm, ResetPassword, PasswordResetConfirm


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('subscribe/', views.SubscribeView, name='subscribe'),
    path('newsletter/', views.NewsletterView, name='newsletter'),
    path('shop/', views.ShopProductsView.as_view(), name='shop'),
    path('mensf/', views.MensItem.as_view(), name='mens_fashion'),
    path('womensf/', views.WomensItem.as_view(), name='womens_fashion'),
    path('babysf/', views.BabysItem.as_view(), name='babys_fashion'),
    path('shirtsf/', views.ShirtsItem.as_view(), name='shirts_fashion'),
    path('jeansf/', views.JeansItem.as_view(), name='jeanss_fashion'),
    path('jacketsf/', views.JacketsItem.as_view(), name='jacket_fashion'),
    path('shoesf/', views.ShoesItem.as_view(), name='shoes_fashion'),
    path('seatersf/', views.SweaterItem.as_view(), name='sweater_fashion'),
    path('winter-colletion/', views.Winter_Collection, name='winter_colletion'),
    path('Spring-colletion/', views.Spring_collection, name='Spring_colletion'),

    path('register/', views.RegisterFormView.as_view(), name='register_form'),

 
    path('changespassword/', auth_views.PasswordChangeView.as_view(template_name='Shop/passwordchange.html', form_class=ChangesPasswordForm, success_url='/changespassword/done/'), name='password_changes'),
    path('changespassword/done/', auth_views.PasswordChangeDoneView.as_view(template_name='Shop/password_change_done.html'), name='password_changes_done'),
    
    
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='Shop/reset_password.html', form_class=ResetPassword), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='Shop/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='Shop/password_reset_confirm.html', form_class = PasswordResetConfirm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='Shop/password_reset_complete.html'), name='password_reset_complete'),
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='Shop/login.html', authentication_form=LoginForm), name=
    'login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    
    path('product-detail/<int:pk>', views.ProductDetailsView.as_view(), name='shop_detail'),
    path('addcart/',views.AddToCart, name='addcart'),
    path('allcart/<int:pk>', views.AllProductCartView.as_view(), name='all_cart_show'),
    path('shop-product/', views.ShopProductsViewS.as_view(), name='shop_product'),
    path('cart/', views.CartCheckOut, name='cart_show'),
    path('checkout/', views.OrderPlacedView.as_view(), name='checkout'),
    # path('savecheckout/', views.CheckoutView, name='save_checkout'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('faqs/', views.FaqsView, name='faqs'),
    path('orders/', views.order, name='order'),
    
    
    path('pluscart/', views.plus_Cart),
    path('minuscart/', views.minus_Cart),
    path('removecart/', views.remove_Cart),
    
    

    path('faq/', views.FAQView.as_view(), name='faq'),
    path('help-support/', views.HelpSupportView.as_view(), name='help_support'),

    # Payment URLs
    path('payment/', views.payment_demo, name='payment_demo'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)