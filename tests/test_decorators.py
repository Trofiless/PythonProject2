import pytest

from src.decorators import log


def test_log_success(capsys):
    @log()
    def add(x, y):
        return x + y

    result = add(1, 2)
    captured = capsys.readouterr()

    assert result == 3
    assert "add ok" in captured.err or "add ok" in captured.out


def test_log_error(capsys):
    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()

    assert "divide error" in captured.err or "divide error" in captured.out
    assert "ZeroDivisionError" in captured.err or "ZeroDivisionError" in captured.out
