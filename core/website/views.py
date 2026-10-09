from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index_view(request):
    context = {}
    return render(request, "website/index.html", context)