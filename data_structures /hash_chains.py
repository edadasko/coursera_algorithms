'''
Hashing with chains
Task. In this task your goal is to implement a hash table with lists chaining.
      You are already given the number of buckets m and the hash function.
      Your program should support the following kinds of queries:
      add string, del string, find string, check i — output the content
      of the i-th list in the table.
Input Format. There is a single integer m in the first line — the number
              of buckets you should have. The next line contains the number
              of queries N. It’s followed by N lines, each of them contains
              one query in the format described above.
Output Format. Print the result of each of the find and check queries,
               one result per line, in the same order as these queries
               are given in the input.
'''

class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007
    
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.hash_table = [[] for i in range(bucket_count)]
    
    def hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count
    
    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')
    
    def write_chain(self, chain):
        print(' '.join(chain))
    
    def read_query(self):
        return Query(input().split())
    
    def process_query(self, query):
        if query.type == 'add':
            index = self.hash_func(query.s)
            if query.s not in self.hash_table[index]:
                self.hash_table[index].insert(0, query.s)
        elif query.type == 'del':
            index = self.hash_func(query.s)
            if query.s in self.hash_table[index]:
                self.hash_table[index].remove(query.s)
        elif query.type == 'find':
            index = self.hash_func(query.s)
            self.write_search_result(query.s in self.hash_table[index])
        else:
            self.write_chain(self.hash_table[query.ind])

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


bucket_count = int(input())
proc = QueryProcessor(bucket_count)
proc.process_queries()
