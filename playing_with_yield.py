def runner(a,b,op):
    yield op(a,b)

print [i for i in runner(5,6,lambda a,b: a+b)]
