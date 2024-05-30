FILENAME = "books/frankenstein.txt"
def word_count(string: str) -> int:
    if not string:
        raise Exception("Empty string passed")
    return len(string.split())


def word_frequency(string: str) ->dict:
    if not string:
        raise Exception("Empty string passed")

    string = string.lower()
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def main():
    with open(FILENAME, "r") as f:
        file_contents = f.read()

    wc = word_count(file_contents)

    wf = word_frequency(file_contents)
    wf = dict(sorted(wf.items(), key=lambda item: item[1], reverse=True))
    print(f"--- Begin report of {FILENAME} ---")
    print(f"{wc} words found in the document\n")

    for word, freq in wf.items():
        if word.isalpha():
            print(f"The '{word}' character was found {freq} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()