from main.characters import Bear


def test_bear_listen():
    bear = Bear()
    bear.listen('good bear!')
    assert bear.mood > 0.0
    bear.listen('bad bear!')
    assert bear.mood < 0.0
    bear.listen(None)
    assert bear.mood == 0.0


def test_bear_faces():
    bear = Bear()
    assert bear.get_face() == 'ʕ •ᴥ• ʔ'
    bear.mood = -1.0
    assert bear.get_face() == 'ʕ •̀ o •́ ʔ'
    bear.mood = -0.4
    assert bear.get_face() == 'ʕ •̀ ω •́ ʔ'
    bear.mood = 0.4
    assert bear.get_face() == 'ʕ ᵔᴥᵔ ʔ'
    bear.mood = 1.0
    assert bear.get_face() == 'ʕ ᵔᴥᵔ ʔ'


def test_bear_colors():
    bear = Bear()
    assert bear.get_color() == 'lightest-blue'
    bear.mood = -1.0
    assert bear.get_color() == 'dark-red'
    bear.mood = -0.4
    assert bear.get_color() == 'red'
    bear.mood = 0.4
    assert bear.get_color() == 'washed-green'
    bear.mood = 1.0
    assert bear.get_color() == 'green'
