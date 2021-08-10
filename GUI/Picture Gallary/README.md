# About
The program is a graphic art gallery application, consisting of paintings by different authors. 

## Prerequisites & Installation
To work, you need installed Python 3 and the sqlite3 library.

Running the program through the console:
```
python3 main.py
```

## Recommendation 
Use art_gallery.db file of sqlite3 database. Check the operation and reflection of the database by pressing the View All Artists or View All Arts keys.

## Description
The user can add a new artist to the database: information about which can be presented in full or absent (for example, address, city and code, or even name). It is important if you use an already prepared database, then the index of the newly created artist will be # 6.
Adding a picture is the same as described above, only all information is required. The type of paint for the painting is selected from the list. One artist can have one or more paintings. Using the original database file, you can add more paintings by artists with an index of 1-5.

The same information cannot be added to the database; after clicking Add Art or Add Artist, the add button becomes inactive. To activate it, you must click the Clear Artist's entries or Clear Art's entries button.

The program allows you to find information about paintings:

- [x] by the entered artist's name (you must enter the full name as in the database) - case-sensative and click the Search by Artist button;

- [x] by the type of paint of the painting, which is selected from the options menu;

- [x] within the price, setting the starting price and the final;

- [x] finally, if the user wants to purchase a painting. You need to click View All Arts and enter the number of the picture you like and click Sold. As a result, the selected picture will be saved to a text file and deleted from the database, this can be checked by pressing the View All Arts button again.

Future plans:

- [ ] it bad thing to expect the user enters the right artist id, so it'd be great if the user can select for which artist user wants to add picture;
- [ ] add some logging to program;
- [ ] improved art_gallery_db.py by;
- [ ] some graphics design improvements custom color, icon and change size of objects.  