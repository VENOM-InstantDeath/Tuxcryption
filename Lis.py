import color
import re

#5(°-°)h%1@0$^e%1@1$^l%2@2$3$^o%1@4$^

def plist(letter: str, word: str) -> list:
    l = []
    for i in range(len(word)):
        if word[i] == letter:
            l.append(i)
    return l

def dlist(x: list) -> list:
    x=x.split('$')
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def encrypt(x: str) -> str:
    pd = []
    pp = {}
    for i in range(len(x)):
        if i not in pd:
            pd.append(x[i])
            pp[x[i]] = plist(x[i], x)
    s = f"{len(x)}(°-°)"
    for i in pp:
        s += f"{i}%{len(pp[i])}@"
        r = str(pp[i]).replace('[', '')
        r = r.replace(']', '')
        r = r.replace(',', '')
        r = r.replace(' ', '$')
        s += f"{r}$^"
    f=open("debug", 'w+'); f.write(str(pp));f.close()
    f=open("output", 'w+'); f.write(str(s));f.close()
    return s


def decrypt(x: str) -> str:
    size = re.match('[0-9]+', x).group()
    print(size)
    lis = {}
    text = []
    res = ""
    for i in range(int(size)):
        text.append(0)
    x = x[len(size)+5:]
    x = x.split('$^');x.pop()
    for i in range(len(x)):
        lis[x[i].split("%")[0]] = dlist(re.split('[0-9]@', x[i])[1])
    for i in lis:
        for e in lis[i]:
            text[e] = i
    for i in text:
#        print(i)
        res += str(i)
    return res


if __name__ == "__main__":
    print(f"\t\t{color.red}Cry{color.nm}\n\n[1]Encriptar texto\n[2]Desencriptar texto\n\n")
    opt = input("Opción: ")
    if opt == "1":
        text = input("\nTexto: ")
        print(f"\n\t\t{color.red}Texto encriptado{color.nm}\n\n")
        print(encrypt(text))
    elif opt == "2":
        print()
        text = input("Texto: ")
        print(f"\n\t\t{color.red}Texto desencriptado{color.nm}\n\n")
        print(decrypt(text))
    elif opt == "3":
        t=input()
        print(decrypt(t))
    else:
        print(f"\n{color.red}Opción inexistente.{color.nm}")

#t=input()
#print(decrypt(t))

