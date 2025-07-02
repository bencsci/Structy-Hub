## prefix product

Write a function, _prefixProduct_, that takes in a list of *numbers*. The function should return a new
list of the same length where each element contains the running product up to that index of the original list.

```plaintext
For example, the i-th result should be the product of all elements 0 to i:

result[i] = numbers[0] * numbers[1] * numbers[2] * ... * numbers[i]
```

You can assume that the input list is non-empty.

#### test_00:

```python
prefix_product([4, 2, 1, 6, 3, 6]) # -> [ 4, 8, 8, 48, 144, 864 ] 
```

#### test_01:

```python
prefix_product([10, 5, -2, 1, 1]) # -> [ 10, 50, -100, -100, -100 ] 
```

#### test_02:

```python
prefix_product([2, 5]) # -> [ 2, 10 ]
```

#### test_03:

```python
prefix_product([12, 88, 0, -50, 30, 2]) # -> [ 12, 1056, 0, 0, 0, 0 ] 
```

#### test_04:

```python
prefix_product([2]) # ->  [ 2 ]
```
