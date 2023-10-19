def linear_search_product(products, target_product):
  indices = []
  for i in range(len(products)):
      if products[i] == target_product:
          indices.append(i)
  return indices

# define a list of products
products = ["apple", "banana", "orange", "banana", "grape"]

# search for a target product
target_product = "banana"
indices = linear_search_product(products, target_product)

# print the indices of all occurrences of the target product
if len(indices) == 0:
  print("The product was not found.")
else:
  print("The product was found at indices:", indices)
