# Movie API GUI - Usage Instructions

This guide explains how to use the Movie API GUI application.

---

## 1. Running the Application

Run the program from your terminal or PowerShell:

```powershell
py .\movie_api_GUI.py
````

You will see a menu like this:

```
movlst   - List all movies
movdt    - View movie details
movsrch  - Search for a movie
movadd   - Add a movie
movfv    - Favorites menu
movcat   - Top 5 movies
movadm   - Admin menu
exit     - Exit the application
```

---

## 2. Main Menu Commands

---

###  List All Movies (`movlst`)

**Command:** `movlst`

Example:

```
What do you want to do movlst
Listing all movies
[('Christmas on Duty',), ('The Shawshank Redemption',), ...]
```

---

###  View Movie Details (`movdt`)

**Command:** `movdt`
**Options:** Provide ID or name of the movie.

**Example by ID:**

```
Do you know the name or the ID of the movie? id
What is the id of the movie 3
[('The Godfather', 'Gangster Tragedy', 'Francis Ford Coppola', ...)]
```

**Example by Name:**

```
Do you know the name or the ID of the movie? name
What is the name of the movie Shaw
[('The Shawshank Redemption', 'Drama', 'Frank Darabont', ...)]
```

---

###  Search for a Movie (`movsrch`)

**Command:** `movsrch`
**Search by:** name, genre, dir, year, or description.

**Example:**

```
Please choose by what parameter to search for: name
What is the name of the movie godf
[(3, 'The Godfather', ...)]
```

---

###  Add a Movie (`movadd`)

**Command:** `movadd`
You will be prompted for movie details.

**Example:**

```
What do you want to do movadd
Adding a movie
What is the name of the movie? Christmas on Duty
Please say something about the movie? Former rivals Blair and Josh must work Christmas duty together....
Which year was it released? 2025
Who directed the movie? Jake Van Wagoner
In what genre is the movie? Romance
Rate the movie? 6.7
Just added: (18, 'Christmas on Duty', 'Former rivals Blair and Josh must work Christmas duty together....', 'Jake Van Wagoner', 'Romance', 2025, 6.7)
```

---

###  Favorites Menu (`movfv`)

**Command:** `movfv`

**Steps:**

1. Specify if you are a new user (yes/no).
2. Enter your username.
3. Choose from:

   * `favlst` - List favorite movies
   * `favadd` - Add a movie to favorites
   * `lv` - Leave favorites menu

**Example:**

```
What do you want to do movfv
Opening favorites!
Are you a new user? no
What is the username you've registered with?
Choices are: favlst, favadd, lv
What do you want to do favadd
Please type the name of the movie to add: Dark
Movie 'The Dark Knight' was added successfully to favourites for user velko
```

---

###  Top 5 Movies (`movcat`)

**Command:** `movcat`
**Options:** rate (IMDB rating), newest (year), liked (by genre)

**Example:**

```
What do you want to do movcat
Showing top 5 movies
Choices are: rate, newest, liked
What do you want to do? rate
[('The Shawshank Redemption', 9.3), ('The Godfather', 9.2), ...]
```

---

###  Admin Menu (`movadm`)

**Command:** `movadm`
**Options:**

* List all movies
* Recreate a table
* Delete a whole table
* Delete a record from a table
* Change something in a record
* Exit admin menu

**Example - Deleting a Record:**

```
What do you want to do movadm
Showing ADMIN MENU
Choice: 4
What is the name of the table? movie
What is the id? 18
Record 18 was deleted from movie
```

**Example - Updating a Movie:**

```
What to update? name
Change the name to the value you wish to be: Gana
What is the id? 16
Just changed: 16 to Gana
```

---

## 3. Exiting the Application

**Command:** `exit`

```
What do you want to do exit
Alright, have a nice day!
```

---

This usage guide provides **step-by-step instructions for each command** in the Movie API GUI.

```

---

 Key Improvements:  
1. Each command has a **clear header** with emoji for visual distinction.  
2. Horizontal rules (`---`) separate sections.  
3. Commands are **bolded and inline code** for clarity.  
4. Examples are in **code blocks** for easy reading.  

---

If you want, I can also create a **more compact version** where each command has a **single “at-a-glance” block** so users can scan faster. That’s nice for GitHub READMEs. Do you want me to do that next?
```
