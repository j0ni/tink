from tink.playing import Playing

def test_thingy_inc():
    thingy = Playing()
    assert thingy.value == 10
    thingy.inc()
    assert thingy.value == 11

def test_thingy_dec():
    thingy = Playing()
    assert thingy.value == 10
    thingy.dec()
    assert thingy.value == 9
    
