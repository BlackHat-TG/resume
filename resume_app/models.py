from django.db import models


class basic_info(models.Model):
	id = models.BigAutoField(primary_key = True)
	name = models.CharField(max_length=20)
	mobile_number = models.CharField(max_length=10)

class personal(models.Model):
	id = models.ForeignKey(basic_info,on_delete=models.CASCADE,primary_key=True,unique=True)
	email = models.EmailField()
	dob = models.DateField()
	gender = models.CharField(max_length=5)
	Address_line1 = models.CharField(max_length=100)
	Address_line2 = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	pincode = models.CharField(max_length=50)

class rlogin(models.Model):
	id = models.BigAutoField(primary_key = True)
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=10)


	def __str__(self):
		return self.username