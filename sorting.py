arr=[1,2,3,5,6]
arr.sort()
print(arr)


arr.sort(reverse=True)
print(arr)

"""tri chaine et longueur de chaine """
arr=["alice","bob","charles","david","zinedine"]
arr.sort()
print(arr)

""" longueur"""
arr.sort(key=lambda x: len(x))

