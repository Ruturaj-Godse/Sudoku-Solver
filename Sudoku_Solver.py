import random
import time
start_time = time.time()
adj = [[] for _ in range(81)]
row = [0 for _ in range(9)]
graph = [row.copy() for _ in range(9)]


def make_graph():
    for i in range(9):
        for j in range(9):
            cell_ind = i*9 + j

            for r in range(9):
                if r==i:
                    continue
                ind = r*9 + j
                adj[cell_ind].append(ind)

            for c in range(9):
                if c==j:
                    continue
                ind = i*9 + c
                adj[cell_ind].append(ind)

            lc = (j//3)*3
            tr = (i//3)*3

            for r in range(tr, tr+3):
                for c in range(lc, lc+3):
                    if r==i and c==j:
                        continue
                    ind = r*9 + c
                    adj[cell_ind].append(ind)

def add_values():
    file = open("sudoku_table.csv", "r")
    lines = file.readlines()
    i = 0
    for line in lines:
        row = line.strip().split(',')
        for j in range(9):
            graph[i][j] = int(row[j])
        i+=1
    '''
    while True:
        print("Enter 0-based co-ord and value (x y v): ")
        text = input()
        if text=="":
            break
        x, y, v = map(int, text.split())
        graph[x][y] = v
    '''
    file.close()

def fill_graph():
    count_0 = 0
    for _ in range(81):
        change = 0
        for min_len in range(1, 10):
            for cell_ind in range(81):
                r = cell_ind//9
                c = cell_ind%9
                if graph[r][c]!=0:
                    continue

                possible_values = [i for i in range(1, 10)]
                for neigh in adj[cell_ind]:
                    r = neigh//9
                    c = neigh%9
                    if graph[r][c] in possible_values:
                        possible_values.remove(graph[r][c])

                if len(possible_values)==min_len:
                    r = cell_ind//9
                    c = cell_ind%9
                    graph[r][c] = random.choice(possible_values)
                    change = 1
                    #print(min_len)
                    break
            if change>0:
                break
        count_0 = 0
        for i in range(9):
            for j in range(9):
                if graph[i][j]==0:
                    count_0+=1
                    break
        if count_0==0:
            break

    return count_0

def print_graph():
    for i in range(9):
        print(*graph[i])

if __name__=="__main__":

    make_graph()
    add_values()
    trial = 0
    while True:
        #print(trial)
        add_values()
        cnt0 = fill_graph()
        if cnt0==0:
            print(trial)
            break
        trial+=1
    print_graph()
    #print()
    #print(adj[0])
    end_time = time.time()
    print(end_time-start_time)

