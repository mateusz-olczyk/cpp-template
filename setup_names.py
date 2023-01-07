#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from os import rename

SCRIPT_DIR = Path(__file__).resolve().parent


def name_upper(string: str) -> str:
    return string.replace(" ", "").upper()


def name_lower(string: str) -> str:
    return string.replace(" ", "").lower()


def name_capitalized(string: str) -> str:
    return "".join(word.lower().capitalize() for word in string.split())


def replace_names(old_name: str, new_name: str) -> None:
    cmake_old_utils_file = SCRIPT_DIR.joinpath("cmake", name_capitalized(old_name) + "Utils.cmake")
    cmake_new_utils_file = SCRIPT_DIR.joinpath("cmake", name_capitalized(new_name) + "Utils.cmake")
    rename(cmake_old_utils_file, cmake_new_utils_file)

    cmake_files = [
        cmake_new_utils_file,
        SCRIPT_DIR.joinpath("CMakeLists.txt"),
        SCRIPT_DIR.joinpath("test", "CMakeLists.txt"),
        SCRIPT_DIR.joinpath("src", "CMakeLists.txt")
    ]

    for cmake_file in cmake_files:
        with open(cmake_file, "r+", encoding="UTF-8") as file:
            content = file.read()
            content = content.replace("project(" + name_capitalized(old_name), "project(" + name_capitalized(new_name))
            content = content.replace("include(" + name_capitalized(old_name) + "Utils",
                                      "include(" + name_capitalized(new_name) + "Utils")
            content = content.replace(name_lower(old_name) + "_", name_lower(new_name) + "_")
            content = content.replace(name_upper(old_name) + "_", name_upper(new_name) + "_")
            file.seek(0)
            file.write(content)


if __name__ == "__main__":
    parser = ArgumentParser(description='Replaces "myproject" names in all CMakeLists.txt files.')
    parser.add_argument("old_name", nargs="?", default="my project", help="old project name to be replaced")
    parser.add_argument("new_name", help="new project name to be set")

    args = parser.parse_args()
    replace_names(args.old_name, args.new_name)
