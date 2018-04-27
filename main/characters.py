from textblob import TextBlob


class Character:
    # Subclasses must override these
    neutral = None
    very_negative = None
    slightly_negative = None
    slightly_positive = None
    very_positive = None

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
            return self.very_negative
        elif self.mood < -0.3:  # slightly negative
            return self.slightly_negative
        elif self.mood > 0.5:  # very positive
            return self.very_positive
        elif self.mood > 0.3:  # slightly positive
            return self.slightly_positive
        else:
            return self.neutral

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


class Bear(Character):
    neutral = 'ʕ •ᴥ• ʔ'
    very_negative = 'ʕ •̀ o •́ ʔ'
    slightly_negative = 'ʕ •̀ ω •́ ʔ'
    slightly_positive = 'ʕ ᵔᴥᵔ ʔ'
    very_positive = 'ʕ ᵔᴥᵔ ʔ'
