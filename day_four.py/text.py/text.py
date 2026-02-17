
set1 = set(map(int, input("Enter elements of first set : ").split()))
set2 = set(map(int, input("Enter elements of second set : ").split()))
if set1.issubset(set2):
    print("First set is a subset of second set")
elif set2.issubset(set1):
    print("Second set is a subset of first set")
else:
    print("Neither is a subset of the other")
