import builtins
import importlib
import io
import sys

import pytest
from pytest import MonkeyPatch


@pytest.mark.parametrize(
    "test_input",
    [
        ["1", "1", "1"],
        ["2", "2", "2"],
        ["5", "5", "5"],
    ],
)
def test_equilátero(monkeypatch: MonkeyPatch, test_input: str):
    mocked_input = lambda prompt="": test_input.pop(0)
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    assert "Não é um triângulo" not in mocked_stdout.getvalue().strip()
    assert "Equilátero" in mocked_stdout.getvalue().strip()
    assert "Isósceles" not in mocked_stdout.getvalue().strip()
    assert "Escaleno" not in mocked_stdout.getvalue().strip()


@pytest.mark.parametrize(
    "test_input",
    [
        ["2", "2", "3"],
        ["3", "2", "2"],
        ["2", "3", "2"],
    ],
)
def test_isósceles(monkeypatch: MonkeyPatch, test_input: str):
    mocked_input = lambda prompt="": test_input.pop(0)
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    assert "Não é um triângulo" not in mocked_stdout.getvalue().strip()
    assert "Equilátero" not in mocked_stdout.getvalue().strip()
    assert "Isósceles" in mocked_stdout.getvalue().strip()
    assert "Escaleno" not in mocked_stdout.getvalue().strip()


@pytest.mark.parametrize(
    "test_input",
    [
        ["2", "3", "4"],
        ["2", "4", "3"],
        ["4", "2", "3"],
    ],
)
def test_escaleno(monkeypatch: MonkeyPatch, test_input: str):
    mocked_input = lambda prompt="": test_input.pop(0)
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    assert "Não é um triângulo" not in mocked_stdout.getvalue().strip()
    assert "Equilátero" not in mocked_stdout.getvalue().strip()
    assert "Isósceles" not in mocked_stdout.getvalue().strip()
    assert "Escaleno" in mocked_stdout.getvalue().strip()


@pytest.mark.parametrize(
    "test_input",
    [
        ["1", "2", "3"],
        ["1", "3", "2"],
        ["3", "1", "2"],
    ],
)
def test_não_é_um_triângulo(monkeypatch: MonkeyPatch, test_input: str):
    mocked_input = lambda prompt="": test_input.pop(0)
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    assert "Não é um triângulo" in mocked_stdout.getvalue().strip()
    assert "Equilátero" not in mocked_stdout.getvalue().strip()
    assert "Isósceles" not in mocked_stdout.getvalue().strip()
    assert "Escaleno" not in mocked_stdout.getvalue().strip()
