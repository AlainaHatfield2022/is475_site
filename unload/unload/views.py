from django.views.generic import TemplateView
from datetime import datetime, timedelta

class HomeView(TemplateView):
    template_name = 'Index.html'

class FormView(TemplateView):
    template_name = 'Form.html'

class BoardView(TemplateView):
    template_name = 'Leaderboard.html'