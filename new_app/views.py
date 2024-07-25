from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from DEV.settings import EMAIL_HOST_USER
from new_app.models import Contact

def index(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        course_select=request.POST.get('course-select')
        message=request.POST.get('message')

        en=Contact(name=name,email=email,course=course_select,phone_number=mobile,message=message)
        # en.save()

        data ={
            'name':name,
            'email':email,
            'mobile':mobile,
            'course_select':course_select,
            'message':message
        }
        all_message='''
            For Course :{}

            From : {}

            Mobile Number : {}

            Enquiry : {}
        '''.format(data['course_select'],data['email'],data['mobile'],data['message'])

        send_mail(data['course_select'],all_message,EMAIL_HOST_USER,[EMAIL_HOST_USER],fail_silently=False,)
        en.save()
    return render(request,"index.html")

def courses(request):
    return render(request,"courses.html")

def contact_email(request):
    pass

def ft_courses(request):
    return render(request,"fameux-courses.html")

def about_us(request):
    return render(request,"about-us.html")

def bca_course(request):
    return render(request,"course_pages/BCA.html")

def bcom_course(request):
    return render(request,"course_pages/B-COM.html")

def ba_course(request):
    return render(request,"course_pages/BA.html")

def mcom_course(request):
    return render(request,"course_pages/M-COM.html")

def bba_course(request):
    return render(request,"course_pages/BBA.html")

def mca_course(request):
    return render(request,"course_pages/MCA.html")

def mba_courses(request):
    return render(request,"MBA-courses.html")

def data_science(request):
    return render(request,"FT_courses/data_science.html")

def digital_marketing(request):
    return render(request,"FT_courses/digital_marketing.html")

def product_management(request):
    return render(request,"FT_courses/product_management.html")

def web_development(request):
    return render(request,"FT_courses/web_development.html")

def java_fullstack(request):
    return render(request,"FT_courses/java_fullstack.html")

def ccna(request):
    return render(request,"FT_courses/ccna.html")

def cyber_security(request):
    return render(request,"FT_courses/cyber_security.html")

def cloud_computing(request):
    return render(request,"FT_courses/cloud_computing.html")



