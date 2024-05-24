#Importing the libs
import csv
import pandas as pd

#Creating a global dictionary to store the words and meanings
words_dict = {}

#Creating a function for load words from csv and error handling: 
def load_words_from_csv(func):
    def wrapper(*args, **kwargs):
        global words_dict
        try:
            df = pd.read_csv('Fvoa.csv')
            words_dict = pd.Series(df.prmean.values, index=df.enword).to_dict()
        except FileNotFoundError:
            print("The CSV file does not exist. Please add new words first.")
            words_dict = {}
        return func(*args, **kwargs)
    return wrapper

#Creating the new word function:
def new_word():
    global words_dict

    while True:
        #Geting the inputs 
        new_word = input("Enter the new word: ")
        new_mean = input("Enter the new mean: ")

        #Adding the inputs to the list
        words_dict[new_word] = new_mean
        break
    words_dict = [{'enword': key, 'prmean': value} for key, value in words_dict.items()]
    #Convert the list to DataFrame
    df = pd.DataFrame(words_dict)

    #Saving the DataFrame to CSV file
    df.to_csv('Fvoa.csv', index=False)

    print("Data saved to Fvoa.csv")

#Creating a function for searching the words:
@load_words_from_csv
def search_word():
    
    search_word = input("Enter the word which you want to searh it: ")
    meaning = words_dict.get(search_word)
    
    if meaning :
        print(f"The meaning of {search_word} is {meaning}")
    else :
        print(f"{search_word} not found in the dictionary!")

#Creating a function for deleting a word:
@load_words_from_csv
def delete_word():
    global words_dict


    delete_word = input("Enter the word which you want to delete it: ")

    if delete_word in words_dict :
        del words_dict[delete_word]

        # Convert the updated dictionary to a list of dictionaries
        word_list = [{'enword': key, 'prmean': value} for key, value in words_dict.items()]
        
        # Convert the list to DataFrame
        df = pd.DataFrame(word_list)

        # Saving the updated DataFrame to CSV file
        df.to_csv('Fvoa.csv', index=False)

        print(f"'{delete_word}' has been deleted.")
    else :
        print(f"{delete_word} not found in the dictionary! ")


#Create a function to see all the words :
def all_words ():
    if len(words_dict) > 0 :
        print(words_dict)
    else :
        print("dictionary is empty! please add a new word first")




new_word()
search_word()
delete_word()
all_words()
