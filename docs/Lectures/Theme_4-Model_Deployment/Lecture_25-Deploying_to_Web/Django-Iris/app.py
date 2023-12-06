from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

import model

def index_view(request):
    return render(request, 'index.html')

def predict_class(request):
    try:
        slen = float(request.GET.get('slen'))
        swid = float(request.GET.get('swid'))
        plen = float(request.GET.get('plen'))
        pwid = float(request.GET.get('pwid'))

        # Get the output from the classification model
        variety = model.classify(slen, swid, plen, pwid)

        # Render the output in a new HTML page
        return render(request, 'output.html', {'variety': variety})
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)

urlpatterns = [path('', index_view),
    path('predict', predict_class)]

if __name__ == '__main__':
    from django.conf import settings

    settings.configure(
        DEBUG=True,
        # SECRET_KEY='0ix6w=71r6f)p6=7dz$3p2m_7n2(5*slxh-ac0gsm0a_&c)2&k',  # Replace with your actual secret key
        ROOT_URLCONF=__name__,
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': ['templates'],
                'APP_DIRS': True,
            },
        ],
    )

    import django
    django.setup()

    from django.core.management import execute_from_command_line

    execute_from_command_line(['app.py', 'runserver'])

   