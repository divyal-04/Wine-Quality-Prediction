from django.shortcuts import render
from django.http import HttpResponse
from joblib import load
import numpy as np

# We have to create the views here

def home(request):
    quality_score = None

    if request.method == 'POST':
        quality_score = None
        # Load the model from the file
        model = load('models/model2.joblib')

        # Get the input data from the form
        fixed_acidity = float(request.POST.get('fixed_acidity'))
        volatile_acidity = float(request.POST.get('volatile_acidity'))
        citric_acid = float(request.POST.get('citric_acid'))
        residual_sugar = float(request.POST.get('residual_sugar'))
        chlorides = float(request.POST.get('chlorides'))
        free_sulphur = float(request.POST.get('free_sulphur'))
        total_sulphur = float(request.POST.get('total_sulphur'))
        density = float(request.POST.get('density'))
        pH = float(request.POST.get('pH'))
        sulphates = float(request.POST.get('sulphates'))
        alcohol = float(request.POST.get('alcohol'))

        # Create an input array for the model prediction
        input_data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
                                chlorides, free_sulphur, total_sulphur, density, pH, sulphates, alcohol]])

        # Make a prediction using the model
        prediction = model.predict(input_data)
        print(prediction)

        # Convert the prediction to a quality score between 0 and 10
        # quality_score = int(round(prediction[0] * 10))
        # print("quality score: ", quality_score)

        quality_score = prediction[0]

        print("quality is: ", quality_score)

        if (quality_score==1):
            print('Good Quality Wine')
        else:
            print('Bad Quality Wine')

    # Send the quality score to the template using context
    context = {'quality_score': quality_score}
    return render(request, 'main.html', context)



def about(request):
    return render(request, 'about.html')


def modelInfo(request):
    return render(request, 'modelInfo.html')
