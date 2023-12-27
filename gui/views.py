from django.template import loader
from django.http import HttpResponse
from gui.forms import PredictForm

def home(request):
    template = loader.get_template('home.html')
    form = PredictForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))
