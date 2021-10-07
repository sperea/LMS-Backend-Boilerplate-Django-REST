# Create your views here.
import json
from django.http import HttpResponse
from django.views import View
# from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
#from rest_framework_simplejwt.authentication import TokenAuthentication
from rest_framework.authentication import TokenAuthentication

class ViewWrapper(APIView):
    # we have created a view wrapper
    # to hide format details and decouple
    # our views from the framework
    view_factory = None

    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        body, status = self.view_factory.create(request).get(**kwargs)

        return HttpResponse(json.dumps(body), status=status,
                            content_type='application/json')

    def post(self, request, *args, **kwargs):
        #print(str(**kwargs))
        body, status = self.view_factory.create(request).post(**kwargs)

        return HttpResponse(json.dumps(body), status=status,
                            content_type='application/json')