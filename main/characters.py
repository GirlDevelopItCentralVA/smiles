from textblob import TextBlob


class Bear:

    def __init__(self):
        self.mood = 0.0

    def listen(self, text):
        if text:
            blob = TextBlob(text)
            sentiment = blob.sentiment
            self.mood = sentiment.polarity
        else:
            self.mood = 0.0
        return self.mood

    def get_face(self):
        if self.mood < -0.5:  # very negative
            return 'ʕ •̀ o •́ ʔ'
        elif self.mood < -0.3:  # slightly negative
            return 'ʕ •̀ ω •́ ʔ'
        elif self.mood > 0.5:  # very positive
            return 'ʕ ᵔᴥᵔ ʔ'
        elif self.mood > 0.3:  # slightly positive
            return 'ʕ ᵔᴥᵔ ʔ'
        else:
            return 'ʕ •ᴥ• ʔ'

    def get_color(self):
        if self.mood < -0.5:  # very negative
            return 'dark-red'
        elif self.mood < -0.3:  # slightly negative
            return 'red'
        elif self.mood > 0.5:  # very positive
            return 'green'
        elif self.mood > 0.3:  # slightly positive
            return 'washed-green'
        else:
            return 'lightest-blue'
