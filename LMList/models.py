from django.db import models


class Personalinfo(models.Model):
	qfull_name = models.TextField(max_length=120, default='')
	qaddress = models.TextField(max_length=10, default='')
	qage= models.IntegerField( default='')
	qemail= models.TextField(max_length=20, default='')
	qnumber= models.TextField(max_length=20, default='')
	gfile = models.FileField(default='')
	gstatus = models.TextField(default='')
	uusername = models.TextField(max_length=120, default='')
	upassword = models.TextField(max_length=120, default='')

	class meta:
		db_table = "background"


class Admin(models.Model):
	ausername = models.TextField(max_length=120, default='')
	apassword = models.TextField(max_length=120, default='')

	class meta:
		db_table = "zadmin"


'''
class Educationalbackground(models.Model):
	gprimary_level = models.TextField(max_length=50,default='')
	gsecondary_level = models.TextField(max_length=50,default='')
	gtertiary_level= models.TextField(max_length=50,default='')
	personal = models.ForeignKey(Personal_Info, default=None, on_delete=models.CASCADE)
	class meta:
		db_table = "background"



class List(models.Model):
    npet = models.TextField(default='')
    nname = models.TextField(default='')


class Item(models.Model):
    npet = models.TextField(default='')
    nname = models.TextField(default='')
    nAddress = models.TextField(default='')
    nBreed = models.TextField(default='')
    nDay = models.TextField(default='') 
    list = models.ForeignKey(List, default=None, on_delete=models.PROTECT)'''

