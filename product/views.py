from django.shortcuts import render
from.models import MainContent

def index(request):
    content_list = MainContent.objects.order_by('-pub_date') # '-':역순(최신콘텐츠 상단 노출)
    context = {'content_list':content_list}
    return render(request, 'product/content_list.html', context)