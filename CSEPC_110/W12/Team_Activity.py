#book
#chapter
#volume
import os 
os.system('clear')
from types import MethodDescriptorType


books = []
chapters = []
volumes = []

most_chapters = None
book_with_most_chapters = None
book_volume = None

with open("books_and_chapters.txt") as scriptures:

        for lines in scriptures:
                clean_line = lines.split(":")
                # clean_line2 = clean_line.strip()
                book = clean_line[0].strip()
                chapter = int(clean_line[1])
                volume = clean_line[2].strip()

        #adding to my arrays
                books.append(book)
                chapters.append(chapter)
                volumes.append(volume)

        #find the book with the most chapters
                if most_chapters == None or chapter > most_chapters:
                        most_chapters = chapter
                        book_with_most_chapters = book
                        book_volume = volume
        

print(f"Scripture: {book_volume}, Book: {book_with_most_chapters}, Chapters: {most_chapters}")

