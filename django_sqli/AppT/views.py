from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponse
from .models import Prod

# Create your views here.
def vul_view(request):
    #fild name get
    field = request.GET.get('field', 'title')

    try:
        queryset = Prod.objects.annotate(**{field: Count("title")})

        data = ""
        for item in queryset:
            data += f"<h2>{item.title}</h2>"
        return HttpResponse(data)
    except Exception as e:
        return HttpResponse(f"<pre>Error: {e}</pre>", status=500)