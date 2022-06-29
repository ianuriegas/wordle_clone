import requests
from bs4 import BeautifulSoup
import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


URL = "https://wordfind.com/length/5-letter-words/"
page = requests.get(URL)

# set up an empty list to append words from url to
unnamed = []

soup = BeautifulSoup(page.content, "html.parser")
# cmd + alt + i  ---  find the id you want  --  <div class="5-letter-words" style....>  .......  </div>
results = soup.find(id="5-letter-words")

# cmd + alt + i  ---  find the tag you want to extract
job_elements = results.find_all("a")

for job_element in job_elements:
    unnamed.append(job_element.text.strip())

print("--------------------------------------------------------")
print("Simple Guide: ")
print(bcolors.BOLD + "5 letter words only" + bcolors.ENDC)
print(bcolors.OKCYAN + bcolors.BOLD + "Letter is in the word and in the right place" + bcolors.ENDC)
print(bcolors.WARNING + bcolors.BOLD + "Letter is in the word but not in the right place" + bcolors.ENDC)
print(bcolors.FAIL + bcolors.BOLD + "Word is not valid" + bcolors.ENDC)
print("--------------------------------------------------------")
print(bcolors.BOLD + "Input a word to begin" + bcolors.ENDC)


def random_word():
    number = random.randint(0, len(unnamed))
    random_num = unnamed[number]
    return random_num


rand = random_word()


def init_word_check():
    while True:
        user_word = input()
        if user_word in unnamed:
            return user_word
            break
        print(bcolors.FAIL + bcolors.BOLD + user_word + " not valid" + bcolors.ENDC)


def word_checker(user_word, rand, count):
    temp = ""
    for i in range(0, len(user_word)):

        if user_word[i] == rand[i]:
            colored = bcolors.OKCYAN + bcolors.BOLD + user_word[i] + bcolors.ENDC
        elif user_word[i] in rand:
            colored = bcolors.WARNING + bcolors.BOLD + user_word[i] + bcolors.ENDC
        else:
            colored = bcolors.BOLD + user_word[i]
        # print(user_word[i])

        temp = temp + colored

    print("Attempt " + str(count + 1) + ": " + temp)


count = 0
while count <= 6:
    if count == 6:
        print("The word was: " + bcolors.BOLD + rand)
        break
    user_word = init_word_check()
    if user_word == rand:
        print(bcolors.BOLD + "Got the word in attempt: " + str(
            count + 1) + ", " + bcolors.OKGREEN + user_word + bcolors.ENDC)
        break
    word_checker(user_word, rand, count)
    count = count + 1
