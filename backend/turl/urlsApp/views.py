from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import json
from .models import Entry


def index(request):
    return HttpResponse("Hello, world. You're at the urlsApp index.")


@csrf_exempt
def get(request, path_id):
    if request.method == 'GET':
        try:
            path_id = str(path_id)
            entry_id = path_id[-2:]
            path_id = int(path_id[:-2])
            print(entry_id, path_id)
            entry = Entry.objects.get(entry_id=entry_id)
            print(entry.link)
            return redirect(entry.link)
            # if (entry.link.startswith("http://") or entry.link.startswith("https://")):
            #     print("h2: "+entry.link)
            #     # return redirect(url)
            # else:
            #     print("h1 http://"+entry.link)
            #     # return redirect("http://"+url)
            return JsonResponse({
                'status_code': 404,
                'error': 'The resource was not found'
            })
        except Entry.DoesNotExist:
            return JsonResponse({
                'status_code': 404,
                'error': 'The resource was not found'
            })
        except:
            return JsonResponse({
                'status_code': 505,
                'error': 'Internal Server Error'
            })
    # elif request.method == 'POST':
    #     return JsonResponse({
    #         'status_code': 200,
    #         'request': request
    #     })


@csrf_exempt
def post(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        link = str(body["link"])
        if (not link.startswith('http://') and not link.startswith('https://')):
            link = "http://"+link
        link = link.replace("https", "http")
        if (not link[7:10] == "www"):
            link = "http://www."+link[7:]
        try:
            entry = Entry.objects.get(link=link)
            return JsonResponse({
                'status_code': 200,
                'saved': "already exists",
                'url': "http://127.0.0.1:8000/urls/"+entry.path+str(entry.entry_id)
            })
        except Entry.DoesNotExist:
            entry = Entry.objects.create(link=link)
            entry.save()
            return JsonResponse({
                'status_code': 200,
                'saved': "true",
                'url': "http://127.0.0.1:8000/urls/"+entry.path+str(entry.entry_id)
            })
