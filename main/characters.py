

class Classic:
    def __init__(self):
        self.mood = 0.0

    def get_face(self):
        if self.mood < -0.5:  # very negative
            return ":'-("
        elif self.mood < -0.3:  # slightly negative
            return ':-('
        elif self.mood > 0.5:  # very positive
            return ':-D'
        elif self.mood > 0.3:  # slightly positive
            return ':-)'
        else:
            return ':-|'

    ##### TODO: Your code here #####


class Bear:
    ##### TODO: Your code here #####
    pass


class Bird:
    ##### TODO: Your code here #####
    pass
