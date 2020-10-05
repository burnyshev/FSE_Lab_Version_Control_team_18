from storage import Storage

def test_add():
    pass

def test_remove():
    pass

def test_set():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    value = 3
    st.set(key, value)
    result = st.get(key)
    assert result == 3, "Set function does not change value for key {}".format(key)
    key = 'c'
    value = 10
    st.set(key, value)
    result = st.get(key)
    assert result is None, "Set function created new key-value"

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    test_add()
    test_remove()
    test_set()
    test_get()

if __name__ == "__main__":
    run_tests()
