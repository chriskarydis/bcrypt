from datetime import datetime, timedelta

def generate_wordlist(start_year, end_year):
    wordlist = []
    current_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year + 1, 1, 1)

    while current_date < end_date:
        formatted_date = current_date.strftime("%d%m%y")
        wordlist.append(formatted_date)
        current_date += timedelta(days=1)

    return wordlist

def save_wordlist(wordlist, filename):
    with open(filename, 'w') as file:
        for word in wordlist:
            file.write(word + '\n')

start_year = 1970
end_year = 2030
wordlist = generate_wordlist(start_year, end_year)

filename = "date_wordlist.txt"
save_wordlist(wordlist, filename)
print("Wordlist saved to", filename)
