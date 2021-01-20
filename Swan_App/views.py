from django.shortcuts import render
from django.http import HttpResponse
from Swan_App.models import User,Category,Item,Order,Orderdone

def index(request):
	category_Item = Item.objects.all()
	contex = {
		'Data':category_Item
	}
	return render(request,'index.html',contex)

def demo(request):
	return render(request,'demo.html')

def category(request):
	category_Item = Item.objects.all()
	contex = {
		'Data':category_Item
	}
	return render(request,'category.html',contex)

def elements(request):
	return render(request,'elements.html')

def cart(request):
	orders = Order.objects.all()
	contex = {
		'Data':orders
	}
	return render(request,'cart.html',contex)

def login(request):
	count = request.session.get('page_count',0)
	request.session['page_count'] = count+1
	return render(request,'login.html')

def registration(request):
	return render(request,'registration.html')

# Actions

def registrationaction(request):
	username = request.GET.get('username')
	password = request.GET.get('password')
	email = request.GET.get('email')
	address = request.GET.get('address')
	mobileno = request.GET.get('mobileno')

	u = User(username=username,password=password,email=email,address=address,mobileno=mobileno)
	print(u)
	u.save()
	return render(request,'login.html')


def loginaction(request):
	username = request.GET.get('username')
	password = request.GET.get('password')

	l = User.objects.all()
	print(l)

	for i in l:
		if username == i.username and password == i.password:
			k = i.id
			print(k)
			contex = {
				'Userid':k
			}
			request.session['k'] = k
			return render(request,'index.html',contex)
	else:
		return render(request,'login.html')

def addcartaction(request):
	c_id = request.GET.get('id')
	print(c_id)
	session_id = request.GET.get('session_id')
	name = request.GET.get('name')
	price = request.GET.get('price')
	img = request.GET.get('img')
	obj = User.objects.all()

	if session_id == session_id:
		entry = User.objects.get(pk=session_id)
		order_Customer = Order(name=name,price=price,user=entry)
		order_Customer.save()
		category_Item = Item.objects.all()
		contex = {
					'Data':category_Item
				}
		return render(request,'category.html',contex)
	return render(request,'login.html')
	
	# for i in obj:
	# 	if c_id == i.id:
	# 		obj1 = i
	
	# return render(request,'category.html')

	

	

def logout(request):
	del request.session['k']
	return render(request,'login.html')

# Create your views here.






