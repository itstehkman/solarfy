from django.shortcuts import render
from django.http import HttpResponse
import django.template as template
from django.template import RequestContext, loader

# Create your views here.

#15 ppl
objectWithBillJson = {'json' :'{"0": ["250 FRANK H OGAWA PLZ STE 3341 ", 2019.17], "1": ["250 FRANK OGAWA PLAZA ", 1708.13], "2": ["250 FRANK OGAWA PLAZA ", 101.42], "3": ["250 FRANK H OGAWA PLZA ST 1329 ", 320.29], "4": ["250 FRANK H OGAWA PLZ STE 3341 ", 1046.54], "5": ["250 FRANK H OGAWA PLZA ST 1329 ", 159.72], "6": ["250 FRANK OGAWA PLAZA ", 1374.42], "7": ["250 FRANK H OGAWA PLZA ST 1329 ", 252.36], "8": ["PWA - PARKS 119M ", 685.3], "9": ["250 FRANK H OGAWA PLZA ST 1329 ", 618.48], "10": ["PWA - PARKS 176M ", 5770.9], "11": ["250 FRANK OGAWA PLAZA ", 30.72], "12": ["250 FRANK OGAWA PLAZA ", 559.01], "13": ["250 FRANK OGAWA PLZ ", 1420.6], "14": ["250 FRANK OGAWA PLAZA ", 1906.65]}' }

def index(request):
	template = loader.get_template('app/index.html')
	context = RequestContext(request, objectWithBillJson)
	return HttpResponse(template.render(context))