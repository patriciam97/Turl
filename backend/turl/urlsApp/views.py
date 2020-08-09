from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from .models import Entry


def index(request):
    return HttpResponse("Hello, world. You're at the urlsApp index.")


@csrf_exempt
def get(request, path_id):
    if request.method == 'GET':
        try:
            path_id = int(path_id)
            entry = Entry.objects.get(path=path_id)
            return redirect(entry.link)
        except Entry.DoesNotExist:
            return JsonResponse({
                'status_code': 404,
                'error': 'The resource was not found'
            })
