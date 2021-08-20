from time import sleep

loopstr = input('모스부호 SVG를 제작할 글자들을 띄어쓰기 없이 입력해주세요.\n(영문 알파벳과 숫자만 가능)\n').upper()
morsedict = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
"K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
"U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--",
"4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----"}

for filename in loopstr:
    morse = morsedict.get(filename)
    morselen = len(morse)
    fulllen = (morselen - 1) * 144 + morse.count('.') * 48 + morse.count('-') * 144

    f = open('./' + filename + '.svg', 'w')

    f.write('<?xml version="1.0" encoding="iso-8859-1"?>\n')
    f.write('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"\n')
    f.write('	 viewBox="0 0 ' + str(fulllen) + ' 800" style="enable-background:new 0 0 143.947 799.994;" xml:space="preserve">\n')
    f.write('<g id="모스부호">\n')

    path = 'M0,0'
    loopnum = 0
    for chr in morse:
        loopnum = loopnum + 1
        if chr == '.': path = path + 'h48v800h-48v-800z'
        if chr == '-': path = path + 'h144v800h-144v-800z'
        if loopnum != morselen:
            if chr == '.': path = path + 'm96,0'
            if chr == '-': path = path + 'm192,0'

    f.write('	<path d="' + path + '"/>\n')

    f.write('</g>\n')
    f.write('</svg>')

    f.close()

    print(filename + '.svg 생성 완료.')
    sleep(1)

print('모든 작업이 완료되었습니다.')
sleep(5)
print('프로세스를 종료합니다.')