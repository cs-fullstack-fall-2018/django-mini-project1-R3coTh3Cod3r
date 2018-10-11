from django.http import HttpResponse
from .models import TimePunch
from django.template import loader

def Name(request, name):
    return HttpResponse("Hello what is your name %s." % name)
def School(request, school):
    return HttpResponse("Hello what is your name %s." % school)

def Hour(request, hour):
    return HttpResponse("What is your hours?%s" % hour)

def DateofWork(request, dateofwork):
    return HttpResponse("What day was it?%s" % dateofwork)

def DateofEntry(request,dateofentry ):
    return HttpResponse("Give the current date.%s" % dateofentry)

def index(request):
    latest_question_list = TimePunch.objects.order_by('-pub_date')[:5]
    template = loader.get_template('timecard_app/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))