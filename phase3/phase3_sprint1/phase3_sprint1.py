import sys
import csv
from tempfile import NamedTemporaryFile
import shutil


def main() -> None:
    fields = ["Name", "Age"]
    tempfile = NamedTemporaryFile(mode="w", delete=False)

    with open("data.csv", mode="r") as f, tempfile:
        reader = csv.DictReader(f, fieldnames=fields)
        writer = csv.DictWriter(f, fieldnames=fields)

        for row in reader:
            age = int(float(row["Age"]))
            row["Age"] = str(age + 1)

            print(row)
            writer.writerow(row)

    shutil.move(tempfile, f)


if __name__ == "__main__":
    sys.exit(main())
