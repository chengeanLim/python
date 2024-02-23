#알파벳이면 더하고, 아니면 소문자로 변환을 하는 명령어
def process(w):
    output =""
    
    for ch in w:
        if ch.isalpha():
            output += ch

    return output.lower()


words = set()
fname = input("파일 이름 입력:")
file = open(fname, "r")


#띄어쓰기 기준으로 split을 이용해 단어를 다가져온다.
for line in file:
    lineWords = line.split()

    for word in lineWords:
        words.add(process(word))

print("사용된 단어의 개수 =", len(word))
print(words)
