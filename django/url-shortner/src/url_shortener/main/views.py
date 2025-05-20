from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import URLMap
from .forms import URLShortenForm

def home_view(request):
    form = URLShortenForm()
    shortened_url_onj = None

    if request.method == 'POST':
        if form.is_valid():
            og_url = form.cleaned_data['original_url']
            url_map_instance, created = URLMap.objects.get_or_create(original_url=og_url)

    context = {
        'form' : form,
        'shortened_url_obj' : url_map_instance,
    }

    return render(request, 'main/home.html', context)


def redirect_to_original_url(request, short_code):
    url_map = get_object_or_404(URLMap,short_code=short_code)
    return redirect(url_map.original_url)