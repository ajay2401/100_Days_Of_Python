# Syntax and Concepts

    Lists -> Data Structure that stores group of data that has some sort of connection with each other. ARRAY.

    Index -> The data inside the lists are called index. 
    
        Startes from 0..n, beacuse the second item in the list has an offset of 1 from the start, that is why indexes start from 0 and not 1.


<!-- Syntax: --> 

        fruits = ["Cherry","Apple","Orange"]

        print(fruits[1]) - Apple
        
        print(fruits[-1]) - Orange

        fruits[0] = "Blueberry" -> will change ["Blueberry","Apple","Orange"]

        veggies = ["carrot","beans"]

        mix = [fruits,veggies] -> will give a nested list. [["Blueberry","Apple","Orange"],["carrot","beans"]]

        mix[1][1] - beans # since mix[1] will give veggies list and veggies[1] = beans.

# Lists

    1. list.append("Pear") -> adds value at end of list

    2. list.extend(["Guava","Mango"]) -> appends given list to ours at the end

    3. list.insert(target_index, value) -> inserts given value before the given target index

    4. list.remove() -> removes the first index from list

    5. list.pop() -> pops the last index if index not mentioned

        list.pop(3) -> removes the value from the given index

    6. list.clear() -> clears the array.

    7. list.index() -> finds the position (index) of a value in a list.

        a. list = [10,20,30]
            list.index(20) - 1

        b. list = [1,2,3,2,4]
            list.index(2,2,len(list)) - 3

                This syntax is like slicing - list.index(Target Value, Start Index, Stop Index)

    8. list.count() -> returns the number of times a values appears in the list

    9. list.sort() -> sorts the original array

        list = [3,2,1]
        list.sort() - [1,2,3]

        list = [1,2,3]
        list.sort(reverse=True) - [3,2,1]

        list = ["apple", "kiwi", "banana"]
        list.sort(key=len) - ["kiwi","apple","banana"] #based on the length of value it sorts

        x = list.sort() will sort the list
        print(x) - will return none since original array only will be sorted

        sorted(list) -> returns the sorted array in a new list, unlike sort() which changes the original array

    10. list.revers() -> reverse the values of array without sorting. 

        list = [1,3,2]
        list.reverse() - [2,3,1]

        x = list.reverse() - will reverse the list literally without sorting
        print(x) - will return none since original array only will be reversed

# list.sort() vs sorted(list)

| list.sort()           | sorted()              |
| --------------------- | --------------------- |
| Changes original list | Returns new list      |
| Faster                | Slightly slower       |
| Works only on lists   | Works on any iterable |

# The Concept of Randoms in Python

    import random -> import is the keyword for importing modules into our script

    1. random.randint() -> Gives a random integer between given values

        a. random.randint(1,10) works like 1 <= X >= 10, where X is the int generated

        b. Ex: random.randint(1,10)

    2. random.random() -> Gives a random floating point from 0 to 1.0 unless multiplied to a certain range

        a. random.random() works like 0.0 <= X > 1.0 where X is the float generated. 

            Notice how X is lesser than 1.0 and not equal to as in random.randomint()

        b. random.random() does not take inputs and can be used only like:

            random.random() * 10, given 0.0 <= X > 10

    3. random.uniform() -> Gives a random float between given values

        a. random.uniform(1,10) works like 1.0 <= X >= 10.0, where X is the float generated

        b. Ex: random.uniform(1,10)

    4. random.choice() -> Gives a random value from a sequence or list

        a. random.choice(["a","b","c"]) gives b or a or c randomly

    5. random.shuffle() -> Shuffles the elements of a list

        a. random.shuffle(["a","b","c"]) gives c,b,a or b,c,a randomly

# random.choice() vs random.shuffle()

    | Function    | Returns | Modifies original? |
    | ----------- | ------- | ------------------ |
    | `choice()`  | element | ❌ No               |
    | `shuffle()` | `None`  | ✅ Yes              |


# Points to Remember



