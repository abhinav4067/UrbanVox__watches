from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('authentication-register/',views.user_registration,name='authentication-register'),
    path('authentication-login/', views.login1, name='authentication-login'),
    path('account-dashboard/',views.dashboard,name='account-dashboard'),
   
    path('add_product/',views.add_product,name='add_product'),
  
    path('account-orders/',views.account_orders,name='account-orders'),
    path('about-us/',views.about_us,name='about-us'),
    path('product-details/<id1>',views.product_details,name='product-details'),
    path('account-profile/',views.account_profile,name='account-profile'),
    path('account-edit-profile/',views.update_profile,name='account-edit-profile'),
    path('account-saved-address/',views.account_saved_address,name='account-saved-address'),
    path('address/',views.address1,name='address'),
    path('addToCart/<id>',views.addToCart,name='addToCart'),
    path('removeCart/<id>',views.removeCart,name='removeCart'),
    path('addToWishlist/<id>',views.addToWishlist,name='addToWishlist'),
    path('RemoveWishlist/<id>',views.RemoveWishlist,name='RemoveWishlist'),

    path('authentication-reset-password/',views.reset_password,name='authentication-reset-password'),
    
    path('billing-details/',views.billing_details,name='billing-details'),
    path('blog-post/',views.blog_post,name='blog-post'),
   
    path('cart/',views.cart1,name='cart'),  
    path('addToWishlistFromCart/<id>',views.addToWishlistFromCart,name='addToWishlistFromCart'),
    path('contact-us/',views.contact_us,name='contact-us'),
    path('payment-method/',views.payment_method,name='payment-method'),
    path('wishlist/',views.wishlist1,name='wishlist'),
    path('addToCartFromWish/<id>',views.addToCartFromWish,name='addToCartFromWish'),

    path('all-products/', views.all_products,name='all-products'), 
    path('addToWishlistFromAllProducts/<id>',views.addToWishlistFromAllProducts,name='addToWishlistFromAllProducts'),
    path('addToCartFromAllProducts/<id>',views.addToCartFromAllProducts,name='addToCartFromAllProducts'),
    path('navbar/',views.navbar,name='navbar'),
    path('footer/',views.footer,name='footer'),
    path('SignOut/',views.SignOut,name='SignOut'),
    path('search/',views.search,name='search'),
    
    
    
   

]