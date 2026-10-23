from pathlib import Path


def test_basic_arithmetic():
    assert 1 + 1 == 2


def test_database_configuration_file_exists():
    project_root = Path(__file__).resolve().parents[2]
    assert (project_root / "database" / "connection.py").exists()


def test_database_models_file_exists():
    project_root = Path(__file__).resolve().parents[2]
    assert (project_root / "database" / "models.py").exists()
