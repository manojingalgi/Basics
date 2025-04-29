#exp1 of litsts
mylists1=[10,20,30,40,50]
mylists2 = ["apple","mango","orange"]
mylists3 =[1,2,"aaple",8,"blore","hyd", "jaipur"]
mylists4 =list()
#
# print(mylists3[-2])

newlists = ['apple','banana','chiku','jira', 'cashew','dal','nuts', 'veggies', "jiuce"]
#print(newlists[2:5])  #['chiku', 'jira', 'cashew']

# newlists[0] = 'donut' #adding elements in list by index
# print(newlists)

# read elements
# for i in newlists:
#     print(i)

# newlists.insert(-1,"pav")
# print(newlists)
#

# #copy list
newlists2 = newlists.copy()
print(newlists2)
# #newlists2.remove(100)
# newlists2.pop(100)

#fruits = {'apple', 'banana'}
#fruits.add('mango')  # {'apple', 'banana', 'mango'}

#################################33
# Here's a structured overview of   set functions and methods with examples:
#
# ## Core Set Methods
# **add()**
# Adds a single element:
# ```
# fruits = {'apple', 'banana'}
# fruits.add('mango')  # {'apple', 'banana', 'mango'}
# ```
#
# **update()**
# Adds multiple elements from iterables:
# ```
# fruits.update(['kiwi', 'orange'])  # Adds list elements
# ```
#
# **remove()/discard()**
# Remove elements (remove raises KeyError if missing):
# ```
# fruits.remove('apple')
# fruits.discard('guava')  # No error if missing
# ```
#
# **clear()**
# Empties the set:
# ```
# fruits.clear()  # Returns set()
# ```
#
# ## Mathematical Operations
# **union()** (`|`)
# Combines sets:
# ```
# set_a = {1, 2}
# set_b = {3, 4}
# set_a.union(set_b)  # {1, 2, 3, 4}
# ```
#
# **intersection()** (`&`)
# Common elements:
# ```
# {1,2,3}.intersection({2,3,4})  # {2, 3}
# ```
#
# **difference()** (`-`)
# Elements in first set only:
# ```
# {1,2,3}.difference({2,3})  # {1}
# ```
#
# **symmetric_difference()** (`^`)
# Elements in either set but not both:
# ```
# {1,2} ^ {2,3}  # {1, 3}
# ```
#
# ## Comparison Methods
# **isdisjoint()**
# No common elements:
# ```
# {1,2}.isdisjoint({3,4})  # True
# ```
#
# **issubset()** (`=`)
# Contains all elements of another set:
# ```
# {1,2,3}.issuperset({1,2})  # True
# ```
#
# ## Built-in Functions
# **len()**
# Count elements:
# ```
# len({1,2,3})  # 3
# ```
#
# **sorted()**
# Return sorted list:
# ```
# sorted({3,1,2}, reverse=True)  # [3, 2, 1]
# ```
#
# **max()/min()/sum()**
# Mathematical operations:
# ```
# max({5,2,8}), min({5,2,8}), sum({1,2,3})  # (8, 2, 6)
# ```
#
# **copy()**
# Create shallow copy:
# ```
# new_set = fruits.copy()
# ```
#
# **pop()**
# Remove random element:
# ```
# element = {1,2,3}.pop()  # Could return 1, 2, or 3
# ```
#
# ## Set Creation
# **set()**
# Convert iterables to sets:
# ```
# set([1,2,2,3])  # {1, 2, 3}
# ```
