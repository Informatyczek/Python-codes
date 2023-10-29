import os
import time
import heapq
import funkcja_wyswietlajaca_kopiec


class Product:
    """
    Attributes:
        name (str): The name of the product.
        owner (str): The owner of the product, coresponding with key in users[].
        add_timestamp (int): The Unix timestamp representing the time the product was added.
        expiration_date (int): The number of days until the product expires, counting from the add timestamp.
    """

    def __init__(self, name, owner, add_timestamp, expiration_date):
        self.name = name
        self.owner = owner
        self.add_timestamp = add_timestamp
        self.expiration_date = expiration_date


def min_heapify(heap, i, n):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and heap[left] < heap[smallest]:
        smallest = left

    if right < n and heap[right] < heap[smallest]:
        smallest = right

    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        min_heapify(heap, smallest, n)




# sprawdzenie dzialania kopca
print("sprawdzenie dzialania kopca na przykladach")
tablica = [1, 10, -2, 7, 14]
tab2=tablica[::]
funkcja_wyswietlajaca_kopiec.build_min_heap(tab2)
heapq.heapify(tablica)
print(tablica)
print(tab2)
heapq.heappop(tablica)
tablica.append(15)
funkcja_wyswietlajaca_kopiec.print_tree(tablica)
tablica.remove(15)
tablica.append(2)
funkcja_wyswietlajaca_kopiec.print_tree(tablica)
print("\n\n\n\n\n\n")
# Warunek kopca jest spelniony!!




print("Sortowanie za pomocą kopców")
from funkcja_wyswietlajaca_kopiec import arr
heap = []
for num in arr:
    heapq.heappush(heap, num)
    print("Zawartość kopca:", num)
    funkcja_wyswietlajaca_kopiec.print_tree(heap)
    print()

# Wyświetlenie posortowanych liczb
sorted_numbers = []
while heap:
    sorted_numbers.append(heapq.heappop(heap))

print("Posortowane liczby:")
print(sorted_numbers)
print("\n\n\n\n")


print("dzialanie convert_to_max_heap")
def convert_to_max_heap(heap):
    max_heap = [-x for x in heap]  # Zamiana kolejności elementów na odwrotną
    heapq.heapify(max_heap)  # Utworzenie kopca min
    max_heap = [-x for x in max_heap]  # Zamiana kolejności elementów na odwrotną
    return max_heap
funkcja_wyswietlajaca_kopiec.print_tree(convert_to_max_heap(arr))
# wszystko się zgadza
print("\n\n\n\n")



def funkcja_sortujaca(arr):
    heap=[]
    for num in arr:
        heapq.heappush(heap, num)
    sorted_numbers = []
    while heap:
        sorted_numbers.append(heapq.heappop(heap))


import random
import time
print("sprawdzanie czasu dzialania kopców")
def create_random_heap(N):
    numbers = [random.randint(-1000, 1000) for _ in range(N)]
    heapq.heapify(numbers)
    return numbers

def create_random_heap2(N):
    numbers = [random.randint(-1000, 1000) for _ in range(N)]
    return numbers
sizes = [100, 1000, 1000000]
import time
for N in sizes:
    print(f"heapify() size{N}")
    for i in range(2):
        start_time = time.time()
        heap = create_random_heap(N)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Czas wykonania:", execution_time,"s")
    print(f"heappush() size{N}")
    for i in range(2):
        start_time = time.time()
        heap = create_random_heap2(N)
        funkcja_sortujaca(heap)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Czas wykonania:", execution_time,"s")
    print()
print("\n\n\n\n")


print("użycie kopców dla przypadku sklepu spożywczego: ")
print("wyszukanie przeterminowaych produktow jako funkcja w klasie")
users = {}  # Słownik przechowujący kolejki dla poszczególnych pracowników
outdated_and_free = []  # Kolejka przechowująca przeterminowane produkty
storage = {}  # Słownik przechowujący wszystkie produkty


def add_new_element(user_id, expiration_days, name):
    current_time = int(time.time())
    expiration_date = current_time + (expiration_days * 24 * 60 * 60)

    if user_id not in users:
        users[user_id] = []  # Nie ma goscia

    product = Product(name, user_id, current_time, expiration_days)
    element = (expiration_date, product)  # Tworzenie elementu do dodania do kolejki
    heapq.heappush(users[user_id], element)

    storage[element] = name  # Dodanie elementu do słownika storage, gdzie kluczem jest wygenerowany element


def no_spoilled_food(now):
    for user_queue in users.values():
        while user_queue and user_queue[0][0] > now:
            element = heapq.heappop(user_queue)
            heapq.heappush(outdated_and_free, element)

    # Usuwanie przeterminowanych produktów z kolejki outdated_and_free
    one_day = 24 * 60 * 60
    while outdated_and_free and outdated_and_free[0][0] >= now + one_day:
        element = heapq.heappop(outdated_and_free)
        del storage[element]


def holidays(user_id, vacation_start, vacation_end):
    vacation_start = int(vacation_start)
    vacation_end = int(vacation_end)

    if user_id in users:
        user_queue = users[user_id]
        products_to_move = []

        for element in user_queue:
            expiration_date = element[0]
            product = element[1]

            if vacation_start <= expiration_date <= vacation_end:
                products_to_move.append(element)

        for element in products_to_move:
            user_queue.remove(element)
            heapq.heappush(outdated_and_free, element)


add_new_element("user1", 5, "Apple")
add_new_element("user1", 3, "Banana")
add_new_element("user2", 7, "Orange")
add_new_element("user2", 4, "Grapes")
add_new_element("user1", 8, "Appleo")
add_new_element("user1", 98, "Bananao")
add_new_element("user2", 22, "Orangeo")
add_new_element("user2", -1, "Grapeso")
add_new_element("user2", -4, "Expired Grapes")
def print_products(user_id):
    if user_id in users:
        user_queue = users[user_id]
        print(f"User: {user_id}")
        for element in user_queue:
            product = element[1]
            print(f"Product: {product.name}, Expiration Date: {element[0]}")
    else:
        print(f"User {user_id} not found")


print_products("user1")


def print_expired_products(user_id):
    if user_id in users:
        user_queue = users[user_id]
        print(f"Expired Products for User: {user_id}")
        for element in user_queue:
            expiration_date = element[0]
            current_time = int(time.time())
            if expiration_date < current_time:
                product = element[1]
                print(f"Product: {product.name}, Expiration Date: {element[0]}")
    else:
        print(f"User {user_id} not found")


print_expired_products("user1")
print()

print_expired_products("user2")
