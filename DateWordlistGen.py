from datetime import datetime, timedelta

# Function to generate a wordlist of dates formatted as ddmmyy
def generate_wordlist(start_year, end_year):
    wordlist = []
    current_date = datetime(end_year, 12, 31)
    end_date = datetime(start_year - 1, 12, 31)

    # Loop through each day from start_date to end_date
    while current_date > end_date:
        # Format the current date as ddmmyy
        formatted_date = current_date.strftime("%d%m%y")
        # Append the formatted date to the wordlist
        wordlist.append(formatted_date)
        # Move to the next day
        current_date -= timedelta(days=1)

    return wordlist

# Function to save the wordlist to a file
def save_wordlist(wordlist, filename):
    with open(filename, 'w') as file:
        # Write each word from the wordlist to the file
        for word in wordlist:
            file.write(word + '\n')

# Define the start and end years
start_year = 1970
end_year = 2024

# Generate the wordlist of dates
wordlist = generate_wordlist(start_year, end_year)

# Define the filename for saving the wordlist
filename = "date_wordlist.txt"

# Save the wordlist to the file
save_wordlist(wordlist, filename)

print("Wordlist saved to", filename)
