from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Category, CategoryProduct, Product
from django.db.models import F
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  
from cart.forms import CartAddProductForm


class ProductList(ListView):
    model = Product
    template_name = "shop/shop.html"
    paginate_by = 2
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(available=True)

def product_list(request, category_product_slug=None):
    category_product = None
    categories_product = CategoryProduct.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 1)
    page = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    try:  
        page_obj = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        page_obj = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        page_obj = paginator.page(paginator.num_pages) 
    if category_product_slug:
        category_product = get_object_or_404(CategoryProduct, slug=category_product_slug)
        products = products.filter(category_product=category_product)
    return render(request, 'shop/shop.html',{'category_product': category_product,'categories_product': categories_product,'products': products, 'page': page, 'page_obj': page_obj})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/single-product.html', {'product': product, 'cart_product_form': cart_product_form})
    








def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'shop/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserLoginForm()  
    return render(request, 'shop/login.html', {"form": form})

def user_logout (request):
    logout(request)
    return redirect('login')

class BlogPost(ListView):
    model = Post
    template_name = 'shop/blog.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context

# def index(request):
#     return render(request, template_name='shop/blog.html')

class CategoryByPost(ListView):
    template_name = 'shop/blog.html'
    context_object_name = 'posts' 
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    
class ViewPost(DetailView):
    model = Post
    template_name = "shop/blog-details.html"
    context_object_name = 'post_item'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context