"""
from django.template import loader
from .models import produit
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
"""


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import produit, Image, Slide, windsurf
from django.utils import timezone



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_produit_list'
    
    def get_queryset(self):
        #Return the last five published produits
        return produit.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['slide_list'] = Slide.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
        return context 



class produitView(generic.ListView):
    template_name = 'polls/produit.html'
    context_object_name = 'latest_produit_list'
    
    def get_queryset(self):
        #Return the last five published produits
        return produit.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]













class DetailView(generic.DetailView):
    model = produit
    template_name = 'polls/detail.html'

    def get_queryset(self):
        
            #Excludes any produits that aren't published yet.
        
        return produit.objects.filter(pub_date__lte=timezone.now())

















class windsurfView(generic.ListView):
    template_name = 'polls/windsurf.html'
    context_object_name = 'latest_windsurf_list'
    
    def get_queryset(self):
        #Return the last five published windsurfs
        return windsurf.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]




class DetailwindsurfView(generic.DetailView):
    model = windsurf
    template_name = 'polls/detail.html'

    def get_queryset(self):
        
            #Excludes any windsurfs that aren't published yet.
        
        return windsurf.objects.filter(pub_date__lte=timezone.now())










"""

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'slide_list'
    
    def get_queryset(self):
        #Return the last five published produits
        return Slide.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class SlideView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'slide_list'
    
    def get_queryset(self):
        #Return the last five published produits
        #print slide.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        return Slide.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]










class ResultsView(generic.DetailView):
    model = produit
    template_name = 'polls/results.html'





def vote(request, produit_id):
    produit = get_object_or_404(produit, pk=produit_id)
    try:
        selected_choice = produit.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the produit voting form.
        return render(request, 'polls/detail.html', {
                      'produit': produit,
                      'error_message': "You didn't select a choice.",
                      })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(produit.id,)))


"""
