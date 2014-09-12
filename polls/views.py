from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from polls.models import Poll,Choice
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
    #return HttpResponse("Hello,index")
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list':latest_poll_list}
    return render(request,"polls/index.html",context)
def detail(request,poll_id):
    poll = get_object_or_404(Poll,pk=poll_id)
    return render(request,"polls/detail.html",{"poll":poll})
def results(request,poll_id):
    #return HttpResponse("results:%s." % poll_id)
    poll = get_object_or_404(Poll,pk=poll_id)
    return render(request,'polls/results.html',{'poll':poll})
def vote(request,poll_id):
    #return HttpResponse("vote:%s." % poll_id)
    p = get_object_or_404(Poll,pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'poll':p,
                                                  'error_message':'You did not select a choice',})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
