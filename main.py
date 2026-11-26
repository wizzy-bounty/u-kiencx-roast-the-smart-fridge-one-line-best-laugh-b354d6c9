import os

def entry_text():
    return "My smart fridge has an inside camera, so now my leftovers get judged before I do."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as entry_file:
        entry_file.write(entry_text())


if __name__ == "__main__":
    main()
