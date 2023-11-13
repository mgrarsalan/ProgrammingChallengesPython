# Counts occurrences of characters in a given string (Excluding unicode)
# 46 - Easy - Algorithmic
import string

# Getting the string
def get_string() -> str:
    return input('Enter a string: ').lower() # Just for the convenience we convert it to lowercase

chars = list(string.ascii_lowercase + string.digits + string.punctuation + string.whitespace)


def count(text: str) -> dict:
    char_occur = {key: 0 for key in chars}
    for i in text:
        char_occur[i] += 1
    return char_occur

def main():
    text = get_string()
    count_dict = count(text)
    print(count_dict)

if __name__ == "__main__":
    main()