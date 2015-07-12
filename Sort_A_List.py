def sort_list():
    myfile =  open("C:\Users\phill_000\Desktop\Python Projects\ThomasPaineQuotes.txt") 
    list1 = list(myfile.read().split())
    print(sorted(list1))

sort_list()
