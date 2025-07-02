def prefix_product(numbers):
  res = []
  product = 1
  for num in numbers:
    product *= num
    res.append(product)

  return res