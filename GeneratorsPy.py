#GENERATORS:
"""we use iterators to print or fetch one value at a time.there are small issues with iterators . you need to create the iterator, you have to define those two functions 1.iter() 2.__next__().
we dont want to do that python to do it for us and that's where python says ok if you want iterators we will give you generators.
Generators will give you iterators.
How exactly we create generators?
instead of return we will use yield.
yield is a special keyword which will make your functions as a generator."""
def top():
    yield 5
val=top()
print(val)   #it will give object of generator.
#it will give 5 
print(val.__next__())  #you knows if you want to fetch something for an iterator we have to use the next function.
"""return also you can print 5 , yield also return the value but it will return in the format of iterator.
return also give the same output, but there is a difference. In yield since its a generator which will give you iterator you can write multiple yield statements."""
def Top():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
vals=Top()
print(next(vals))
#so this is same as iterator. when you are getting multiple values. so you got your own iterator without using next& iter function.
#loop
for i in vals:
      print(i)


#i want to print top 10 perfect square.
print("perfect squares from 1 to 10")
def topP():
    n=1
    while n<=10:     #we want perfect square we use loop. i did not use for here, because indirectly for is an iterator.
        sq=n*n
        yield sq     #when return executes it terminates the function, but yield will not.
        n+=1
values=topP()
for i in values:
    print(i)


#why will use generators.
"""
you are fetching 1000 records from the database, so when you say you are fetching 1000 records may be you want to print all or may be you want to process something from those records.
it means the 1000 records will be loaded in your memory. we dont want that. may be you want to work with one value at a time. In that case you can use generator that instead of using or
instead of fetching the entire list you can fetch one by one value.
"""
#differences Yield vs return:
"""
The return statement is used to exit a function and pass a value back to the caller. Once return is executed, the function terminates.
yield is used in a generator to produce a sequence of values over time without terminating the function. """
