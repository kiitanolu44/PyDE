import sys
import os
import yaml
import xml.etree.ElementTree as ET
import configparser
import fcntl
import threading


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

    assert root[1][0].text == "Bob"

    user_count = 0

    for user in root:
        user_count += 1

    assert user_count == 3

    # 3

    config = configparser.ConfigParser()
    config.read("settings.ini")

    config.set("network", "timeout", "60")
    config["cache"] = {"enabled": True}

    with open("settings.ini", "w") as config_file:
        config.write(config_file)

    config = configparser.ConfigParser()
    config.read("settings.ini")

    assert int(config["network"]["timeout"]) == 60
    assert config["cache"]["enabled"] == "True"

    # cleanup/restoring .ini file to its original

    config.set("network", "timeout", "30")

    if config.has_section("cache"):
        config.remove_section("cache")

    with open("settings.ini", "w") as clean_config_file:
        config.write(clean_config_file)

    # 4

    flags = fcntl.LOCK_EX | fcntl.LOCK_NB
    lock_failed = [None]

    f1 = open("lockfile.txt", "w+")

    try:
        fcntl.flock(f1, flags)
    except BlockingIOError:
        assert False, "first lock should succeed"

    def worker_func():
        f2 = open("lockfile.txt", "w+")
        try:
            fcntl.flock(f2, flags)
            lock_failed[0] = False
        except BlockingIOError:
            assert True, "working as intended"
            lock_failed[0] = True
        finally:
            f2.close()

    t = threading.Thread(target=worker_func)
    t.start()
    t.join()

    assert lock_failed[0] is True, "second thread should have failed to acquire the lock"

    # cleanup
    fcntl.flock(f1, fcntl.LOCK_UN)
    f1.close()

    if os.path.exists("lockfile.txt"):
        os.remove("lockfile.txt")


if __name__ == "__main__":
    sys.exit(main())

# .ini felt the most intuitive and easiest to work with, wheras fcntl task was quite intersting/tricky, little documentation to work with on file locking
