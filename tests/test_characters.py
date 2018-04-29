from main.characters import Classic
from main import coin


def test_coin():
    result = coin.flip()
    assert 0, 'todo'


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
