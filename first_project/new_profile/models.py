from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=264)
	last_name = models.CharField(max_length=264)
	email = models.EmailField(max_length = 254)
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.email


class User_Data(models.Model):
	reg_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=264)
	last_name = models.CharField(max_length=264)
	father_name = models.CharField(max_length=264)
	email = models.EmailField(max_length = 254)
	gender = models.BooleanField()
	mobile = models.IntegerField() 
	dob = models.DateField()
	address = models.CharField(max_length=264)
	id_proof = models.CharField(max_length=264)
	id_proof_no = models.IntegerField()
	reg_date = models.DateField()
	file = models.ImageField(upload_to='user_image')
	due = models.IntegerField() 
	status = models.CharField(max_length=264)

	def __str__(self):
		return self.first_name

class Bill_Data(models.Model):
	reg_id = models.ForeignKey(User_Data, on_delete = models.CASCADE) 
	batch = models.CharField(max_length=264)
	amount = models.IntegerField() 
	rec_no = models.IntegerField() 
	rec_date = models.DateField()
	start_on = models.DateField()
	end_on = models.DateField()
	days = models.IntegerField()

	def __str__(self):
		return str(self.rec_no)

