from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import Post,PricingPlan
from .forms import PostForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user) 
    else:
        posts = []
    
    context = {
        'posts': posts
    }

    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create_user(username=email,email=email,password=password)
            user.save()
            return redirect('signin')
    return render(request,'register.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            request.session.set_expiry(0)
            return redirect('index')
    return render(request,'signin.html')

def signout(request):
    logout(request)
    return redirect('signin')

def create_post(request): 
    if request.method == 'POST': 
        form = PostForm(request.POST) 
        if form.is_valid(): 
            title = form.cleaned_data['title'] 
            content = form.cleaned_data['content'] 
            user = User.objects.get(id = request.user.id)
            Post.objects.create(author = user,title = title, content=content) 
            return redirect('index') 
    else: 
        form = PostForm() 
    context = { 
        'form': form 
    } 
    return render(request, 'create_post.html',context)

def edit_post(request,id): 
    if request.method == 'POST': 
        title = request.POST['title'] 
        content = request.POST['content'] 
        Post.objects.filter(id=id).update(title=title,content=content) 
        return redirect('index') 
 
 
    post = Post.objects.get(id=id) 
    form = PostForm(instance=post) 
    context = { 
        'posts':post, 
        'form':form 
    } 
    return render(request,'edit_post.html',context) 


def delete_post(request,id): 
    post = Post.objects.get(id=id) 
    post.delete() 
    return redirect('index')


def read_more(request,id):
    post = Post.objects.get(id = id)
    context = {
        'post':post
    }
    return render(request,'read_more.html',context)

import razorpay
def pricing_view(request):
    plans = PricingPlan.objects.all()
    return render(request, 'pricing.html', {'plans': plans})

def payment(request,id):

    plan = PricingPlan.objects.get(id=id)
    client = razorpay.Client(auth=("rzp_test_n0lhpmrEfeIhGJ", "UOrbXQGnsEc2dhB1IFg0zNWZ"))
    data = { "amount": int(plan.price*100), "currency": "INR", "receipt": str(id) }
    context = {
        'data':data,
        'plan':plan
    }

    return render(request,'payment.html',context)


from django.core.mail import send_mail
from django.conf import settings
def payment_success(request):
    payment_id = request.GET.get('payment_id','N/A')
    id = request.GET.get('id','N/A')
    send_mail(
        'Payment Successful',
        f'Your payment with ID {payment_id} was successful for plan ID {id}.',
        settings.DEFAULT_FROM_EMAIL,
        ['customer@example.com'], 
        fail_silently=False,
    )
    context = {
        'payment_id': payment_id,
        'id': id
    }
    return render(request, 'payment_success.html', context)


def about(request):
    return render(request,'about.html')