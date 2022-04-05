def foo():
    """hello world."""
    
    
    
    print("hello world!")


def bar(x: int, y: int) -> int:
    """hello world.
    
    blah blah blah...
    """
    


    return x + y

# output
def foo():
    """hello world."""
    print("hello world!")


def bar(x: int, y: int) -> int:
    """hello world.

    blah blah blah...
    """
    return x + y
