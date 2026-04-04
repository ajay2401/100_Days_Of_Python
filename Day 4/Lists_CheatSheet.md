# LISTS CHEATSHEET


| Function            | Description                                      | Example -> Output                          |
|---------------------|--------------------------------------------------|--------------------------------------------|
| list.append(x)      | adds value at end of list                        | [1,2].append(3) -> [1,2,3]                 |
| list.extend(iter)   | appends given list items to ours at the end      | [1,2].extend([3,4]) -> [1,2,3,4]           |
| list.insert(i, x)   | inserts value before given index                 | [1,3].insert(1,2) -> [1,2,3]               |
| list.remove(x)      | removes first matching value from list           | [1,2,2].remove(2) -> [1,2]                 |
| list.pop([i])       | removes and returns item (last if no index)      | [1,2,3].pop() -> 3                         |
|                     |                                                  | [1,2,3].pop(1) -> 2                        |
| list.clear()        | removes all values from list                     | [1,2].clear() -> []                        |
| list.index(x)       | gives index of first matching value              | [10,20,30].index(20) -> 1                  |
| list.count(x)       | counts how many times value appears              | [1,2,2,3].count(2) -> 2                    |
| list.sort()         | sorts list in ascending order                    | [3,1,2].sort() -> [1,2,3]                  |
| list.sort(reverse=True) | sorts list in descending order             | [1,2,3].sort(reverse=True) -> [3,2,1]      |
| list.sort(key=...)  | sorts list based on given rule (like length)     | ["apple","kiwi"].sort(key=len) -> ["kiwi","apple"] |
| sorted(list)        | returns new sorted list without changing original| sorted([3,1,2]) -> [1,2,3]                 |
| list.reverse()      | reverses list order without sorting              | [1,3,2].reverse() -> [2,3,1]               |
