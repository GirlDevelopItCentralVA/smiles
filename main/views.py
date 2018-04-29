from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

from main.characters import Classic

##### Write your code here #####
def hello(request):
    #### TODO: Your code here #####
    pass


def coin_flip(request):
    ##### TODO: Your code here #####
    return render(request, 'coin.html', context={'text': 'Heads'})


def hello_form(request):
    #### TODO: Your code here #####
    pass
##### End #####


def character_page(request, character_id=None):
    if request.method == 'POST':
        saying = request.POST['saying']
        # Save the saying on the session
        request.session['saying'] = saying
        # Redirect back to the page that the user came from
        if character_id:
            return redirect('/' + character_id)
        else:
            return redirect('/')
    else:
        if character_id:
            ##### TODO: Handle different character types #####
            if character_id == 'classic':
                character = Classic()
            ##### End #####
            else:
                raise Http404('Character not found.')
        else:
            character = Classic()
        last_saying = request.session.get('saying', '')
        character.listen(last_saying)
        context = {
            'character_id': character_id,
            'last_saying': last_saying,
            'bg_color': character.get_color(),
            'face': character.get_face(),
            'mood': character.mood,
        }
        request.session['saying'] = None
        return render(request, 'character.html', context=context)
