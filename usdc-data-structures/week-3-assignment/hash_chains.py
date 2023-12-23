# python3

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev

                return True  # Node deleted
            current = current.next
        return False  # Node not found

    def find(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True  # Node found
            current = current.next
        return False  # Node not found

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
        # store all strings in one list
        self.elems = [DoublyLinkedList() for _ in range(bucket_count)]
        # initialize empty lists 

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        result = ""
        current = chain.head
        while current:
            result += current.data
            if current.next:
                result += " " 
            current = current.next
        if not result:
            print("")
        else:
            print(result)
    
    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(self.elems[query.ind])
        else:
            try:
                string_present = False
                bucket = self._hash_func(query.s)
                chain = self.elems[bucket]
                if chain:
                    string_present = chain.find(query.s)
            except ValueError:
                string_present = False

            if query.type == 'find':
                self.write_search_result(string_present)
            elif query.type == 'add':
                if not string_present:
                    self.elems[bucket].insert_front(query.s)
            else:
                if string_present:
                    self.elems[bucket].delete(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
