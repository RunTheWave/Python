answer = "y"
counter = 1
totalaverage = 0
while answer == "y":
  total = 0
  highest = 0
  lowest = 10
  for s in range(5):
    score = float(input("Enter the score:"))
    while score < 0 or score > 10:
      print "Invaild Score, try again"
      score = float(input("Enter the score:"))
    if score > highest:
      highest = score
    if score < lowest:
      lowest = score
    total += score
  print highest, lowest
  average = (total - highest - lowest) / 3
  totalaverage += average
  finalaverage = totalaverage / counter
  print average
  answer = input("another user? y/n")
  print "times tried:", counter
  counter = counter + 1
print finalaverage