a = input("a:")
b = input("b:")

c = a
a = b
b = c

print("a = " + a)
print("b = " + b)


"""
This code swaps the values entered in the console.

The variable `c` acts as a temporary container: 
1. We store the value of `a` in `c` to keep it safe.
2. Assign the value of `b` to `a`.
3. Finally, assign the value stored in `c` (original `a`) to `b`.

Analogy: Imagine `a` and `b` are containers with liquid. We pour `a` into `c` 
temporarily, pour `b` into `a`, 
and then pour `c` into `b` to complete the swap.

This demonstrates the basic **swap algorithm** using a temporary variable.
"""
