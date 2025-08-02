import pytest
from excalibur.excalibur import ExcaliburCore

def test_core():
    core = ExcaliburCore()
    assert core.process_query("Test") is not None
