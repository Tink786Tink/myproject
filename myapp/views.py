import random

from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import auth
from django.core.serializers import serialize
from django.db.models.fields import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate

from myapp.models import CustomUser


# Create your views here.


def welcome_page(request):
    return render(request, 'result.html')


def view_user_login(request):
    return render(request, 'userLogin.html')


def view_admin_login(request):
    return render(request, 'adminLogin.html')


def admin_login(request):
    if request.method == 'POST':
        username = str(request.POST['username'])
        password = str(request.POST['pass'])

        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_admin:
            print('OKKKKKKKKKK')
            print(user.username)
            auth.login(request, user)
            request.session['user_id'] = user.username
            return render(request, 'addUser.html')
        else:
            print('wrong cred')
            messages.error(request, 'username or password not correct')
            return render(request, 'adminLogin.html')
    else:
        return render(request, 'index.html')


def admin_logout(request):
    del request.session['user_id']
    auth.logout(request)
    return render(request, 'adminLogin.html')


def create_user(request):
    if request.method == 'POST':
        firstname = str(request.POST['firstname'])
        lastname = str(request.POST['lastname'])
        email = str(request.POST['email'])
        mobile = str(request.POST['contact'])
        birthday = str(request.POST['birthday'])
        username = firstname + '_' + lastname
        initialpass = firstname + str(random.randint(1000, 9999))
        # password = make_password(initialpass)
        print(username)
        print(initialpass)
        createuser = CustomUser.objects.create(username=username,
                                               first_name=firstname, last_name=lastname,
                                               email=email, password=initialpass, phone_number=mobile,
                                               birthday=birthday)
        createuser.save()
    return render(request, 'adminLogin.html')


def user_login(request):
    if request.method == 'POST':
        username = str(request.POST['username'])
        password = str(request.POST['pass'])

        # user = auth.authenticate(username=username, password=password)
        userdata = CustomUser.objects.filter(is_admin='False', username=username).values()
        print(userdata)
        # if user is not None and not user.is_admin:
        print(username)
        print(password)
        print(userdata[0]["password"])
        if userdata.exists() and userdata[0]["password"] == password:
            print('OKKKKKKKKKK  user')
            # auth.login(request, user)
            request.session['user_id_user'] = userdata[0]["username"]
            return render(request, 'homeAdmin.html')
        else:
            print('wrong cred')
            messages.error(request, 'username or password not correct')
            return render(request, 'userLogin.html')
    else:
        return render(request, 'index.html')


def create_user_view(request):
    return render(request, 'addUser.html')


def view_user(request):
    mydata = CustomUser.objects.filter(is_admin='False', is_superuser='False').order_by('-date_joined').values()
    context = {
        'mymembers': mydata,
    }
    return render(request, 'viewUser1.html', context)


def forgot_password(request):
    return render(request, 'forgotPassword.html')


def validate_forgot_password(request):
    if request.method == 'POST':
        userid = str(request.POST['userid'])
        birthday = str(request.POST['birthday'])
        mydata = CustomUser.objects.filter(is_admin='False', is_superuser='False', username=userid,
                                           birthday=birthday).values()
        if mydata.exists():
            print("Valid User")
            username = mydata[0]["username"]
            context = {
                'user_name': username,
            }
            return render(request, 'forgotPwdInput.html', context)
        else:
            print("no dataaaaaaa")
            messages.error(request, 'Invalid User name or Birth date')
            return render(request, 'forgotPassword.html')


def change_password(request):
    if request.method == 'POST':
        username = str(request.POST['username'])
        password = str(request.POST['password'])
        confirm_password = str(request.POST['confirm_password'])
        record = CustomUser.objects.get(username=username)
        record.password = make_password(password)
        record.save(update_fields=["password"])
        messages.info(request, 'Your password has been changed successfully')
        return render(request, 'userLogin.html')


def view_user_api(request):
    mydata = CustomUser.objects.filter(is_admin='False', is_superuser='False').order_by('-date_joined').values_list()
    print(list(mydata))
    # return render(request, 'viewUser1.html', context)
    # values_list("username","first_name")

    # data = [user.get_data() for user in mydata]
    # print(data)

    # data = serialize("json", mydata)

    response = {'data': mydata}
    print(response)
    return JsonResponse(response, safe=False)
# response = {'data':mydata}
# return JsonResponse(response,safe=False)
# return JsonResponse({"data": list(mydata)})
# return JsonResponse({"data": mydata})
