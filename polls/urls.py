from django.urls import path
from .views import IndexView, DetailView, ResultsView
from .views import PollCreateView, PollUpdateView, PollDeleteView
from .views import index, detail, results, vote


app_name = 'polls'

urlpatterns = [
	# path('', index, name='index'),
	# path('<int:question_id>/', detail, name='detail'),
	# path('<int:question_id>/results/', results, name='results'),
	path('', IndexView.as_view(), name='index'),
	path('<int:pk>/', DetailView.as_view(), name='detail'),
	path('<int:pk>/results/', ResultsView.as_view(), name='results'),
	path('<int:question_id>/vote/', vote, name='vote'),

	path('create/', PollCreateView.as_view(), name='create'),
	path('<int:pk>/update/', PollUpdateView.as_view(), name='update'),
	path('<int:pk>/delete/', PollDeleteView.as_view(), name='delete'),
]
