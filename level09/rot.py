import sys

content = enumerate(sys.argv[1].encode(encoding="utf-8", errors="surrogateescape"))
for i, character in content:
    print(chr(character - i), end="")
