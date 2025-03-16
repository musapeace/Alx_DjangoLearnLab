## Book API Features

### 1️⃣ Filtering
- `/api/books/?title=<book_title>`
- `/api/books/?author__name=<author_name>`
- `/api/books/?publication_year=<year>`

### 2️⃣ Searching
- `/api/books/?search=<keyword>` (Searches title and author)

### 3️⃣ Ordering
- `/api/books/?ordering=title` (Ascending)
- `/api/books/?ordering=-title` (Descending)
- `/api/books/?ordering=publication_year`
- `/api/books/?ordering=-publication_year`
