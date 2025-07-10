from django.shortcuts import render,  HttpResponse


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
     return render(
         request=request,
         template_name='website/index.html'
     )