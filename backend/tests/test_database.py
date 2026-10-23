
from pathlib import Path


def test_basic_arithmetic():
    assert 1 + 1 == 2


def test_database_configuration_file_exists():
    project_root = Path(__file__).resolve().parents[2]
    assert (project_root / "backend" / "database" / "connection.py").exists()


def test_database_models_file_exists():
    project_root = Path(__file__).resolve().parents[2]
    assert (project_root / "backend" / "database" / "models.py").exists()


def test_company_model_definition_exists():
    project_root = Path(__file__).resolve().parents[2]
    models_file = project_root / "backend" / "database" / "models.py"
    source = models_file.read_text(encoding="utf-8")

    assert "class Company(Base):" in source
    assert '__tablename__ = "companies"' in source


def test_lead_model_definition_exists():
    project_root = Path(__file__).resolve().parents[2]
    models_file = project_root / "backend" / "database" / "models.py"
    source = models_file.read_text(encoding="utf-8")

    assert "class Lead(Base):" in source
    assert '__tablename__ = "leads"' in source
    
