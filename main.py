import random
import math
import matplotlib.pyplot as plt
import time
import statistics
import sys
sys.setrecursionlimit(50000)

# dzailanie quicksort w wersji 1
def partition(A, p, r):
    pivot = A[p]
    i = p - 1
    j = r + 1
    while True:
        i += 1
        while A[i] < pivot:
            i += 1

        j -= 1
        while A[j] > pivot:
            j -= 1

        if i >= j:
            return j

        A[i], A[j] = A[j], A[i]

def quicksort(A,p,r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q)
        quicksort(A, q+1, r)


#dzialanie quicksort w wersji2
def quicksort2(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot_index = random.randint(0, len(arr)-1)
        pivot = arr[pivot_index]
        left = []
        right = []
        for i in range(len(arr)):
            if i == pivot_index:
                continue
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort2(left) + [pivot] + quicksort2(right)


#sprawdzenie dzialania funkcji
# tab=[2,3,4,1,4,5,321,4,3,2]
# quicksort2(tab)
# print(tab)



#stworzenie tabeli czasow dla quicksort
# zwykle losowania
N = 200000
czas1=[]
# zwykle losowania dla quicksort
for i in range(5):
    lista = [random.randint(0, N) for i in range(N)]
    start_time = time.time()
    quicksort(lista,0,len(lista)-1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    czas1.append(elapsed_time)
mediana = statistics.median(czas1)
#print(czas1)
print(f"Mediana quicksort1 dla zwyklych liczb losowych: {mediana}")



#stworzenie tabeli czasow dla quicksort2
# zwykle losowania
czas2=[]
for i in range(5):
    lista = [random.randint(0, N) for i in range(N)]
    start_time = time.time()
    quicksort2(lista)
    end_time = time.time()
    elapsed_time = end_time - start_time
    czas2.append(elapsed_time)

#print(czas2)
mediana2 = statistics.median(czas2)
print(f"Mediana quicksort1 dla zwyklych liczb losowych: {mediana2}")



#stworzenie tabeli czasow dla quicksort
# gausowskie losowania dla quicksort
czas3 =[]
for i in range(5):
    lista = [random.gauss(0, N) for i in range(N)]
    start_time = time.time()
    quicksort(lista,0,len(lista)-1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    czas3.append(elapsed_time)

mediana = statistics.median(czas3)
#print(czas1[5:])
print(f"Mediana quicksort1 dla gausowskich losowych: {mediana}")


#stworzenie tabeli czasow dla quicksort2
# gausowskie losowania dla quicksort2
czas4 =[]
for i in range(5):
    lista = [random.gauss(0, N) for i in range(N)]
    start_time = time.time()
    quicksort2(lista)
    end_time = time.time()
    elapsed_time = end_time - start_time
    czas4.append(elapsed_time)

#print(czas2[5:])
mediana2 = statistics.median(czas4)
print(f"Mediana quicksort2 dla gausowskich liczb losowych: {mediana2}")


# funkcja tworzaca prawie posortowana tablice
def generate_list(N):
    lista = [1]
    quantity = N // 20
    start_index = 0
    for i in range(quantity):
        for j in range(20):
            lista.append(lista[-1] + random.randint(1, 5))
        random.shuffle(lista[start_index+1:])
        start_index += 20
    lista.pop()
    return lista


#stworzenie tabeli czasow dla quicksort
# losowanie prawie posortowanej
czas5 =[]
for i in range(5):
    lista3 = generate_list(N)
    start_time = time.time()
    quicksort2(lista3)
    end_time = time.time()
    elapsed_time = end_time - start_time
    czas5.append(elapsed_time)

mediana1 = statistics.median(czas5[1:])
#print(czas1)
print(f"Mediana quicksort1 dla prawie posortowanych tablic: {mediana}")


#stworzenie tabeli czasow dla quicksort2
# losowanie prawie posortowanej 2
czas6 =[]
for i in range(5):
    lista3 = generate_list(N)
    start_time = time.time()
    quicksort2(lista3)
    end_time = time.time()
    elapsed_time = end_time - start_time
    czas6.append(elapsed_time)

mediana2 = statistics.median(czas6[1:])
#print(czas2)
print(f"Mediana quicksort2 dla prawie posortowanych tablic: {mediana2}")




# Tworzenie jednego rysunku z 3 wierszami i 2 kolumnami
plt.figure(figsize=(10, 8))

# Pierwszy wykres
plt.subplot(3, 2, 1)
plt.plot(czas1, label="Quicksort 1")
plt.title("Qicksort1 losowe dane")
plt.xlabel("wyniki funkcji")
plt.ylabel("Czas [s]")
plt.legend()

# Drugi wykres
plt.subplot(3, 2, 2)
plt.plot(czas2, label="Quicksort 2")
plt.title("Qicksort2 losowe dane")
plt.xlabel("wyniki funkcji")
plt.ylabel("Czas [s]")
plt.legend()

# Trzeci wykres
plt.subplot(3, 2, 3)
plt.plot(czas3, label="Quicksort 3")
plt.title("Qicksort1 gausowskie dane")
plt.xlabel("wyniki funkcji")
plt.ylabel("Czas [s]")
plt.legend()

# Czwarty wykres
plt.subplot(3, 2, 4)
plt.plot(czas4, label="Quicksort 4")
plt.title("Qicksort4 gausowskie dane")
plt.xlabel("wyniki funkcji")
plt.ylabel("Czas [s]")
plt.legend()

# Piąty wykres
plt.subplot(3, 2, 5)
plt.plot(czas5, label="Quicksort 5")
plt.title("Qicksort1 prawie posortowane dane")
plt.xlabel("wyniki funkcji")
plt.ylabel("Czas [s]")
plt.legend()

# Szósty wykres
plt.subplot(3, 2, 6)
plt.plot(czas6, label="Quicksort 6")
plt.title("Qicksort2 prawie posortowane dane")
plt.xlabel("wyniki funkcji")
plt.ylabel("Czas [s]")
plt.legend()

plt.tight_layout()

plt.show()
