def format_text(w):
    import re

    words = re.findall(r'\w+|\s+|,', w)

    max_word_length = max(len(word.rstrip(',')) for word in words if word.strip() and word != ',')
    max_len = max_word_length * 3

    lines = []
    current_line = ''
    current_length = 0

    new_words = []
    for i in range(len(words)):
        if words[i] == ',' and new_words:
            j = -1
            while new_words[j].isspace():
                j -= 1
            new_words[j] += ','
        else:
            new_words.append(words[i])
    for word in new_words:
        if word.isspace():
            continue
        
        word_length = len(word)

        if current_length + word_length + 1 > max_len:
            lines.append(current_line.strip())
            current_line = word
            current_length = word_length
        else:
            if current_line:
                current_line += ' '
                current_length += 1

            current_line += word
            current_length += word_length

    if current_line:
        lines.append(current_line.strip())

    for line in lines:
        print(line.strip())

# input_text = input()
# format_text(input_text)



input_text = "once upon a time, in a land far far away lived a princess , whose beauty was yet unmatched"
format_text(input_text)

input_text = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,yandex"
format_text(input_text)

input_text = "xp,bd,l"
format_text(input_text)

