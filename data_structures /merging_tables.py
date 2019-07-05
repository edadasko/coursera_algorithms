'''
Merging tables
Task. There are n tables stored in some database. The tables are numbered from 1 to n.
      All tables share the same set of columns. Each table contains either several rows
      with real data or a symbolic link to another table. Initially, all tables contain data,
      and i-th table has ri rows. You need to perform m of the following operations:
      1. Consider table number destination(i). Traverse the path of symbolic links to get
      to the data.
      2. Consider the table number source(i) and traverse the path of symbolic links
      from it in the same manner as for destination(i).
      3. Now, destination(i) and source(i) are the numbers of two tables with real data.
      If destination(i) != source(i), copy all the rows from table source(i) to table
      destination(i), then clear the table source(i) and instead of real data put a symbolic
      link to destination(i) into it.
      4. Print the maximum size among all n tables (recall that size is the number of rows
      in the table). If the table contains only a symbolic link, its size is considered to be 0.
Input Format. The first line of the input contains two integers n and m — the number of tables
              in the database and the number of merge queries to perform, respectively.
              The second line of the input contains n integers ri — the number of rows in the i-th table.
              Then follow m lines describing merge queries. Each of them contains two integers
              destination(i) and source(i) — the numbers of the tables to merge.
Output Format. For each query print a line containing a single integer — the maximum of the sizes of all
               tables (in terms of the number of rows) after the corresponding operation.
'''
import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
parents = list(range(0, n))
max_lines = max(lines)


def get_root(node):
    while node != parents[node]:
        node = parents[node]
    return node


def merge(destination, source):
    real_destination = get_root(destination)
    real_source = get_root(source)
    
    if real_destination == real_source:
        return False

    lines[real_destination] += lines[real_source]

    global max_lines
    if lines[real_destination] > max_lines:
        max_lines = lines[real_destination]

    lines[source] = lines[real_destination]
    p = parents[source]
    parents[source] = real_destination

    while p != parents[p]:
        lines[p] = lines[real_destination]
        new_p = parents[p]
        parents[p] = real_destination
        p = new_p
    
    parents[p] = real_destination
    return True


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(max_lines)
