from main.characters import Classic


def test_classic_faces():
    c = Classic()
    assert c.get_face() == ':-|'
    c.mood = -1.0
    assert c.get_face() == ":'-("
    c.mood = -0.4
    assert c.get_face() == ':-('
    c.mood = 0.4
    assert c.get_face() == ':-)'
    c.mood = 1.0
    assert c.get_face() == ':-D'


def test_listen():
    c = Classic()
    c.listen('good day!')
    assert c.mood > 0
    c.listen('bad day!')
    assert c.mood < 0
    c.listen('')
    assert c.mood == 0
    c.listen(None)
    assert c.mood == 0


def test_get_color():
    c = Classic()
    assert c.get_color() == 'lightest-blue'
    c.mood = -1.0
    assert c.get_color() == "dark-red"
    c.mood = -0.4
    assert c.get_color() == 'red'
    c.mood = 0.4
    assert c.get_color() == 'washed-green'
    c.mood = 1.0
    assert c.get_color() == 'green'
