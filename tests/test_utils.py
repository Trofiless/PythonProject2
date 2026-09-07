import json
from src.utils import load_operations


def test_load_operations_valid_file(tmp_path):
    data = [{"id": 1, "state": "EXECUTED"}]
    file_path = tmp_path / "operations.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")
    assert load_operations(file_path) == data


def test_load_operations_file_not_found(tmp_path):
    file_path = tmp_path / "missing.json"
    assert load_operations(file_path) == []


def test_load_operations_empty_file(tmp_path):
    file_path = tmp_path / "empty.json"
    file_path.write_text("", encoding="utf-8")
    assert load_operations(file_path) == []


def test_load_operations_not_a_list(tmp_path):
    file_path = tmp_path / "operations.json"
    file_path.write_text(json.dumps({"id": 1}), encoding="utf-8")
    assert load_operations(file_path) == []
