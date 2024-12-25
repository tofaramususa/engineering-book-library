import os
import subprocess
# This is a simple script that lists of the books available and adds it to a booklist.txt


# Function to open directory
def open_directory():
    # open current directory
    directory = os.getcwd()
    # open the directory
    # os.startfile(directory)
    subprocess.run(["open", directory])
    # get list of all the books that end with pdf
    books = [file for file in os.listdir(directory) if file.endswith(".pdf")]
    # print the list of books
    existing_books = set()

    if os.path.exists("booklist.txt"):
        with open("booklist.txt", "r") as f:
            existing_books = set(f.read().splitlines())
	
    with open("booklist.txt", "a") as f:
        number = 0
        for book in books:
            number += 1
            if book not in existing_books:
                f.write(f"{number}. {book}" + "\n")
                existing_books.add(book)
                print(f"Added {book} to booklist.txt")

if __name__ == "__main__":
    open_directory()

