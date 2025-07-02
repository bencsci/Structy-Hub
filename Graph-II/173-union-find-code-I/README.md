## union-find code I

Write a function, _count\_components_, that takes in a number of nodes (n) and a list of edges for an
undirected graph. In the graph, nodes are labeled from 0 to n - 1. The function should return the
number of connected components in the given graph. 

This will be practice for implementing the basic Union-Find algorithm for graphs. 

Watch the approach and walkthrough videos first!

#### test_00:

```python
count_components(7, [
  (0, 2),
  (1, 0),
  (4, 3),
  (2, 5),
  (3, 6)
]) # -> 2
```

#### test_01:

```python
count_components(6, [
  (0, 3),
  (5, 3),
  (4, 2)
]) # -> 3
```

#### test_02:

```python
count_components(6, [
  (0, 3),
  (5, 3),
  (4, 2),
  (3, 2),
  (3, 1)
]) # -> 1
```

#### test_03:

```python
count_components(100, [
  (50, 60),
  (80, 20)
]) # -> 98
```
