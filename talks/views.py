from django.views.generic.list import ListView
from django.shortcuts import render_to_response

from .models import Talk


class TalkListView(ListView):
    model = Talk


def home_page(request):
    return render_to_response(
        'home-talks-mithril.html' if 'mithril' in request.GET else 'home-talks.html',
        {
        },

        # context_instance=RequestContext(request)
    )

