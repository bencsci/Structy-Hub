## sum possible

Write a function *sum_possible* that takes in an amount and a list of positive numbers. The
function should return a boolean indicating whether or not it is possible to create the amount by
summing numbers of the list. You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative.

#### test_00:

```python
sum_possible(8, [5, 12, 4]) # -> True, 4 + 4
```

#### test_01:

```python
sum_possible(15, [6, 2, 10, 19]) # -> False
```

#### test_02:

```python
sum_possible(13, [6, 2, 1]) # -> True
```

#### test_03:

```python
sum_possible(103, [6, 20, 1]) # -> True
```

#### test_04:

```python
sum_possible(12, []) # -> False
```

#### test_05:

```python
sum_possible(12, [12]) # -> True
```

#### test_06:

```python
sum_possible(0, []) # -> True
```

#### test_07:

```python
sum_possible(271, [10, 8, 265, 24]) # -> False
```

#### test_08:

```python
sum_possible(2017, [4, 2, 10]) # -> False
```

#### test_09:

```python
sum_possible(13, [3, 5]) # -> true
```

#### test_10:

```python
sum_possible(10, [4, 5, 7]) # -> true
```

#### test_11:

```python
sum_possible(16, [7, 6, 3])# -> true
```
