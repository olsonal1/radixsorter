# A radix sorter for enumerable elements
- by Alexander Olson.

Radix sort is a handy and very simple algorithm to sort data that can be efficiently assigned an integer ordering of reasonable size.

The algorithm has quite a few variations: you can read more about it in CLRS (or by its proper title, "Introduction to Algorithms" by Charles E. Leiserson, Clifford Stein, Ronald Rivest, and Thomas H. Cormen.

Here, we implement it in python: we'll assume that we already have a list of elements, and- if they're not already integers- a function to cheaply enumerate them.

If you'd like to use this for whatever (non-plagiarizing) reason, feel free! (But please attribute it).
