# 1b ,2b,3#,4a,5c,6a,7c,7d,8c,9a,10d,11b,12b,



# 13.Массив:Бүх элементүүийг дараалсан санах ойд хадгалдаг
# Өгөгдлийг хадгалах арга:
# Массив: Бүх элементүүдийг дараалсан санах ойд хадгалдаг.
# Холбоослогдсон жагсаалт: Элементүүдийг тусдаа санах ойд хадгалж, холбоосоор холбосон байдаг.
# санах ой:
# Санах ой:
# Массив: Нэг хэмжээст массивд бүх элементүүдийг олоход хурдан (O(1)).
# Холбоослогдсон жагсаалт: Элемент олохын тулд нэгдүгээрээс нь эхэлж (O(n)) явна.
# Мэдээллийг боловсруулах хурд:
# Мэдээллийг боловсруулах хурд:
# Массив: Хурдан бөгөөд уян хатан. Гэсэн хэдий ч, хэмжээ нэмэгдэхэд дахин тохируулах шаардлагатай.
# Холбоослогдсон жагсаалт: Олон үйлдлийг гүйцэтгэхэд хялбар, гэхдээ элемент олох, дахин давталт хийхэд удаан.




# 14.
# Стек:

# Хэрхэн ажилладаг: LIFO (Last In, First Out) зарчмаар ажилладаг. Сүүлийн оруулсан элемент хамгийн түрүүнд гарч ирнэ.
# Жишээ: Сайтын "Undo" функцийг ажиллуулахад ашиглагддаг.
# Давуу тал: Саруулж ойлгоход хялбар, хурдан (O(1)) үйлдлүүд.
# Сул тал: Зөвхөн дээд хэсэгт ажилладаг, бусад элементүүдийг шууд олох боломжгүй.

# Мод:

# Хэрхэн ажилладаг: Тодорхой бүтэцтэй, ихэвчлэн олон давхарга, олон салбартай.
# Жишээ: Хайлт хийхэд (жишээ нь, хоёртын хайлтын мод).
# Давуу тал: Мэдээллийг зохион байгуулах, хялбархан хайлт хийх боломжтой.
# Сул тал: Зэрэгцээгээ алдахад үйлдлүүд удаан болох боломжтой.




# 15c
# 16a
# 17b
# 18c




# Даалгавар1:Минимум зоосны тоо:
# def greedy_coin_change(amount):
#     coins = [25, 10, 5, 1]
#     coin_count = {}
#     for coin in coins:
#         if amount >= coin:
#             count = amount // coin
#             coin_count[coin] = count
#             amount -= count * coin

#     return coin_count

# amount = 83
# result = greedy_coin_change(amount)

# for coin, count in result.items():
#     print(f"{count}x{coin} төгрөг")




# Асуулт 1: Грэйди алгоритмын
# дагуу хамгийн бага зоосны тоог
# хэрхэн сонгох вэ? (C)




# Асуулт 2: (b)





# Даалгавар2:
# import heapq
# from collections import defaultdict

# class Node:
#     def __init__(self, char, freq):
#         self.char = char
#         self.freq = freq
#         self.left = None
#         self.right = None
    
#     def __lt__(self, other):
#         return self.freq < other.freq

# def huffman_code(frequencies):
#     heap = [Node(char, freq) for char, freq in frequencies.items()]
#     heapq.heapify(heap)
    
#     while len(heap) > 1:
#         left = heapq.heappop(heap)
#         right = heapq.heappop(heap)
#         merged = Node(None, left.freq + right.freq)
#         merged.left = left
#         merged.right = right
#         heapq.heappush(heap, merged)
    
#     root = heap[0]
#     huffman_codes = {}
    
#     def generate_codes(node, current_code):
#         if node is None:
#             return
#         if node.char is not None:
#             huffman_codes[node.char] = current_code
#         generate_codes(node.left, current_code + "0")
#         generate_codes(node.right, current_code + "1")
    
#     generate_codes(root, "")
#     return huffman_codes

# frequencies = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
# x = huffman_code(frequencies)

# for char, code in x.items():
#     print(f"{char}: {x}")






# Даалгавар3:
# import time

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
# input_array = [64, 34, 25, 12, 22, 11, 90]

# # Bubble Sort
# start_time = time.time()
# bubble_sorted = bubble_sort(input_array.copy())
# bubble_time = time.time() - start_time

# # Insertion Sort
# start_time = time.time()
# insertion_sorted = insertion_sort(input_array.copy())
# insertion_time = time.time() - start_time

# print("Bubble Sort үр дүн:", bubble_sorted)
# print("Insertion Sort үр дүн:", insertion_sorted)
# print(f"Bubble Sort хугацаа: {bubble_time:.6f} секунд")
# print(f"Insertion Sort хугацаа: {insertion_time:.6f} секунд")





# 3. Алгоритмын гүйцэтгэлийн
# шинжилгээ

# Асуулт 1: О(n) гэж юуг
# илэрхийлдэг вэ?

# с) Алгоритмын хамгийн бага
# гүйцэтгэл






# Даалгавар4:
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.val

    def find_max(self, root):
        current = root
        while current.right is not None:
            current = current.right
        return current.val

values = [20, 9, 25, 5, 12, 15, 30]
bst = BinarySearchTree()
root = None

for value in values:
    root = bst.insert(root, value)

print("Minimum value:", bst.find_min(root))
print("Maximum value:", bst.find_max(root))

search_results = [12, 18]
for search_value in search_results:
    result = bst.search(root, search_value)
    if result:
        print(f"Search {search_value}: Found")
    else:
        print(f"Search {search_value}: Not found")
