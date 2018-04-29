from main.characters import Character, Classic


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
    assert 0, 'todo'


def test_get_color():
    assert 0, 'todo'
