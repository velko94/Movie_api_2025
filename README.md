# Movie_api_GUI

This is an API that works from the CLI (command-line interface). Its purpose is to be used in a site to manage a movie
library, which will be built later.

With this API, you can:

- View the movie library
- See details for a specific movie
- Add a new movie
- Search for a movie
- Add movies to favorites and view your favorites
- See the top 5 movies based on different criteria
- Access admin features to manage the library

If you want to contribute or find a bug, please raise an issue.

---

## Installation

1. Install Python 3.6+

2. Clone the repository:

git clone <repo>
cd Movie_api_2025

3. Run the application python 
 movie_api_GUI.py
---

## Quick Start - Movie API GUI

### Running the Application

1. Run the application:

```powershell
py .\movie_api_GUI.py
```

### Main Commands

| Command | Action                                                       |
|---------|--------------------------------------------------------------|
| movlst  | List all movies                                              |
| movdt   | View movie details                                           |
| movsrch | Search movies by name, genre, year, director, or description |
| movadd  | Add a new movie                                              |
| movfv   | Manage favorites                                             |
| movcat  | View top 5 movies by rating, year, or genre                  |
| movadm  | Admin menu (table management)                                |
| exit    | Exit the application                                         |

### Favorites Menu

- Available options:

- favadd — add a movie to your favorites

- favlst — list your favorite movies

- lv — leave favorites menu

- You will be prompted for:

- whether you are a new or returning user

- your username

Favorites are stored in the database under the favorites table.

### Admin Menu

Admin options include:

- List movies

- Delete a whole table (movie, users, favorites)

- Recreate a missing table

- Delete a specific record

- Update columns in a record

- Inspect database structure

---

## Database Schema

The project uses a SQLite database (`Movie.db`) with the following tables:

### `movie` table

| Column       | Type    | Constraints                     | Description                                     |
|--------------|---------|---------------------------------|-------------------------------------------------|
| ID           | INTEGER | PRIMARY KEY AUTOINCREMENT UNIQUE | Unique identifier for each movie                |
| MOVIE_TITLE  | TEXT    | NOT NULL, UNIQUE                | Movie title                                     |
| GENRE        | TEXT    |                                 | Movie genre                                     |
| DIRECTOR     | TEXT    |                                 | Director of the movie                           |
| DESCRIPTION  | TEXT    |                                 | Brief description of the movie                  |
| RELEASE_YEAR | INTEGER |                                 | Year the movie was released                     |
| LIKENESS     | INTEGER | Global movie rating             | User rating / likeness score |

---

### `users` table

| Column    | Type    | Constraints               | Description                     |
|-----------|---------|---------------------------|---------------------------------|
| ID        | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique identifier for each user |
| USER_NAME | TEXT    | NOT NULL, UNIQUE          | Username                        |

---

### `favorites` table

| Column      | Type    | Constraints                                | Description                               |
|-------------|---------|--------------------------------------------|-------------------------------------------|
| ID          | INTEGER | PRIMARY KEY AUTOINCREMENT                  | Unique identifier for each favorite entry |
| MOVIE_TITLE | TEXT    | NOT NULL, FOREIGN KEY → movie(MOVIE_TITLE) | Title of the favorite movie               |
| GENRE       | TEXT    |                                            | Genre of the favorite movie               |
| RATING      | FLOAT   |                                            | Rating given by the user                  |
| FAVORITE_OF | TEXT    | FOREIGN KEY → users(USER_NAME)             | User who added this movie to favorites    |

**Notes:**

* Foreign keys link favorites to users and movie.
* The schema prevents duplicate movie titles and usernames.
* Update this section if the database structure changes.

---


## Contributing

If you have suggestions, please fork the repo and create a pull request. You can also open an issue with the tag *
*enhancement**.

**Steps:**

1. Fork the project.
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a pull request

---

## Acknowledgements

* Main acknowledgement is to **Yasen Petrov** for teaching me how to write code in Python.
* **Gergana** for being the lead UX and UI tester and giving a non-IT perspective on UX and Finding bugs I did not know I had.
* Google, StackOverflow, and ChatGPT for troubleshooting and ideas.

---

## Authors

[@Velko Rizov](https://bg.linkedin.com/in/velko-rizov-548049177) – [vrizov5@gmail.com](mailto:vrizov5@gmail.com)

---

## Roadmap

* Move the API from CLI to a website (Django or custom HTML/CSS).
* Implement login for better UX.
* Enhance movie details page for more options.
* Refactor `all_done()` function to be reusable across the project.
* Create a generic yes/no user choice function.
* Implement user login for personalized experience.

---

## License

Unlicensed. Intellectual rights for the API idea belong to Skillo; code rights belong to the author.

```

---

 **Changes made**:  
1. Added clear **horizontal rules (`---`)** to separate major sections.  
2. Used **headings (`##`, `###`)** for subsections like Database Tables, Favorites Menu, Admin Menu.  
3. Formatted tables and lists consistently for readability.  
4. Preserved **all original content exactly**.  

---

```
