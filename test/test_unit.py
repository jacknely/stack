import pytest
from app.stack import Interpreter


class TestStack():

    def setup_method(self):
        self.interpreter = Interpreter([4, 5, 6, 8])

    @pytest.mark.parametrize('digits, result', [('45', 45), ('toilet', None,)])
    def test_getdigits(self, digits, result):
        self.interpreter.getdigits(digits)
        assert self.interpreter.digits == result

    @pytest.mark.parametrize('result', [([4, 5, 6])])
    def test_pop(self, result):
        self.stack = self.interpreter.pop()
        assert self.interpreter.stack == result


if __name__ == '__main__':
    pytest.main()

