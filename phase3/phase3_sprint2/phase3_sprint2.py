import sys
import yaml
from pprint import pprint



def main() -> None:

    # 1

    yaml_check = {
        "service": {
            "name": "emailer",
            "retries": 3,
            "endpoints": [
                {"url": "https://api.example.com/send"},
                {"url": "https://api.backup.com/send"},
            ],
        },
    }

    with open("config.yaml", "r") as file:
        yaml_file = yaml.safe_load(file)
    

    assert yaml_file == yaml_check


if __name__ == "__main__":
    sys.exit( main())
