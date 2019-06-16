import pytest
from app.stack import Interpreter


@pytest.fixture
def mock_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "Push 4")

class TestStack():

    def setup_method(self):
        self.stack = [4, 5, 8, 6]
        self.interpreter = Interpreter(self.stack)

    def test_processinput(self, mock_input):
        self.interpreter.processinput()
        assert self.interpreter.result == [4, 5, 8, 6, 4]


