from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Bb
from .models import Rubric

def by_rubric(request, rubric_id):
	bbs = Bb.objects.filter(rubric= rubric_id)
	rubrics = Rubric.objects.all()
	current_rubric = Rubric.objects.get(pk = rubric_id)
	context = {'bbs': bbs, 'rubrics':rubrics, 'current_rubric':current_rubric}
	return render(request, 'bboard/by_rybric.html', context)

# def index(request):
# 	s = 'list of advertisement \r\n\r\n\r\n'
# 	for bb in Bb.objects.order_by('-published'):
# 		s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
# 	return HttpResponse( s, content_type = 'text/plain; charset=utf-8')

def index(request):
	template = loader.get_template('bboard/index.html')
	bbs = Bb.objects.order_by('-published')
	context = {'bbs' : bbs }
	return HttpResponse(template.render(context, request))

def hh(request):
	bbs = Bb.objects.order_by('-published')
	return render(request,'bboard/index.html', {'bbs':bbs})

	
def vova(request):
	return HttpResponse('he is Vova')
# Create your views here.



