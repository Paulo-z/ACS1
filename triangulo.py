n = int (input())
letter = 'A'

for line in range (1, n+1):
    print(letter * line)
    letter = chr(ord(letter)+1)