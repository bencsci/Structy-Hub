## overlap subsequence

Write a function, *overlap_subsequence*, that takes in two strings as arguments. The function should
return the length of the longest overlapping subsequence.

A subsequence of a string can be created by deleting any characters of the string, while maintaining
the relative order of characters.

```
For example, given:

"dogs", "daogt"

Deleting the s from "dogs" and the a,t from "daogt", gives the subsequence "dog"
```

#### test_00:

```python
overlap_subsequence("dogs", "daogt") # -> 3
```

#### test_01:

```python
overlap_subsequence("xcyats", "criaotsi") # -> 4
```

#### test_02:

```python
overlap_subsequence("xfeqortsver", "feeeuavoeqr") # -> 5
```

#### test_03:

```python
overlap_subsequence("kinfolklivemustache", "bespokekinfolksnackwave") # -> 11
```

#### test_04:

```python
overlap_subsequence(
  "mumblecorebeardleggingsauthenticunicorn",
  "succulentspughumblemeditationlocavore"
) # -> 15
```
