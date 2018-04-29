from django.http import Http404
from django.shortcuts import render, redirect

from main.characters import Classic, Bear, Bird


def root(request, character_id=None):
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
            if character_id == 'bear':
                character = Bear()
            elif character_id == 'bird':
                character = Bird()
            elif character_id == 'classic':
                character = Classic()
            else:
                raise Http404('Character not found.')
        else:
            character = Bear()
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
        return render(request, 'index.html', context=context)
