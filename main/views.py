from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

from main.characters import Classic, Bear, Bird

##### Students would write the code below #####
def hello(request):
    return HttpResponse('Hello World')

def hello_with_query_param(request):
    name = request.GET.get('name', 'World')
    return HttpResponse('Hello ' + name)

def hello_with_template(request):
    context = {
        'name': 'World'
    }
    return render(request, 'hello.html', context)


def hello_with_param(request, name='World'):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)

def hello_with_post(request):
    if request.method == 'POST':
        name = request.POST['name']
    else:
        name = 'World'
    context = {
        'name': name,
    }
    return render(request, 'hello_with_form.html', context)
##### End of student's code


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
        ##### Student would write the code below
        if character_id:
            if character_id == 'bear':
                character = Bear()
            elif character_id == 'bird':
                character = Bird()
            elif character_id == 'classic':
                character = Classic()
        ##### End of students' code
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
