from storage import Storage

def test_add():
    st = Storage({'a': 1, 'b': 2})
    st.add('c', 3)
    key = 'c'
    val = st.get(key)
    assert val == 3, "Value for the key {} is not equal to expected".format(key)
    st.add('a', 5)
    key = 'a'
    val = st.get(key)
    assert val == 1, "Value for the key {} is not equal to expected".format(key)
    st.add(['a', 'b'], 10)
    assert (['a', 'b'] in list(st.data.keys())) == False, "Added invalid key"

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
