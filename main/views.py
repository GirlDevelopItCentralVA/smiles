from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

from . import coin
from main.characters import Classic, Bear, Bird

#### Lesson 1: A basic view #####

# def hello(request):
#     return HttpResponse('Hello World')

##### Lesson 2: Using query parameters #####

# def hello(request):
#     name = request.GET.get('name', 'World')
#     return HttpResponse('Hello ' + name)


##### Lesson 3: Using a template #####

def hello(request):
    name = request.GET.get('name', 'World')
    return render(request, 'hello.html', context={'name': name})

##### "Let's develop it" (independent practice) #####

def coin_flip(request):
    result = coin.flip()
    if result == 'H':
        text = 'Heads'
    else:
        text = 'Tails'
    return render(request, 'coin.html', context={'text': text})


##### Lesson 4: Handling POST requests #####

def hello_form(request):
    if request.method == 'POST':
        name = request.POST['name']
    else:
        name = 'World'
    return render(request, 'hello_with_form.html', context={'name': name})


#### Lesson 5: Handling path variables ####

def hello_path(request, name='World'):
    return render(request, 'hello.html', context={'name': name})


#### Lesson 6: Putting it all together #####
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
            ##### Student's code goes here #####
            if character_id == 'classic':
                character = Classic()
            elif character_id == 'bear':
                character = Bear()
            elif character_id == 'bird':
                character = Bird()
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
