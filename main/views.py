from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

from main.characters import Classic

#### Lessons 1-3: A basic view; query parameters; templates #####

def hello(request):
    ##### TODO: Your code here #####
    pass

##### "Let's develop it" (independent practice) #####

def coin_flip(request):
    ##### TODO: Your code here #####
    text = 'Heads'
    return render(request, 'coin.html', context={'text': text})


##### Lesson 4: Handling POST requests #####

def hello_form(request):
    ##### TODO: Your code here #####
    return render(request, 'hello_with_form.html', context={'name': 'World'})

##### Lesson 5: Handling path variables #####

def hello_path(request, name):
    ##### TODO: Your code here #####
    pass


##### Lesson 6: Putting it all together #####
def character_page(request, character_id=None):
    if request.method == 'POST':
        saying = request.POST['saying']
        # Redirect back to the page that the user came from
        # With the saying in the query params
        if character_id:
            return redirect('/' + character_id + '/?saying=' + saying)
        else:
            return redirect('/?saying=' + saying)
    else:
        if character_id:
            ##### TODO: Your code here #####
            if character_id == 'classic':
                character = Classic()
            ##### End #####
            else:
                raise Http404('Character not found.')
        else:
            character = Classic()
        last_saying = request.GET.get('saying', '').strip()
        character.listen(last_saying)
        context = {
            'character_id': character_id or '',
            'last_saying': last_saying,
            'bg_color': character.get_color(),
            'face': character.get_face(),
            'mood': character.mood,
        }
        return render(request, 'character.html', context=context)
