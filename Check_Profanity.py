import urllib

def read_text():
    quotes = open("C:\Users\phill_000\Desktop\Python Projects\ThomasPaineQuotes.txt")
    content= quotes.read()
    quotes.close()
    check_profanity(content)


def check_profanity(content):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+content)
    output = connection.read()
    print(output)

read_text()
