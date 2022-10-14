from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from.forms import AlbumForm
from django.views import View
class CreateView(View):
    template_name = 'createAlbum.html'

    def get(self, request, *args, **kwargs):
        form = AlbumForm()
        context = {'form' : form}
        return render(request,self.template_name,context)
    
    def post(self, request, *args, **kwargs):
        form = AlbumForm()
        if(request.method == "POST"):
            form = AlbumForm(request.POST)
            if form.is_valid():
                form.save()
        context = {'form' : form}
        return render(request,self.template_name,context)

