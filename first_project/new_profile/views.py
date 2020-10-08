from django.shortcuts import render, get_object_or_404, redirect
from new_profile import forms
from new_profile import models
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from datetime import date,datetime
from django.db.models import Sum
from dateutil.relativedelta import relativedelta
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

# function that convert Y-M-D date input string to date object
def html_to_model_date(date_str):
	d = list(map(int,date_str.split('-')))
	return date(d[0],d[1],d[2])

def number_to_month(month):
	months = ["January", "Febuary","March", "April", "May", "June", "July", "August",  "September", "October", "November", "December"]
	return months[month-1]

def get_last_months(start_date, months):
    for i in range(months):
        yield (start_date.year,start_date.month)
        start_date += relativedelta(months = -1)

def dashbord(request):
	today = date.today()
	bill = models.Bill_Data.objects
	member = models.User_Data.objects
	income = bill.filter(start_on__year=today.year, start_on__month=today.month)
	old_member = member.filter(reg_date__year=today.year, reg_date__month=today.month).count()
	gender = {'male':member.filter(gender=False).count(),'female':member.filter(gender=True).count()}
	earnings_months = [i for i in get_last_months(datetime.today(), 6)]
	earnings = []
	for year,month in earnings_months:
		earn_data = bill.filter(start_on__year=year, start_on__month=month)
		earn = earn_data.aggregate(sum=Sum('amount'))['sum']
		if earn==None:
			earn = 0
		earnings.append({'earn':earn,'month':number_to_month(month)})
	total = member.count()
	enable = member.exclude(status='3').count()
	active = member.filter(status='0').count()
	pactive = member.filter(status='1').count()
	inactive = member.filter(status='2').count()
	counter = {'total':total,'active':active,'enable':enable,'pactive':pactive,'inactive':inactive,'disable':total-enable}
	this_month = income.aggregate(sum=Sum('amount'))['sum']
	print(earnings)
	return render(request, 'dashbord.html',{'this_month':this_month,'count':income.count(),'old_count':old_member,'counter':counter,'gender':gender,'earnings':earnings})


def new_user(request):
	form = forms.User_Data_Form()
	form1 = forms.Bill_Data_Form()

	if request.method == "POST":
		form  = forms.User_Data_Form(request.POST, request.FILES)
		form1 = forms.Bill_Data_Form(request.POST)
			# form.save(commit=True)
		if form.is_valid():
			user = models.User_Data()
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.father_name = form.cleaned_data['father_name']
			user.email = form.cleaned_data['email']
			user.gender = form.cleaned_data['gender']
			user.mobile = form.cleaned_data['mobile']
			user.dob = form.cleaned_data['dob']
			user.address = form.cleaned_data['address']
			user.id_proof = form.cleaned_data['id_proof']
			user.id_proof_no = form.cleaned_data['id_proof_no']
			user.reg_date = "2019-10-10"
			myfile = request.FILES['file']
			fs = FileSystemStorage()
			filename = fs.save(None, myfile)
			uploaded_file_url = fs.url(filename)
			user.file = filename
			# print(type(myfile),"+++++++++++",filename,"***********",uploaded_file_url)
			# user.file = handle_uploaded_file(request.FILES['file'],user.reg_id)
			user.due = 0
			user.status= '2'
			user.save()
			print(form.cleaned_data['pay'])
			if form.cleaned_data['pay']=='0' and form1.is_valid():
				bill = models.Bill_Data()
				bill.reg_id = user
				bill.batch = form1.cleaned_data['batch']
				bill.amount = form1.cleaned_data['amount']
				if form1.cleaned_data['due']=='':
					user.due = 0
				else:
					user.due = form1.cleaned_data['due']
				bill.rec_no = form1.cleaned_data['rec_no']
				bill.rec_date = form1.cleaned_data['rec_date']
				bill.start_on = form1.cleaned_data['start_on']
				bill.end_on = form1.cleaned_data['end_on']
				dayss = bill.end_on-date.today()
				bill.days = dayss.days
				bill.save()

			user.save()
			return redirect('members')
		else:
			print("+++++",form.errors,"+++++\n")
			# print(form1.errors)
			print("ERROR form")
	else:
		print("no request")
		# if form1.is_valid():
		# 	print("bill_form")
		# 	print("SuCCESS")
		# else:
		# 	print(form1.errors)
		# 	print("ERROR form1")

	return render(request,'new_profile.html',{'form':form,'form1':form1})


def members(request, order=0):
	member_list = models.User_Data.objects.order_by('first_name')
	# for objects in models.User_Data.objects:
	# TO-DO
	print(order)
	# due days calculate
	for x in member_list:
		objs = models.Bill_Data.objects.filter(reg_id = x).order_by('-rec_no')
		if objs.count()<=0:
			x.status = '2'
			continue
		obj = objs[0]
		days = obj.end_on-date.today()
		obj.days = days.days
		if x.status != '3':
			if obj.days<0:
				x.status = '2'
			else:
				if x.due>0:
					x.status = '1'
				else:
					x.status = '0'
		print(order)
		obj.save()
		x.save()
	# print(models.User_Data.objects.get(reg_id=2))s
	# print(models.User_Data.objects)
	return render(request, 'members.html',{'members':member_list})

def view_profile(request,pk):
	member = get_object_or_404(models.User_Data,pk=pk)
	bills = models.Bill_Data.objects.filter(reg_id = pk)
	if bills.count()<=0:
			bill = {'null':"empty"}
	else:
		bill = bills.order_by('-rec_no')[0]

	message = ""
	male = ""
	female = ""
	if not member.gender:
		male = "checked"
	else:
		female = "checked"
	if request.method == "POST" and "file_save" not in request.POST :
		member.first_name = request.POST['first_name']
		member.last_name = request.POST['last_name']
		member.father_name = request.POST['father_name']
		member.email = request.POST['email']
		member.first_name = request.POST['first_name']
		member.gender = request.POST['gender']
		member.mobile = request.POST['mobile']
		member.dob = html_to_model_date(request.POST['dob'])
		member.id_proof = request.POST['id_proof']
		member.address = request.POST['address']
		member.id_proof_no = request.POST['id_proof_no']
		member.save()
		message = "show"
		data = {'percent':100-(bill.days*100/31),'male':male,'female':female,'message':message}
		return render(request, 'view_update.html',{'member':member,'bill':bill,'bills':bills,'data':data})
	elif request.method == "POST" and "file_save" in request.POST:
		myfile = request.FILES['file']
		fs = FileSystemStorage()
		filename = fs.save(None,myfile)
		member.file = filename
		member.save()
		return redirect('member',pk=pk)
	else:
		message = "hidden"
		data = {'percent':100-(bill.days*100/31),'male':male,'female':female,'message':message}
	return render(request, 'view_update.html',{'member':member,'bill':bill,'bills':bills,'data':data})

def clear_due(request,pk):
	member = get_object_or_404(models.User_Data,pk=pk)
	member.due=0
	member.save()
	print(member.pk,"+++++++")
	return redirect('member',pk=pk)

def delete_receipt(request,pk):
	bill = get_object_or_404(models.Bill_Data,pk=pk)
	user = bill.reg_id
	bill.delete()
	return redirect('member',pk=user.pk)

def delete_member(request,pk):
	member = get_object_or_404(models.User_Data,pk=pk)
	member.delete()
	return redirect('members')

def update_receipt(request,pk):
	bill = get_object_or_404(models.Bill_Data,pk=pk)
	user = bill.reg_id
	if request.method == "POST":
		print(request.POST['bill_batch'])
		bill.batch = request.POST['bill_batch']
		bill.amount = request.POST['amount']
		if request.POST['due']=='':
			user.due = 0
		else:
			user.due = request.POST['due']
		bill.rec_no = request.POST['rec_no']
		bill.rec_date = request.POST['rec_date']
		bill.start_on = request.POST['start_on']
		bill.end_on = request.POST['end_on']
		bill.save()
		return redirect('member',pk=user.pk)
		
	due = user.due
	return render(request, 'update_receipt.html',{'bill':bill,'due':due})

def payment(request,pk):
	user = get_object_or_404(models.User_Data,pk=pk)
	bills = models.Bill_Data.objects.filter(reg_id = pk)
	bill = models.Bill_Data()
	if request.method == "POST":
		print(request.POST['bill_batch'])
		bill.reg_id = user
		bill.batch = request.POST['bill_batch']
		bill.amount = request.POST['amount']
		if request.POST['due']=='':
			user.due = 0
		else:
			user.due = request.POST['due']
		bill.rec_no = request.POST['rec_no']
		bill.rec_date = request.POST['rec_date']
		bill.start_on = request.POST['start_on']
		bill.end_on = request.POST['end_on']
		bill.days = 0
		bill.save()
		user.save()
		return redirect('member',pk=pk)

	return render(request, 'payment.html',{'member':user,'bills':bills})

def login(request):
	form = AuthenticationForm()
	return render(request, 'login.html',{"form":form})

def register(request):
	form = forms.MainUser()
	if request.method == "POST":
		form = forms.MainUser(request.POST)
			# form.save(commit=True)
		if form.is_valid():
			user = models.User()
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			pass1 = form.cleaned_data['password']
			pass2 = form.cleaned_data['password_repeat']
			if pass1!=pass2:
				return render(request, 'register.html',{'error':"Password not matched!"})
			user.save()
			
	return render(request, 'register.html')