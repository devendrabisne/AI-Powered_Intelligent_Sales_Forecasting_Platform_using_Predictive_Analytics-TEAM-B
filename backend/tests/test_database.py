
def test_basic_arithmetic():
    assert 1 + 1 == 2


def test_database_configuration_file_exists():
    from pathlib import Path

    project_root = Path(__file__).resolve().parents[2]
    assert (project_root / "backend" / "database" / "connection.py").exists()
  
