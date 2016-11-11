from typing import List, Mapping
import io


def calculate_bigrams(number: int, stream: io.TextIOWrapper)->List[str]:
    """
    :param number: The number of bigrams you want to return
    :param stream: A text stream, the result of opening a file
    :return: List of bigrams
    """
    return ["xx"] * number


def print_result(result:Mapping[str,List[str]])->None:
    """
    :param result: Mapping of language name to the most common bigrams
    :return:
    """
    print("Hello!")

def main(number: int=5):
    result = {}
    for language in ["english", "welsh"]:
        filename = "%s.txt" % language
        result[language] = calculate_bigrams(number, open(filename))

    print_result(result)


if __name__ == "__main__":
    main()