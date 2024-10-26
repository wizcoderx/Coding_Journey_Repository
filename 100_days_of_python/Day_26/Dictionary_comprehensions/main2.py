sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
result = {words:len(words) for words in words}
print(result)
