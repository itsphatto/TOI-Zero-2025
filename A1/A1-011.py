def theos(text):
    if not text.isalpha():
        return None

    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += str(count) + text[i - 1]
            count = 1

    result += str(count) + text[-1]
    return result


text = input("")
print(theos(text))
