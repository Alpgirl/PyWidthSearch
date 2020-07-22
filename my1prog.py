graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
def person_is_celler(name):
    return name[-1] == 'j'
def search(name):
    from collections import deque
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_celler(person):
                print (person, "is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
search("bob")
