from django.shortcuts import render, redirect

from textblob import TextBlob


def polarity_to_face(polarity):
    if polarity < -0.5:  # very negative
        return 'ʕ •̀ o •́ ʔ'
    elif polarity < -0.3:  # slightly negative
        return 'ʕ •̀ ω •́ ʔ'
    elif polarity > 0.5:  # very positive
        return 'ʕ ᵔᴥᵔ ʔ'
    elif polarity > 0.3:  # slightly positive
        return 'ʕ ᵔᴥᵔ ʔ'
    else:
        return 'ʕ •ᴥ• ʔ'


def polarity_to_color(polarity):
    if polarity < -0.5:  # very negative
        return 'dark-red'
    elif polarity < -0.3:  # slightly negative
        return 'red'
    elif polarity > 0.5:  # very positive
        return 'green'
    elif polarity > 0.3:  # slightly positive
        return 'washed-green'
    else:
        return 'lightest-blue'


def root(request):
    last_saying = request.session.get('last_saying', {})
    if last_saying:
        polarity = last_saying['polarity']
    else:
        polarity = 0
    context = {
        'last_saying': last_saying,
        'bg_color': polarity_to_color(polarity),
        'face': polarity_to_face(polarity),
        'polarity': polarity,
    }
    request.session['last_saying'] = None
    return render(request, 'index.html', context=context)


def post_saying(request):
    if request.method == 'POST':
        saying = request.POST['saying']
        blob = TextBlob(saying)
        sentiment = blob.sentiment
        # Store the saying on the session so we can display it
        request.session['last_saying'] = {
            'text': saying,
            'polarity': sentiment.polarity,
        }
    return redirect('root')
