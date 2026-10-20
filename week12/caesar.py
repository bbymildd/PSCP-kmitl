"""Caesar"""
def main():
    """Caesar"""
    text = input()
    word = [
        "what", "when", "why", "which", "this", "there",
        "where", "the", "is", "am", "are", "you", "we",
        "they", "he", "she", "it"
    ]

    best_text = text
    max_count = -1

    for shift in range(26):
        result = ""

        for char in text:
            if "a" <= char <= "z":
                result += chr((ord(char) - ord("a") - shift) % 26
                              + ord("a"))
            elif "A" <= char <= "Z":
                result += chr((ord(char) - ord("A") - shift) % 26
                              + ord("A"))
            else:
                result += char

        words = result.lower().split()
        count = 0

        for item in words:
            item = item.strip(".,!?;:")
            if item in word:
                count += 1

        if count > max_count:
            max_count = count
            best_text = result

    print(best_text)

main()
