from django.db import models

class User(models.Model):
	username = models.CharField(max_length=64)
	password = models.CharField(max_length=64)
	address = models.CharField(max_length=64)
	email = models.CharField(max_length=64)
	mobileno = models.CharField(max_length=10)

	def __str__(self):
		return f"{self.username} ({self.password}) ({self.address}) ({self.email}) ({self.mobileno}) "

class Category(models.Model):
	name = models.CharField(max_length=64)
	des = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name} ({self.des})"

class Item(models.Model):
	name = models.CharField(max_length=64,default=1)
	price = models.CharField(max_length=64,default=1)
	img = models.ImageField(upload_to = "gallery",default=1) 
	# img = models.ImageField(upload_to = "groceryapp/static/img/",default=1) 
	weight = models.CharField(max_length=64,default=1)
	weightunit = models.CharField(max_length=64,default=1)
	description = models.CharField(max_length=64,default=1)

	category = models.ForeignKey(Category,default=1,on_delete=models.CASCADE)

	# iname = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="brandname")
	# iprice = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="brandprice")
	# ides = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="branddes")

	def __str__(self):
		return f"{self.name} ({self.price}) ({self.weight}) ({self.description}) ({self.weightunit})"

class Order(models.Model):
	name = models.CharField(max_length=64,default=1)
	price = models.CharField(max_length=64,default=1)
	# user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
	user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} ({self.price})"

class Orderdone(models.Model):
	item_name = models.CharField(max_length=64,default=1)
	item_price = models.CharField(max_length=64,default=1)
	name = models.CharField(max_length=64,default=1)
	mobile = models.CharField(max_length=64,default=1)
	houseNo = models.CharField(max_length=64,default=1)
	street = models.CharField(max_length=64,default=1)
	session_name = models.CharField(max_length=64,default=1)

	user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.item_name} ({self.item_price}) ({self.name}) ({self.mobile}) ({self.houseNo}) ({self.street})"
# Create your models here.
# Create your models here.
