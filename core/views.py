from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse

from .forms import UrlInputForm
from .models import Url

# render the home page which contain the form to shorten url
class HomePageView(View):
    
    def get(self, request):
        form = UrlInputForm()
        context = {"form": form}
        template = "home.html"
        return render(request,template,context)

    def post(self, request):
        form = UrlInputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            url = form.save()
            template = "success.html"
            context = {'shorten_hash': url.shorten_hash, 'target_url': url.target_url}
            return render(request, template, context)
        return render(request, "fail.html")

# redirect to target url with the hash as url param
class ShortenUrlView(View):
    def get(self, request, shorten_hash):
        #TODO: redirect to home page with error message
        url = get_object_or_404(Url, shorten_hash=shorten_hash)
        target_url = url.target_url
        return redirect(target_url)
