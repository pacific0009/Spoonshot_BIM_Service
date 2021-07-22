from django import views
from django.core.checks import messages
from django.db.models import base
from django.http.response import HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import BookInventory
import json, requests
from Spoonshot_BIM_Service.settings import GOOGLE_BOOKS_API_KEY, GOOGLE_BOOKS_BASEURL
# TODO: Handle error messages 

class BookInventoryListCreate(View):

    def get(self, request, *args, **kwargs):
        print('inside get')
        limit = 20 
        skip = 0
        result = BookInventory.objects.filter().all()[skip: skip+limit]
        response = [item.to_dict() for item in result]
        return JsonResponse({'items': response})

    def post(self, request, *args, **kwargs):

        # Read payload
        try:
            body = json.loads(request.body.decode("utf-8"))
        except Exception as e:
            print(e)
            return HttpResponseBadRequest()
        
        # The validatation can be applied by using serialisers or Pydentic Models can be used 
        # Implementing custom validator 
        def validate_mandate_field(data):
            mandatory_fields = set(['title', 'google_id'])
            missing_fields = set()
            for item in mandatory_fields:
                if not data.get(item): missing_fields.add(item)
            if missing_fields:
                return {"type": "missing_fields", 'messages':  f'missing required fields {missing_fields}'}

        badRequest = validate_mandate_field(body)
        if badRequest: return HttpResponseBadRequest(badRequest.get('messages'))

        new_book = BookInventory()
        new_book.title = body["title"]
        new_book.google_id = body["google_id"]
        if body.get('stock_count'): new_book.stock_count = body.get('stock_count') 
        
        try:
            new_book.save()
            # save_audit_log_history(data)
        except Exception as e:
            return HttpResponseBadRequest(e)

        return JsonResponse(status=201, data=new_book.to_dict())

class BookInventoryUpdate(View):
    def get(self, request, book_id):
        try:
            book = BookInventory.objects.get(id=book_id)
        except Exception as e:
            return HttpResponseBadRequest(e)
        return JsonResponse(book.to_dict())

    def put(self, request, book_id):

        # Read payload
        try:
            body = json.loads(request.body.decode("utf-8"))
        except Exception as e:
            print(e)
            return HttpResponseBadRequest()
        try:
            book = BookInventory.objects.get(id=book_id)
        except Exception as e:
            return HttpResponseBadRequest(e)

        if body.get('title'): book.title = body.get('title')

        # uncomment if needed  
        # if body.get('google_id'): book.title = body.get('title')
        # if body.get('active'): book.active = body.get('active')

        if body.get('stock_count'): book.stock_count = body.get('stock_count')
        
        # saving update
        book.save()

        # save_inventory_audit_log_history(data)
        return JsonResponse(book.to_dict())
    
    def delete(self, request, book_id):
        
        # Read payload
        try:
            body = json.loads(request.body.decode("utf-8"))
        except Exception as e:
            print(e)
            return HttpResponseBadRequest()
        try:
            book = BookInventory.objects.get(id=book_id)
        except Exception as e:
            return HttpResponseBadRequest(e)

        data = book.to_dict()
        if request.GET.get('hard'): 
            book.delete()
        else: 
            book.active = False
            book.save()
        
        return JsonResponse(data=data)

class BookInventoryGoogle(View):
    def get(self, request, google_id):
        try:
            book = BookInventory.objects.get(google_id=google_id)
        except Exception as e:
            return HttpResponseBadRequest(e)
        return JsonResponse(book.to_dict())

class GoogleBooks(View):
    def get(self, request):
        url = f'{GOOGLE_BOOKS_BASEURL}?api_key={GOOGLE_BOOKS_API_KEY}'
        for item in request.GET:
            url = url + '&{}={}'.format(item, request.GET.get(item))
        res = requests.get(url=url)
        return  JsonResponse(status=res.status_code, data=res.json())

class GoogleBooksDetails(View):
    def get(self, request, volume_id):
        url = f'{GOOGLE_BOOKS_BASEURL}/{volume_id}?api_key={GOOGLE_BOOKS_API_KEY}'
        print(url)
        res = requests.get(url=url)
        return  JsonResponse(status=res.status_code, data=res.json())



