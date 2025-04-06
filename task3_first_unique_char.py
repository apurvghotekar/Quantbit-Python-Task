from collections import Counter

def first_unique_char(s: str) -> str:
    char_count = Counter(s)
    for char in s:
        if char_count[char] == 1:
            return char
    return "None"

if __name__ == "__main__":
    s = "swiss"
    print("First unique character is:", first_unique_char(s))  # Output: "w"
