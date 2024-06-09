
from pyexpat.errors import messages
from django.shortcuts import redirect, render

from django.db.models import Avg
# Create your views here.
from datetime import date
from django.shortcuts import render
from . models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.


def user_registration(request):
    if request.POST:
        name=request.POST["u_name"]
        email=request.POST["email"]
        password=request.POST["pass"]
        cpassword=request.POST["cpass"]
        phone_number=request.POST['phone_num']
        location=request.POST['location']
        gender=request.POST['gender']
        dob=request.POST['dob']
        request.POST['location']
        login=Login.objects.create_user(username=email,password=password,userType='customer',viewpassword=password)
        login.save()
        obj=user_reg.objects.create( user=login,u_name=name,u_mobile=phone_number,gender=gender,dob=dob,location=location,u_email=email,u_password=password,u_cpassword=cpassword)
        obj.save()
        return redirect('authentication-login')
    return render(request,'authentication-register.html')




def login1(request):
    
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(username=email,password=password)
        if user:
            login(request,user)
            request.session["user_ID"]=user.id
            return redirect('index') 
        else:
            wrong_message="wrong password"
            messages.error(request,wrong_message)   

    
    return render(request,'authentication-login.html') 



def SignOut(request):
    logout(request)
    return redirect('index')
def dashboard(request):
    return render(request,'account-dashboard.html')  

def add_product(request):
    if request.POST:
        select=request.POST["select"]
        description=request.POST["description"]
        product_price=request.POST["price"]
        product_img=request.FILES["img"]
        obj=product.objects.create(product_name=select,product_description=description,product_price=product_price,product_image=product_img)
        obj.save()
    return render(request,'add_product.html')
   




@login_required(login_url='authentication-login')
def account_orders(request):
    user_id = request.session.get("user_ID")
    reg_id = user_reg.objects.get(user__id=user_id)
    
    data = orders.objects.filter(user_id__id=reg_id.id)
    
    
   
   
    
    return render(request,'account-orders.html',{"order_details":data}) 


def about_us(request):
    return render(request,'about-us.html')



@login_required(login_url='authentication-login')
def account_profile(request):
    user_id = request.session.get("user_ID")
    
    data = user_reg.objects.filter(user__id=user_id)
   

    return render(request,'account-profile.html',{"data":data})

@login_required(login_url='authentication-login')
def update_profile(request):
   
        user_id = request.session.get("user_ID")
        reg_id = user_reg.objects.get(user__id=user_id)
        
        if 'update' in request.POST:
            new_name = request.POST.get('u_name')
            new_email = request.POST.get('u_email')
            new_mobile = request.POST.get('u_mobile')
            new_gender = request.POST.get('u_gender') 
            new_dob = request.POST.get('u_dob')
            new_location = request.POST.get('u_location')

            reg_id.u_name = new_name
            reg_id.u_email = new_email
            reg_id.u_mobile = new_mobile
            reg_id.gender = new_gender
            reg_id.dob = new_dob
            reg_id.location = new_location
            reg_id.save()

            return redirect('account-profile') 

        return render(request, 'account-edit-profile.html')









def account_saved_address(request):
    return render(request,'account-saved-address.html')


def address1(request):
    return render(request,'address.html')
 

def reset_password(request):
    return render(request,'authentication-reset-password.html')



def blog_post(request):
    return render(request,'blog-post.html')



@login_required(login_url='authentication-login')
def cart1(request):
    user_id = request.session.get("user_ID")
    reg_id = user_reg.objects.get(user__id=user_id)
    
    data = cart.objects.filter(user_id__id=reg_id.id)
   
    count = data.count()
   

    

    offer_price=0
    zipped_price=[]
    total=0
    for i in data:
        if i.qty is not None and i.product_id.product_price is not None and i.product_id.product_offer is not None:
            product_price=i.product_id.product_price
            off_percentage=i.product_id.product_offer
            offered_price=int(product_price) * (int(off_percentage) /100)
            offer_price=int(product_price) - int(offered_price)
            total+=i.qty * offer_price
        zipped_price.append((i,offer_price))  
     
    offer=0
    offer_amount=0
    if  total >= 50000: 
         offer=int(total) * (int(2)/100)
         offer_amount=int(total) - int(offer) 
        


    
    bag_offer_price=0
        

    if total<=5000:
        grand_total=total+50
    else:
        grand_total=total

  
    
    context = {
        'count': count,
        'cart1': data,
        'grand_total':grand_total,
        'total': total,
        'offer_price':offer_price,
        'bag_offer_price':bag_offer_price,
        'zipped_price':zipped_price,
        'offer_amount_bag':offer_amount,
        'offer':offer,
        

    }

    return render(request, 'cart.html', context)


@login_required(login_url='authentication-login')
def addToWishlistFromCart(request,id):

    data=product.objects.get(id=id)
  
    u_id=request.session['user_ID']
    user=user_reg.objects.get(user__id=u_id)
    obj=wishlist.objects.create(user_id=user,product_id=data)
    obj.save()
    
       
    return redirect('cart')



def contact_us(request):
    return render(request,'contact-us.html')

def payment_method(request):
    return render(request,'payment-method.html')

def index(request):
    featured_product=product.objects.order_by('priority')[:4]
    latest_product=product.objects.order_by('-id')[:8]
    
    context={
        'featured_product':featured_product,
        'latest_product':latest_product,
        
        
        }
    if 'analog' in  request.POST:
        an=product.objects.filter(product_category__contains="analog")
        context={
            "analog":an
        }
        return render(request,'all-products.html',context)
    
    if 'smart' in  request.POST:
        sm=product.objects.filter(product_category__contains="smart")
        context={
            "smart":sm
        }
        return render(request,'all-products.html',context)
    
    if 'digital' in  request.POST:
        dg=product.objects.filter(product_category__contains="digital")
        context={
            "digital":dg
        }
        return render(request,'all-products.html',context)
    


    

    
        
    return render(request,'index.html',context) 

@login_required(login_url='authentication-login')
def addToCart(request,id):
   
   
    data=product.objects.get(id=id)
    amt=data.product_price
    quantity=1
    u_id=request.session['user_ID']
    user=user_reg.objects.get(user__id=u_id)
    obj=cart.objects.create(user_id=user,product_id=data,qty=quantity,cart_amount=amt)
    obj.save()
    
       
    return redirect('index')
@login_required(login_url='authentication-login')

def addToCartFromWish(request,id):
   
    data=product.objects.get(id=id)
    amt=data.product_price
    u_id=request.session['user_ID']
    user=user_reg.objects.get(user__id=u_id)
    obj=cart.objects.create(user_id=user,product_id=data,cart_amount=amt)
    obj.save()
    
       
    return redirect('wishlist')

@login_required(login_url='authentication-login')
def removeCart(request,id):
    cart_remove=cart.objects.get(id=id)
    cart_remove.delete()


    return redirect('cart')
    

@login_required(login_url='authentication-login')

def addToWishlist(request,id):

    data=product.objects.get(id=id)
    
   
    u_id=request.session['user_ID']
    user=user_reg.objects.get(user__id=u_id)
    obj=wishlist.objects.create(user_id=user,product_id=data)
    obj.save()
    
       
    return redirect('index')

@login_required(login_url='authentication-login')
def addToWishlistFromAllProducts(request,id):

    data=product.objects.get(id=id)
    
   
    u_id=request.session['user_ID']
    user=user_reg.objects.get(user__id=u_id)
    obj=wishlist.objects.create(user_id=user,product_id=data)
    obj.save()
    
       
    return redirect('all-products')

@login_required(login_url='authentication-login')
def addToCartFromAllProducts(request,id):
   
   
    data=product.objects.get(id=id)
    amt=data.product_price
    quantity=1
    u_id=request.session['user_ID']
    user=user_reg.objects.get(user__id=u_id)
    obj=cart.objects.create(user_id=user,product_id=data,qty=quantity,cart_amount=amt)
    obj.save()
    
       
    return redirect('all-products')



def RemoveWishlist(request,id):
    wish_remove=wishlist.objects.get(id=id)
    wish_remove.delete()    
    return redirect('wishlist')



@login_required(login_url='authentication-login')
def product_details(request, id1):
    u_id = request.session['user_ID']
    user = user_reg.objects.get(user__id=u_id)
    data = product.objects.get(id=id1)

    if 'savereview' in request.POST:
        review1 = request.POST["review"]
        rating = request.POST["rating"]
        current_date = date.today()
        obj = review.objects.create(user_review=review1, user_rating=rating, review_date=current_date, user_id=user,
                                    product_id=data)
        obj.save()

    reviews = review.objects.filter(product_id=data)
 
    count = reviews.count()
   

    
    
    count_5star=review.objects.filter(product_id=data, user_rating=5).count()
    count_4star=review.objects.filter(product_id=data, user_rating=4).count()
    count_3star=review.objects.filter(product_id=data, user_rating=3).count()
    count_2star=review.objects.filter(product_id=data, user_rating=2).count()
    count_1star=review.objects.filter(product_id=data, user_rating=1).count()
    sum_of_rating=review.objects.filter(product_id=data)
    sum=0
    for s in sum_of_rating:
        sum+=s.user_rating
        
    average_rating=None
    if count>0:
     average_rating=round(int (sum) / int(count))
    price = data.product_price
    off = data.product_offer
    offer_price = 0
    if price is not None and off is not None:
        result = int(price) * (int(off) / 100)
        offer_price = int(price) - int(result)

    context = {
        'data': data,
        'offer_price': offer_price,
        'off': off,
        'reviews': reviews,
        'count': count,
        'average_rating': average_rating,
        'count_5star':count_5star,
        'count_4star':count_4star,
        'count_3star':count_3star,
        'count_2star':count_2star,
        'count_1star':count_1star,
        
    }

    if 'addToCart' in request.POST:
        qty = request.POST['qty']
        amt = offer_price
        amt = int(amt) * int(qty)
        u_id = request.session['user_ID']
        user = user_reg.objects.get(user__id=u_id)
        obj = cart.objects.create(user_id=user, product_id=data, qty=qty, cart_amount=amt)
        obj.save()

    if 'wishlist' in request.POST:
        u_id = request.session['user_ID']
        user = user_reg.objects.get(user__id=u_id)
        obj = wishlist.objects.create(user_id=user, product_id=data)
        obj.save()

    return render(request, 'product-details.html', context)



def navbar(request):
    
    return render(request,'navbar.html')


@login_required(login_url='authentication-login')
def wishlist1(request):
    user_id=request.session.get("user_ID")
    reg_id=user_reg.objects.get(user__id=user_id)
    
    data=wishlist.objects.filter(user_id__id=reg_id.id)

    count=wishlist.objects.filter(user_id__id=reg_id.id).count()
    context={'count':count,
             'wishlist1':data
             
             }
   

    
    return render(request,'wishlist.html',context)

def all_products(request):
  
    

    products = product.objects.all()
    zipped_data = []

    for data in products:
        price = data.product_price
        off = data.product_offer
        offer_price = 0
        
        if price is not None and off is not None:
            result = int(price) * (int(off) / 100)
            offer_price = int(price) - int(result)
        else:
            offer_price = int(price)
        
        zipped_data.append((data, offer_price))

    context = {
        'zipped_data': zipped_data
    }


    return render(request,'all-products.html',context)




def footer(request):
    return render(request,'footer.html')
def search(request):
    watches_name = None
    watches_brand = None
    combined_results = None
    
    if 'search' in request.POST:
        searchtxt = request.POST.get('tosearch', '').strip()
        
        if searchtxt:
            watches_name = product.objects.filter(product_name__icontains=searchtxt).order_by('-id')
            watches_brand = product.objects.filter(product_brand__icontains=searchtxt).order_by('-id')
            combined_results = (watches_name | watches_brand).distinct()
    
    context = {
        "watches_name": watches_name,
        "watches_brand": watches_brand,
        "combined_results": combined_results,
    }
    
    return render(request, 'search.html', context)


@login_required(login_url='authentication-login')
def addToWishlistFromSearch(request,id):

    data=product.objects.get(id=id)
    
   
    u_id=request.session['user_ID']
    user=user_reg.objects.get(user__id=u_id)
    obj=wishlist.objects.create(user_id=user,product_id=data)
    obj.save()
    
       
    return redirect('search')

@login_required(login_url='authentication-login')
def addToCartFromSearch(request,id):

    data=product.objects.get(id=id)
    
   
    u_id=request.session['user_ID']
    user=user_reg.objects.get(user__id=u_id)
    obj=cart.objects.create(user_id=user,product_id=data)
    obj.save()
    
       
    return redirect('search')










    




def billing_details(request):

    user_id = request.session.get("user_ID")
    reg_id = user_reg.objects.get(user__id=user_id)
    
    data = cart.objects.filter(user_id__id=reg_id.id)


   

    offer_price=0
    zipped_price=[]
    total=0
    for i in data:
        if i.qty is not None and i.product_id.product_price is not None and i.product_id.product_offer is not None:
            product_price=i.product_id.product_price
            off_percentage=i.product_id.product_offer
            offered_price=int(product_price) * (int(off_percentage) /100)
            offer_price=int(product_price) - int(offered_price)
            total+=i.qty * offer_price
        zipped_price.append((i,offer_price))  
     
    offer=0
    offer_amount=0
    if  total >= 50000: 
         offer=int(total) * (int(2)/100)
         offer_amount=int(total) - int(offer) 
         
        


    
    bag_offer_price=0
        

    if total <= 5000:
        grand_total=total+50
    else:
        grand_total=total

    last_total=0
    if offer_amount >= 5000:
         last_total = offer_amount
    else:
          last_total = grand_total
    
    context = {
        
        'cart1': data,
        'grand_total':grand_total,
        'total':total,
        'offer_price':offer_price,
        'bag_offer_price':bag_offer_price,
        'zipped_price':zipped_price,
        
        'offer':offer,
        'last_total':last_total
        

    }


    k=cart.qty
    print(k)
    if request.POST:  
     for item in data:  
        qty = item.qty  

        f_name = request.POST["fname"]
        l_name = request.POST["lname"]
        email = request.POST["email"]
        mobile_number = request.POST["mobile_num"]
        street_address = request.POST["street_address"]
        pincode = request.POST["pincode"]
        city = request.POST["city"]
        country = request.POST["country"]
        current_date = date.today()

        productID = item.product_id

        obj = orders.objects.create(user_id=reg_id, product_id=productID, order_amount=last_total,
                                    ordered_qty=qty, ordered_date=current_date, first_name=f_name, last_name=l_name,
                                    email=email, mobile_num=mobile_number, street_address=street_address,
                                    pincode=pincode, city=city, country=country)

        obj.save()
        product_id = item.product_id.id
        pro = product.objects.get(id=product_id)
        pro.product_qty -= int(qty)
        pro.save()

        data.delete()
        return redirect("cart")

        
    return render(request,'billing-details.html',context)




           
    
   



    








   

    







