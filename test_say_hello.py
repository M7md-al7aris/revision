from hello import say_hello, say_bye

def test_say_hello():
    assert "hello" == say_hello()

def test_say_bye():
    assert 'bye'== say_bye()