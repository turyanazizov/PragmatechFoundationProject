def split_and_join(text):
    for char in text:
        if char==' ':
            text=text.replace(char,'-')
    return text

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)