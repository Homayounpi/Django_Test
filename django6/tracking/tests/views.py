from rest_framework.views import APIView
from rest_framework.response import Response
from tracking.mixins import LogginMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


class MockNoLogginView(APIView):
    def get(self,request):
        return Response('no Logging')

class MockLoggingView(LogginMixin,APIView):
    def get(self,request):
        return Response('with logging')

class MockExplicitLoggingView(LogginMixin,APIView):
    logging_methods = ["POST"]

    def get(self,request):
        return Response('no logging')

    def post(self,request):
        return Response('with logging')
    

class MockCustomCheckLoggingView(LogginMixin,APIView):
    def should_log(self, request, response):
        return 'log' in response.data

    def get(self,request):
        return Response('with log')
    
    def post(self,request):
        return Response('no recording')

class MockSessionAuthLoggingView(LogginMixin,APIView):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        return Response('with session auth logging')

class MockSensitiveFieldsLoggingView(LogginMixin,APIView):
    sensitive_fields = {'mY_fiEld'}

    def get(self,request):
        return Response('with logging')

class MockInvalidCleanedSubstituteLoggingView(LogginMixin,APIView):
    CLEANED_SUBSTITUTE = 1
   


