import datetime
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('home/home.html')


def apiSample(request):
    utc_datetime = datetime.datetime.utcnow()
    formated_string = utc_datetime.strftime("%Y-%m-%d %H:%M:%SZ")
    data = {'SERVERTIME-UTC': formated_string}
    return HttpResponse(json.dumps(data), content_type="application/json")