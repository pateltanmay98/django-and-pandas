# Create your views here.
import pandas as pd
from django.shortcuts import render

from cars.models import Car


def main_view(request):
    qs = Car.objects.all().values()
    data = pd.DataFrame(qs)
    context = {
        'df': data.to_html(),
        'describe': data.describe().to_html()
    }
    return render(request, 'main.html', context)
