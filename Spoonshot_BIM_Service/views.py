from django.views import View
from django.http import HttpResponse, JsonResponse

class Health(View):
    def get(self, request):
        return JsonResponse({'message': 'All Good'})

