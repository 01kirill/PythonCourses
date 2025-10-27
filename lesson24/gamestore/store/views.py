from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Game, Order
from decimal import Decimal

def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})

@login_required
def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'game_detail.html', {'game': game})

@login_required
def cart_detail(request):
    cart = request.session.get('cart', {})
    games = []
    total = Decimal(0)
    for game_id, price in cart.items():
        game = Game.objects.get(id=game_id)
        games.append(game)
        total += Decimal(price)
    return render(request, 'cart.html', {'cart_games': games, 'total': total})

@login_required
def cart_add(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    cart = request.session.get('cart', {})
    cart[str(game.id)] = str(game.price)
    request.session['cart'] = cart
    return redirect('store:cart_detail')

@login_required
def cart_remove(request, game_id):
    cart = request.session.get('cart', {})
    cart.pop(str(game_id), None)
    request.session['cart'] = cart
    return redirect('store:cart_detail')

@login_required
def make_order(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('store:cart_detail')
    total = sum(Decimal(price) for price in cart.values())
    Order.objects.create(user=request.user, total=total)
    request.session['cart'] = {}
    return render(request, 'order_done.html', {'total': total})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('store:game_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('store:game_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('store:game_list')
