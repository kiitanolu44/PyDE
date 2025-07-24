import sys
import yaml
import xml.etree.ElementTree as ET


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

    # 2

    root = ET.Element("root")
    user = ET.SubElement(root, "user", id="1")
    ET.SubElement(user, "name").text = "Alice"

    user = ET.SubElement(root, "user", id="2")
    ET.SubElement(user, "name").text = "Bob"

    user = ET.SubElement(root, "user", id="3")
    ET.SubElement(user, "name").text = "Carol"

    # print(user)

    assert root[1][0].text == "Bob"

    user_count = 0

    for user in root:
        user_count += 1

    assert user_count == 3

    # assert root[1]




if __name__ == "__main__":
    sys.exit( main())
