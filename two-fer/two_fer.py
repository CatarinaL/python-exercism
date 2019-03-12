def two_fer(name=None):
    #to have name as optional parameter, default name=None
    if name is None: #test None with is, not ==
        name = "you"
    return f"One for {name}, one for me."
