from typing import List, Mapping
import io


def calculate_bigrams(number:int, stream:io.TextIOWrapper)->List[str]:
    return ["xx", "xx", "xx"]


def print_result(result:Mapping[str,List[str]])->None:
    print("Hello!")


def main(number:int=5):
    result = {}
    for language in ["eglish", "welsh"]:
        filename = "%s.txt" % language
        result[language] = calculate_bigrams(number, open(filename))

    print_result(result)


if __name__ == "__main__":
    main()