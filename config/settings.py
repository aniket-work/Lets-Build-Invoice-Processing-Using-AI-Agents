import yaml
from pathlib import Path

def load_config():
    config_path = Path(__file__).parent / "config.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

CONFIG = load_config()

# App settings
APP_CONFIG = CONFIG["app"]
COMPANY_INFO = CONFIG["company"]
UPLOAD_CONFIG = CONFIG["upload"]
MODEL_CONFIG = CONFIG["model"]
THEME = CONFIG["theme"]