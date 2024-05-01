from urllib.request import urlopen

response = urlopen("http://127.0.0.1:9000/romeo.txt")

for line in response:
    print(line.decode(), end="")
