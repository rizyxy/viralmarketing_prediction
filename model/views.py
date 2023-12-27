from django.template import loader
import pickle
from gui.forms import PredictForm
from django.http import HttpResponseRedirect, HttpResponse
import os
from viralmarketing import settings
from gui.forms import PredictForm

def load_model():
    model_path = os.path.join(settings.BASE_DIR, 'model/model/model.sav')
    with open(model_path, 'rb') as file:
        model = pickle.load(file=file)
    return model

def predict_view(request):

    if request.method == "POST":

        model = load_model()

        data = PredictForm(request.POST)

        if data.is_valid():

            gender = data.cleaned_data['gender']
            menarik = data.cleaned_data['menarik']
            ramai = data.cleaned_data['ramai']
            diskon = data.cleaned_data['diskon']

            predict_data = [[gender, menarik, ramai, diskon]]

            prediction = model.predict(predict_data)

            if prediction[0] == 0:
                prediction = "Beberapa Kali"
            elif prediction[0] == 1:
                prediction = "Jarang Sekali"
            elif prediction[0] == 2:
                prediction = "Sangat Sering"
            elif prediction[0] == 3:
                prediction = "Sering"

            template = loader.get_template('result.html')
            form = PredictForm()

            context = {
                'form': data,
                'prediction': prediction
            }

            return HttpResponse(template.render(context, request))
        
        else:
            return HttpResponseRedirect('')
    else:
        return HttpResponseRedirect('')

