import sys
import csv
import json
import struct
import contextlib


def main() -> None:

    # 1

    with open("data.csv", mode="r") as file, open("out.csv", mode="w") as tempfile:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(tempfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        check = []

        for row in reader:
            row["Age"] = int(row["Age"])
            row["Age"] = row["Age"] + 1
            writer.writerow(row)
            check.append(row)
            # print(row)
            
        assert check[0].get("Name") == "Alice" and check[0].get("Age") == 31
        assert check[1].get("Name") == "Bob" and check[1].get("Age") == 26
        assert check[2].get("Name") == "Carol" and check[2].get("Age") == 41

    # 2

    with open("base.json", "r") as base_file:
        base = json.load(base_file)

    with open("override.json", "r") as override_file:
        override = json.load(override_file)

    merged = base.copy()
    
    for key, value in override.items():
        if key not in merged:
            merged[key] = value
        else:
            merged[key].extend(override["flags"])

    expected_dict = {
        "threshold": 10,
        "flags": ["a", "b", "c"],
        }

    assert merged == expected_dict



if __name__ == "__main__":
    sys.exit(main())
