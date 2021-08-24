from django.shortcuts import render, redirect
from django.http import HttpResponse
from LMList.models import Personalinfo, Admin
from django.views.decorators.csrf import csrf_exempt

def home_page(request):
	return render(request,'homepage.html')

def update(request):
	return render(request,'Ainfo edit.html')

def ulogin(request):
	return render(request,'Ulogin.html')

def uregister(request):
	return render(request,'Uregister.html')

def user_log(request): 
  if request.method == 'POST':
        if Personalinfo.objects.filter(uusername=request.POST['puser'], upassword=request.POST['ppass']).exists():
            personalinfo_ = Personalinfo.objects.get(uusername=request.POST['puser'], upassword=request.POST['ppass'])
            return redirect(f'{personalinfo_.id}/user_status')

        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'Ulogin.html', context)

def aaccount(request):
    admins = Admin.objects.all()
    return render(request, 'Alogin.html', {'admins' : admins})



def reg_list(request ):
	personalinfos = Personalinfo.objects.all()
	return render(request, 'personal info.html', {'personalinfos' : personalinfos})

def adminn_list(request ):
	personalinfos = Personalinfo.objects.all()
	return render(request, 'admin.html')

def admin_log(request): 
 if request.method == 'POST':
        if Admin.objects.filter(ausername=request.POST['username'], apassword=request.POST['password']).exists():
            admin_ = Admin.objects.get(ausername=request.POST['username'], apassword=request.POST['password'])
            return redirect(f'/applicant')

        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'Alogin.html', context)

def new_list(request):                                                            
    spersonalinfo = Personalinfo.objects.create(qfull_name=request.POST['name'],qaddress=request.POST['add'],qage=request.POST['age'],qemail=request.POST['email'] ,qnumber=request.POST['number'], gfile=request.POST['nfile'],uusername=request.POST['puser'],upassword=request.POST['ppass']) 
    return redirect(f'/uregister')


def last_list(request ):
  	return render(request, 'LAST.html' )

def applicant_list(request ):
  	return render(request, 'personal info.html' )

def about_list(request ):
  	return render(request, 'about.html' )

def admin_list(request ):
  	return render(request, 'admin.html' )

def contact_list(request ):
  	return render(request, 'CONTACT.html' )

def login_list(request ):
  	return render(request, 'Alogin.html' )

def applicantinfo_list(request ):
  	return render(request, 'applicantinfo.html' )



def table_list(request ):
	personalinfos = Personalinfo.objects.all()
	return render(request, 'table.html', {'personalinfos' : personalinfos})


def edit(request, id):
	personalinfos = Personalinfo.objects.get(id=id)
	context = {'personalinfos':personalinfos}
	return render (request, 'Ainfo edit.html',context)

def update(request, id):
	personalinfo = Personalinfo.objects.get(id=id)
	personalinfo.qfull_name = request.POST['name']
	personalinfo.qbirthday = request.POST['DOBirth']
	personalinfo.qage = request.POST['age']
	personalinfo.qaddress = request.POST['add']
	personalinfo.qemail = request.POST['email']
	personalinfo.qnumber = request.POST['number']
	personalinfo.gstatus= request.POST['martial']
	personalinfo.gprimary_level = request.POST['primary']
	personalinfo.gsecondary_level = request.POST['secondary']
	personalinfo.gsecondary_level = request.POST['tertiary']
	personalinfo.save()
	return redirect('/admin')




def delete(request, id):
	personalinfo = Personalinfo.objects.get(id=id)
	personalinfo.delete()
	return redirect('/admin')

def logoutUser(request):
	logout(request)
	return redirect('login')

def home_page(request):
    return render(request, 'homepage.html')


def applicant_status(request):
    personalinfos = Personalinfo.objects.all()
    return render(request, 'Ainfo.html', {'personalinfos' : personalinfos})


def statusupdate(request,personalinfo_id):
    personalinfo = Personalinfo.objects.get(id=personalinfo_id)
    personalinfo.gstatus= request.POST['ggstatus']
    personalinfo.save()   
    return render(request, 'Ainfo.html')
    #return redirect(f'/applicant_status')

def applicant_list(request):
    personalinfos = Personalinfo.objects.all()
    return render(request, 'Atable.html', {'personalinfos' : personalinfos})
 


def user_status(request, personalinfo_id):
	personalinfo_ = Personalinfo.objects.get(id=personalinfo_id)
	return render(request, 'Uinfo.html', {'personalinfo': personalinfo_})






