from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.template import loader
#from models import Audio
#from django.shortcuts import render_to_response
from django.template.loader import render_to_string


from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request):
    rendered = render_to_string('detail.html', {'video_path': ''})
    response = HttpResponse(rendered)

    #template = loader.get_template('polls/templates/detail.html')
    #context = {
    #        'video_path': '',
    #}
    #return HttpResponse(template % context)
    return response

def audio(request):
    rendered = render_to_string('audio.html', {'audio_path': ''})
    response = HttpResponse(rendered)
    return response


def my_view(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)

#def results(request, secret_key):
#    response = "You're looking at the results of question %s."
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': response,
#    }
#    return HttpResponse(response % secret_key)

'''
class AjaxSaveAudio(request):

    audio_file = request.FILES.get('audio')
    shipphoto_obj = ShipPhoto.objects.get(pk='whatever')
    shipphoto_obj.voice_record = audio_file
    shipphoto_obj.save()
    """Use ajax to save audio sent by user."""

    def post(self, request):
        """Save recorded audio blob sent by user."""
        audio_file = request.FILES.get('recorded_audio')
        myObj = Audio()        # Put aurguments to properly according to your model
        myObj.voice_record = audio_file
        myObj.save()
        return JsonResponse({
            'success': True,
        })
'''