import webbrowser
import time

total_break = 3;
current_break = 0;

print("the program time is now: " + time.ctime())
while( current_break < total_break):
    time.sleep(2)
    webbrowser.open('https://www.google.com/')
    current_break = current_break+1
