from main.characters import Character, Classic


def test_listen():
    c = Character()
    c.listen('good boy!')
    assert c.mood > 0.0
    c.listen('bad boy!')
    assert c.mood < 0.0
    c.listen('')
    assert c.mood == 0.0
    c.listen(None)
    assert c.mood == 0.0


def test_get_color():
    c = Character()
    assert c.get_color() == 'lightest-blue'
    c.mood = -1.0
    assert c.get_color() == 'dark-red'
    c.mood = -0.4
    assert c.get_color() == 'red'
    c.mood = 0.4
    assert c.get_color() == 'washed-green'
    c.mood = 1.0
    assert c.get_color() == 'green'


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
