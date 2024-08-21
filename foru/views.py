from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersForm
from service.models import Service
from news.models import News
from contactenquiry.models import contactEnquiry
from django.core.paginator import Paginator 
def homepage(request):
    newsdata=News.objects.all();
    raw={
        'title':'HOME PAGE',
        'heading1':'Welcome to My Page',
        'heading2':'This is the course section',
        'mylist':['Django','PHP','C#','Python','C++'],
        'digits':[10,20,30,40,50,60,70],
        'enroll_detail':[
            {'name':'ubaid','cell':92367891011,'age':20},
            {'name':'baidu','cell':92312131415,'age':25}
        ],
        'newsdata':newsdata
        }
    return render(request,"homepage.html",raw)
def newsDetail(request,slug):
    newsDetail=News.objects.get(news_slug=slug)
    data={
        'newsDetail':newsDetail
    }
    return render(request,"news.html",data)
def aboutus(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"aboutus.html",{'output':output})
def services(request):
    serviceData=Service.objects.all()
    pag=Paginator(serviceData,2)
    page_no=request.GET.get('page')
    serviceDatafinal=pag.get_page(page_no)
    totalpage=serviceDatafinal.paginator.num_pages
    #.order_by('-service_title')[2:5]
    #if request.method=="GET":
     #   sd=request.GET.get('servicename')
      #  if sd!=None:
       #     serviceData=Service.objects.filter(service_title__icontains=sd) 
    data={
        'serviceData':serviceDatafinal,
        'lastpage':totalpage,
        'totalpagelist':[n+1 for n in range(totalpage)]
    }
    return render(request,"service.html",data)
def submitform(request):
    finalans=0
    data={}
    try:
        if request.method=="POST":
            n1=int(request.POST['portion1'])
            n2=int(request.POST['portion2'])
            #n1=int(request.POST.get('portion1'))
            #n2=int(request.POST.get('portion2'))
            finalans=n1+n2
            data={
                #'a':n1,
                #'b':n2,
                'output':finalans
            }
            return HttpResponse(finalans,data)
    except:
        pass        
    return HttpResponse(request)
def contactUs(request):
    return render(request,"contactus.html")
def saveForm(request):
    para=''
    if request.method=="POST":
        naam=request.POST.get('name')
        mail=request.POST.get('email')
        nmbr=request.POST.get('phone')
        sitename=request.POST.get('websitename')
        msg=request.POST.get('message')
        result=contactEnquiry(name=naam,email=mail,phone=nmbr,websitename=sitename,message=msg)
        result.save()
        para="Thanks for submit your form"
    return render(request,"contactus.html",{'sol':para})
def courses(request):
    return HttpResponse('<b>We teach python and java courses on weakend.</b>')
def coursedetail(request,courseid):
    return HttpResponse(courseid)
def calculator(request):
    m=0
    values={}
    try:
        if request.method=="POST":
          m1=eval(request.POST.get('no1'))
          m2=eval(request.POST.get('no2'))
          opr=request.POST.get('opr')
          if opr=="+":
            m=m1+m2
          elif opr=="-":
            m=m1-m2
          elif opr=="*":
            m=m1*m2
          elif opr=="/":
            m=m1/m2
        values={
            'm1':m1,
            'm2':m2,
            'm':m
        }
    except:
        m="Invalid opr....."    
        print(m)
    return render(request,"calculator.html",values)
def viewevenodd(request):
    e=''
    if request.method=="POST":
        if request.POST.get('no1')=="":
            return render(request,"evenodd.html",{'error':True})
        M=eval(request.POST.get('no1'))
        if M%2==0:
            e="EVEN NUMBER"
        else:
            e="ODD NUMBER"
    return render(request,"evenodd.html",{'e':e})
def marksheet(request):
    if request.method=="POST":
        s1=eval(request.POST.get('sub1'))
        s2=eval(request.POST.get('sub2'))
        s3=eval(request.POST.get('sub3'))
        s4=eval(request.POST.get('sub4'))
        s5=eval(request.POST.get('sub5'))
        t=s1+s2+s3+s4+s5
        p=t*100/500;
        if p>=70:
            d="FITST DIVISION"
        elif p>=50:
            d="SECOND DIVISION"
        elif p>=35:
            d="THIRD DIVISION"
        else:
            d="FAIL"    
        value={
            'total':t,
            'per':p,
            'div':d
        }
        return render(request,"marksheet.html",value)
    return render(request,"marksheet.html")
def userForm(request):
    finalans=0
    fn=usersForm()
    data={'form':fn}
    try:
       if request.method=="POST":
       # n1=int(request.GET['portion1'])
       # n2=int(request.GET['portion2'])
          n1=int(request.POST.get('portion1'))
          n2=int(request.POST.get('portion2'))
          finalans=n1+n2
          data={
              'form':fn,
             # 'a':n1,
              #'b':n2,
              'output':finalans
            }
          url="/about-us/?output={}".format(finalans)
          return redirect(url)
    except:
           pass    
    return render(request,"userform.html",data)