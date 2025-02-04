import random

# Open the file and read the content
with open('list-of-quotes.txt', mode='r', encoding='utf-8') as file:
    my_quotes = file.readlines()

# Remove any empty lines and strip extra whitespace from each quote
my_quotes = [quote.strip() for quote in my_quotes if quote.strip()]

# Choose a random quote
random_quote = random.choice(my_quotes)

# Print the random quote
print("Your random quote is: ")
print(random_quote)


