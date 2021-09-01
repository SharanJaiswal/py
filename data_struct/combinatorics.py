import itertools

my_list = [1, 2, 3, 4, 4]
# it dont care about the repetitive elements. All repetitive elements will be treated different, hence different combinations & permutations

combinations = itertools.combinations(my_list, 2)   # how many combinations groups are present where each group has exactly 2 elements is present
print(combinations)
for comb in combinations:
    print(comb)
print('*'*11)
permutations = itertools.permutations(my_list, 2)
print(permutations)
for perm in permutations:
    print(perm)

print('Application :')
print([results for results in combinations if sum(results) == 10])