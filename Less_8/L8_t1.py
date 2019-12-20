# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

# лемма о рукопожатиях (https://www.youtube.com/watch?v=TaT5O8tgwo0)
# m - число ребер
# n - число вершин
# для полного графа (т.е. у графа, у которого все вершины соединены между собой)
# число ребер(соединений) равно
# 2m = n (n - 1)

N = int(input('введите число здоровующихся '))
m = int(N * (N - 1) / 2)
print(f'число руокпожатий у {N} здоровующихся будет {m}')