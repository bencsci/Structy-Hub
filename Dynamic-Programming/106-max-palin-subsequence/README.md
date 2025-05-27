## max palin subsequence

Write a function, *max\_palin\_subsequence*, that takes in a string as an argument. The function should
return the length of the longest subsequence of the string that is also a palindrome.

A subsequence of a string can be created by deleting any characters of the string, while maintaining
the relative order of characters.

```
For example, given:

"luwxult"

Deleting x and t would give the subsequence:

"luwul"

The string "luwul" is a palindrome because it is the same forwards and backwards.
```

#### test_00:

```python
max_palin_subsequence("luwxult") # -> 5
```

#### test_01:

```python
max_palin_subsequence("xyzaxxzy") # -> 6
```

#### test_02:

```python
max_palin_subsequence("lol") # -> 3
```

#### test_03:

```python
max_palin_subsequence("boabcdefop") # -> 3
```

#### test_04:

```python
max_palin_subsequence("z") # -> 1
```

#### test_05:

```python
max_palin_subsequence("chartreusepugvicefree") # -> 7
```

#### test_06:

```python
max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty") # -> 15
```

#### test_07:

```python
max_palin_subsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe") # -> 31
```
