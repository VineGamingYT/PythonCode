movies = ["Interstellar", "Shutter Island", "Forrest Gump", "Inception"]

def count(a,i=0):
    if (i == len(a)):
        return
    print(a[i])
    count(a,i+1)

count(movies)