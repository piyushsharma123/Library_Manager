from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']
class MainUser(forms.Form):
	first_name = forms.CharField(label='First Name',  widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(label='Last Name',  widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='Email',  widget=forms.TextInput(attrs={'class': 'form-control'}))
	# password = forms.Password(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	# password_repeat = forms.Password(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class User_Data_Form(forms.Form):
	GENDER_CHOICES=[('0',"Male"),('1',"Female")]
	first_name = forms.CharField(label='First Name',  widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(label='Last Name',  widget=forms.TextInput(attrs={'class': 'form-control'}))
	father_name = forms.CharField(label="Father's Name",  widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='Email',  widget=forms.TextInput(attrs={'class': 'form-control'}))
	gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER_CHOICES,attrs={'class': 'form-check-input'}))
	mobile = forms.IntegerField(label='Mobile',  widget=forms.TextInput(attrs={'class': 'form-control'}))
	dob = forms.DateField(label='Date of birth',  widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
	address = forms.CharField(label='Address',  widget=forms.TextInput(attrs={'class': 'form-control'}))
	id_proof = forms.ChoiceField(label='ID Proof',  widget=forms.Select(attrs={'class': 'form-control'}),choices=[('0',"Addhar"),('1',"Voter ID"),('2',"Driving Licence")])
	id_proof_no = forms.CharField(  widget=forms.TextInput(attrs={'class': 'form-control'}))
	reg_date = forms.DateField(label='Registration Date',  widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
	pay = forms.CharField(widget=forms.RadioSelect(choices=[('0',"Pay Now"),('1',"Pay Later")],attrs={'class': 'form-check-input'}))
	file = forms.ImageField(label="Choose Image",widget=forms.ClearableFileInput(attrs={'accept':'image/*','class': 'border rounded shadow inputfile'}))

class Bill_Data_Form(forms.Form):
	BATCH_CHOICES=[('0','Morning'),('1','Evening'),('2',"Full-Day")]
	batch = forms.CharField(label='batch', widget=forms.RadioSelect(choices=BATCH_CHOICES,attrs={'class': 'form-check-input'}))
	amount = forms.IntegerField(label='Amount',  widget=forms.TextInput(attrs={'class': 'form-control'}))
	due = forms.IntegerField(label='Due',  widget=forms.TextInput(attrs={'class': 'form-control'}))
	rec_no = forms.IntegerField(label='Receipt Number',  widget=forms.TextInput(attrs={'class': 'form-control'}))
	rec_date = forms.DateField(label='Receipt Date',  widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
	start_on = forms.DateField(label='Start On',  widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
	end_on = forms.DateField(label='End On',  widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
