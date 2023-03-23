from django.shortcuts import render
from django.http import HttpResponse
from .crawler import crawl

# Create your views here.
def termin(request):
	url =  request.GET['url']
	crawledData = crawl(url)
	# crawledData = {'divtext': 'divtext', 'start_date': 'nn', 'end_date': 'nn', 'url': url}
	return render(request, 'termin.html',{'crawledData': crawledData})