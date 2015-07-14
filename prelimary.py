def fizzbuzz(intList):
    '''
    Your fizzbuzz function. The grader will run `fizzbuzz(intList)` to check if your
    function returns the correct output.
    
    intList: list containing integers

    Make sure you write the script so that your algorithm is part of the
    function; you do not need to call the function yourself.
    '''
    list =[]

    # YOUR CODE HERE
    for x in intList:
        if x%3==0 and x%5==0:
            list.append("FizzBuzz")
        elif x%3==0:
            list.append("Fizz")
        elif x%5==0:
            list.append("Buzz")
        else:
            list.append(x)
       
    return list

intList=[3, 15, 9, 10]
print(fizzbuzz(intList))
