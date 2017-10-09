# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from highcharts.views import HighChartsBarView
import numpy as np
import matplotlib.pyplot as plt


from .models import Question
from .models import PollutionByCountry

class ResultEntry:
    def __init__(self, mean_value):
        self.mean_value = mean_value
        self.pollution_list_text = ''

def index(request):
    output = '<!-- this is UTF-8 --><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><form name="form" method="post" action="/polls/test2/">State: <input type="text" name="state" /> <br>Year: <input type="text" name="year" /> <br><input type="submit" name="button" value="request" />&nbsp;&nbsp;</form>'
    return HttpResponse(output)

    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {
    #    'latest_question_list': latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))

    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt 
def myrequest(request, myrequest):
    #output = ''
    output = '<!-- this is UTF-8 --><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
    if request.method == "POST":
        # do something
        #output = 'This is request'
        #output = myrequest
        state_name = request.POST.get('country', '')
        year_str = request.POST.get('year', '')
        if state_name == '':
            state_name ='California'
        if year_str == '':
            year_str = '2012'
        #result_list1 = PollutionByCountry.objects.filter(pub_date__year=year_str)
        result_list1 = PollutionByCountry.objects.filter(country_name=state_name)
        result_list2 = result_list1.filter(pub_date__year=year_str)
        #result_list1 = PollutionByCountry.objects.get(id=1)

        #output = str(len(result_list1))
        for each_entry in result_list2:
            output = output + each_entry.city_name + '<br>'
            #output = each_entry.city_name + ' ' + each_entry.pollution + '<br>'
        
        #output = state_name+year_str+str(result_list2[0].pub_date)
    return HttpResponse(output)


@csrf_exempt 
def test2(request, test2):
    output = '<!-- this is UTF-8 --><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
    if request.method == "POST":
        # do something
        state_name = request.POST.get('state', '')
        year_str = request.POST.get('year', '')
        if state_name == '':
            state_name ='California'
        if year_str == '':
            year_str = '2012'
        result_list1 = PollutionByCountry.objects.filter(country_name=state_name)
        result_list2 = result_list1.filter(pub_date__year=year_str)
        mean_value = 0
        counter = 0

        data_list = []
        for each_entry in result_list2:
            data_list.append(each_entry.pollution)

        data = np.array(data_list)
        B=plt.boxplot(data)
        low = B['whiskers'][0].get_ydata()[1]
        q1 = B['whiskers'][0].get_ydata()[0]
        medium = np.median(data)
        q3 = B['whiskers'][1].get_ydata()[0]
        high = B['whiskers'][1].get_ydata()[1]
        pollution_list_text = str(low) + ', ' + str(q1) + ', ' + str(medium) + ', ' + str(q3) + ', ' + str(high)

        mean_value = medium

        #pollution_list_text = str(len(result_list1)) + ', ' +  str(len(result_list2))
        #pollution_list_text = ''
        #for each_entry in result_list2:
        #    mean_value = mean_value + each_entry.pollution
        #    if counter == 0:
        #        pollution_list_text = str(each_entry.pollution)
        #    else:
        #        pollution_list_text = pollution_list_text + ', ' + str(each_entry.pollution)       
        #    counter = counter + 1
            
        #if counter > 0:
        #    mean_value = mean_value/counter

        #####################
        # templates method
        #template = loader.get_template('polls/test2.html')
        #context = {
        #    'result_list2': result_list2,
        #}
        #return HttpResponse(template.render(context, request))
        #####################
        result_entry = ResultEntry(mean_value)
        result_entry.pollution_list_text = pollution_list_text
        result_entry.state_name_year = state_name + '_' + year_str
        template = loader.get_template('polls/test2.html')
        context = {
            'result_entry': result_entry,
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(output)



def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


