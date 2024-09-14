'''
GrPA 2 - Operations on list and set - GRADED
List mutating operations - This will help you learn the list methods and operations that will modify the list inplace. Note that you should not be creating a new list anywhere in this function.
Create new lists - This will help you learn how to create new lists that resembles the result of above operations but does not affecting the original list.
Set operations - This will help you learn things that you can do with sets.
'''

#answer

# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <noloop>")[2]
if "for " in content or "while " in content:
    print("You should not use for loop, while loop or the word for and while anywhere in this exercise")

# note that apart from the print statements inside the functions, the evaluator will also print what is returned by the function at last
# <noloop>

def list_mutating_operations(items:list, item1, item2):
    # sort the items inplace
    items.sort()
    print("sorted:",items)

    # add item1 to the items at the end
    items.append(item1)
    print("append:",items)

    # add item2 at index 3
    items.insert(3, item2)
    print("insert:",items)

    # extend items with the first three elements in items
    items.extend(items[:3])
    print("extend:", items)

    # pop the fifth element and store it in variable popped_item
    if (len(items) >= 5):
        popped_item = items.pop(4)
    else:
        popped_item = None
    print("pop:",items)

    # remove first occurance of item2 from the list
    if (item2 in items):
        items.remove(item2)
    print("remove:",items)

    # make the element at index 4 None
    if (len(items) > 4):
        items[4] = None
    print("modify_index:",items)

    # make the even indices None
    items[::2] = [None] * len(items[::2])
    print("modify_slice:",items)

    # delete the third last element
    if (len(items) >= 3):
        del items[-3]
    print("delete_index:",items)

    # delete the even indices
    del items[::2]
    print("delete_slice:",items)

    return items, popped_item 

def list_non_mutating_operations(items:list, item1, item2):

    original_items = items.copy()

    # print the sorted version of items
    print("sorted:",sorted(original_items))

    # print a list with item1 appended to the items at the end
    print("append:",original_items + [item1])

    # print a list with item2 added to items at index 3
    new_items = original_items.copy() 
    new_items.insert(3, item2)
    print("insert:", new_items)

    # print a list with the first three elements in items added to the end of the items again
    print("extend:", original_items + original_items[:3])

    #  print a list with the fifth element from items removed
    if (len(original_items) >= 5):
        new_items = original_items.copy()
        del new_items[4]
        print("pop:", new_items)
    else:
        print("pop:", original_items)

    # print a list with first occurance of item2 removed from items
    if (item2 in original_items):
        new_items = original_items.copy()
        new_items.pop(original_items.index(item2))
        print("remove:",new_items) # hint: you may want to use index
    else:
        print("remove:",original_items)

    # print a list with the fourth element of items changed to None
    if (len(original_items) > 4):
        new_items = original_items.copy()
        new_items[3] = None
    print("modify_index:",new_items)

    # print a list with the even indices changed to None
    new_items = original_items.copy()
    new_items[::2] = [None] * len(new_items[::2])
    print("modify_slice:",new_items)

    # print a list with the even indices removed
    new_items = original_items.copy()
    del new_items[::2]
    print("delete_slice:",new_items)

    return items

def do_set_operation(set1, set2, set3, item1, item2):
    # add item1 to set1
    set1.add(item1)
    print(sorted(set1))

    # remove item2 from set1. What if item2 is not in set1?
    set1.discard(item2)
    print(sorted(set1))

    # add elements from set2 to set1
    set1.update(set2)
    print(sorted(set1))

    # remove all elements from set1 that are in set3
    set1 -= set3
    print(sorted(set1))

    # print the common elements in both set2 and set3 as a sorted list.
    print(sorted(set2 & set3))

    #print all unique elements present in set1, set2 an set3 as a sorted list
    print(sorted(set1 | set2 | set3))

    #print all unique elements that are in set2 but not in set3 as a sorted list
    print(sorted(set2 - set3))

    #print all the non common elements from both set2 and set3
    print(sorted((set2 - set3) | (set3 - set2)))

    return set1,sorted(set1),sorted(set2),sorted(set3)