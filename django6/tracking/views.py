from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .mixins import LogginMixin

class Home(LogginMixin,APIView):
    logging_methods = ['GET','POST']
    sensitive_fields = ['name']
    def should_log(self, request, response):
        return response.status_code>=100

    def get(self,request):
     
        return Response('hello')
    
