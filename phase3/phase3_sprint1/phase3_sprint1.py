import sys
import csv
import json
import struct
import contextlib
import ctypes


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

    # 3

    val1 = [1, 2, 65535]
    val2 = [1.5, 2.5, -3.0]
    tuple_list = list(zip(val1, val2))

    with open("records.bin", "wb") as file:

        for id, value in tuple_list:
            packed = struct.pack("Hf", id, value)
            file.write(packed)

    with open("records.bin", "rb") as binary_file:
        record_size = struct.calcsize("Hf")
        record_list = []
        
        while True:
            chunk = binary_file.read(record_size)

            if not chunk:
                break

            record_tup = struct.unpack("Hf", chunk)
            record_list.append(record_tup)

    
    assert record_list == tuple_list



if __name__ == "__main__":
    sys.exit(main())
