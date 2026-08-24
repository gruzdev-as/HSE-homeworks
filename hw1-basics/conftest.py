import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "bonus: необязательное задание со звёздочкой, не влияет на обязательный балл",
    )
