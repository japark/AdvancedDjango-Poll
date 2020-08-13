from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse, reverse_lazy
from django.forms import inlineformset_factory
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.template import loader
from .models import Question, Choice

# Create your views here.

class IndexView(ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]


class DetailView(DetailView):
	model = Question
	template_name = 'polls/detail.html'


class ResultsView(DetailView):
	model = Question
	template_name = 'polls/results.html'


class PollCreateView(CreateView):
	model = Question
	fields = ['question_text']
	template_name = 'polls/create.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['formset'] = inlineformset_factory(Question, Choice, fields=('choice_text',))
		return context

	def form_valid(self, form):
		self.object = form.save()
		ChoiceFormSet = inlineformset_factory(Question, Choice, fields=('choice_text',))
		formset = ChoiceFormSet(self.request.POST, instance=self.object)
		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(self.get_success_url())


class PollUpdateView(UpdateView):
	model = Question
	fields = ['question_text']
	template_name = 'polls/update.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['formset'] = inlineformset_factory(Question, Choice, fields=('choice_text',), extra=0)
		context['formset'] = context['formset'](instance=self.object)
		return context

	def form_valid(self, form):
		self.object = form.save()
		ChoiceFormSet = inlineformset_factory(Question, Choice, fields=('choice_text',))
		formset = ChoiceFormSet(self.request.POST, instance=self.object)
		if formset.is_valid():
			self.object.choice_set.all().delete()
			formset.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.form_invalid(form)

	def form_invalid(self, form):
		context = self.get_context_data(form=form)
		context['error_message'] = '비어있는 선택지가 있으면 안됩니다.'
		return self.render_to_response(context)


class PollDeleteView(DeleteView):
	model = Question
	success_url = reverse_lazy('polls:index')


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

	''' 단축함수 render() 이용하지 않고 하는 방법! '''
	# template = loader.get_template('polls/index.html')
	# return HttpResponse(template.render(context, request))


def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)

	''' 단축함수 get_object_or_404() 이용하지 않고 하는 방법!'''
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
