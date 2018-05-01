from main.characters import Bear, Bird


def test_bear_faces():
    c = Bear()
    assert c.get_face() == 'ʕ •ᴥ• ʔ'
    c.mood = -1.0
    assert c.get_face() == "ʕ •̀ o •́ ʔ"
    c.mood = -0.4
    assert c.get_face() == 'ʕ •̀ ω •́ ʔ'
    c.mood = 0.4
    assert c.get_face() == 'ʕ ᵔᴥᵔ ʔ'
    c.mood = 1.0
    assert c.get_face() == 'ʕ ᵔᴥᵔ ʔ'


def test_bird_faces():
    c = Bird()
    assert c.get_face() == '(￣Θ￣)'
    c.mood = -1.0
    assert c.get_face() == "＼( ˋ Θ ´ )／"
    c.mood = -0.4
    assert c.get_face() == '( ˋ Θ ´ )'
    c.mood = 0.4
    assert c.get_face() == '(◉Θ◉)♡'
    c.mood = 1.0
    assert c.get_face() == 'ヾ(￣◇￣)ノ〃'
