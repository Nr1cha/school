# book
# chapter
# volume
import os
os.system('clear')
# from types import MethodDescriptorType

chosen_volume = input(
    "Which volume of scripture would you like to learn about? ")

# books = []
# chapters = []
# volumes = []

most_chapters = None
book_with_most_chapters = None
book_volume = None

with open("books_and_chapters.txt") as scriptures:

    for lines in scriptures:
        clean_line = lines.split(":")
        book = clean_line[0].strip()  # !# bible, book of mormon etc.
        chapter = int(clean_line[1])  # !# chapter number
        volume = clean_line[2].strip()  # !# nephi, alma, james, matthew etc.

    # adding to my arrays
        # books.append(book)
        # chapters.append(chapter)
        # volumes.append(volume)
        # new portion

        if volume.lower() == chosen_volume.lower():
            print(f"Scripture: {volume}, Book: {book}, Chapters: {chapter}")

            # if chapter > most_chapters:
            #         most_chapters = chapter
            #         book_volume = volume

        # find the book with the most chapters
            if most_chapters == None or chapter > most_chapters:
                most_chapters = chapter
                book_with_most_chapters = book
                book_volume = volume

# print(volume)
# print(f"Scripture: {book_volume}, Book: {book_with_most_chapters}, Chapters: {most_chapters}")
print(
    f"The book with the most chapters in the {chosen_volume} is: {book_with_most_chapters}")
print(f"It has {most_chapters} chapters.")
