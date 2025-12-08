def total(*args, **kwargs):
    print(args)      # tuple
    print(kwargs)    # dict
total(1,2,3, x=4, y=5)