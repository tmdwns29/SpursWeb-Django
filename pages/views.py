from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def product(request):
    return render(request, 'product/content_list.html')
# Create your views here.
