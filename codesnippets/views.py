from django.http import Http404, HttpResponse

from django.shortcuts import redirect, render

from django.views.generic import DetailView, ListView

from .models import CodeSnippet
from .forms import CodeForm

class CodeListView(ListView):
    model = CodeSnippet
    template_name = 'code/index.html'

class CodeDetailView(DetailView):
    model = CodeSnippet
    template_name = 'code/detail.html'

def add(request):

    if request.method == 'POST':
        # First, assert all keys are present. This is already tedious--
        #   imagine how bad it gets when we want granular information
        #   on missing submissions.

        form = CodeForm(request.POST)
        if form.is_valid(): 
            CodeSnippet(
             snippet=form.cleaned_data['snippet']).save()
             
            return redirect('codesnippets:index')
        else:
            return render(request, 'code/add.html', {'form': form})
    else:
        return render(request, 'code/add.html', {'form': CodeForm, 'header': 'GET'})
