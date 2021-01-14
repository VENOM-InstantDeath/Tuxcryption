def caen(s: str, k: int) -> str:
    o = ""
    for i in s:
        if i.islower():
            o += chr((ord(i)+k-97)%26+97)
        elif i.isupper():
            o += chr((ord(i)+k-65)%26+65)
        else:
            o += i
    return o

def cade(s: str, k: int) -> str:
    o = ""
    for i in s:
        if i.islower():
            o += chr((ord(i)-k-97)%26+97)
        elif i.isupper():
            o += chr((ord(i)-k-65)%26+65)
        else:
            o += i
    return o

if __name__ == "__main__":
    import color
    print(f"\t\t{color.red}Caesar cypher{color.nm}\n\n")
    print("[1]Encrypt text\n[2]Decrypt text\n")
    opt = input("Option: ")
    if opt == "1":
        s=input("\ninput string: ")
        k=int(input("input key (1-10): "))
        print(f"\n\noutput: {caen(s,k)}")
    elif opt == "2":
        s=input("\ninput string: ")
        k=int(input("input key (1-10): "))
        print(f"\n\noutput: {cade(s,k)}")
    else:
        print(f"\n\n{color.red}Option does not exist{color.nm}\n")

