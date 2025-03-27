#Write using 'with' - doing so file open and close is not required.

with open("cmd.txt",'r') as reader:
    line=reader.readlines()

    with open('cmd.txt','w') as writer:
        for l in reversed(line):
            writer.write(l)


