from main import coin


def test_flip_loaded():
    result = coin.flip_loaded()
    assert result == 'H'

def test_flip():
    result = coin.flip()
    assert result in ['H', 'T']
