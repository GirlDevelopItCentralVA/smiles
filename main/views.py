from django.shortcuts import render, redirect

from main.characters import Bear, Classic

characters = [
    Bear,
    Classic,
]


def root(request, character_id=None):
    if character_id:
        if character_id == 'bear':
            character = Bear()
        else:
            character = Classic()
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


def post_saying(request):
    if request.method == 'POST':
        saying = request.POST['saying']
        request.session['saying'] = saying
    return redirect('root')
