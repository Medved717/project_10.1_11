from src.code import up_first

def test_up_first():
    assert up_first('python_1') == 'Python_1'


def test_up_first_for_empty():
    assert up_first('') == ''
