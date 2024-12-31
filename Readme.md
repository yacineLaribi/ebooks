# Maktabati

Maktabati is a web-based platform for ebooks, built with Django, HTML, and Tailwind CSS. It offers features like pagination, category and subject filtering, and a simple search engine. The database contains over 100,000 books, most sourced from [Internet Archive](https://archive.org).

## Features

- **Pagination**: Smooth navigation through large sets of books.
- **Filtering**: Filter books by categories and subjects.
- **Search Engine**: Simple search functionality using `icontains`. For advanced algorithms, check the `search_engine.md` file.

## Data Source

The database is populated with over 100,000 books, primarily scraped from the [Internet Archive](https://archive.org). To learn more about the scraping process, visit the related project: [Scraping Books from Internet](https://github.com/yacineLAribi/scraping_books_from_internet).

## Current Status

The project is functional but has some bugs. Contributions are welcome! If you'd like to help improve the platform, feel free to fork the repository and send a pull request.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/maktabati.git
   ```
2. Navigate to the project directory:
   ```bash
   cd maktabati
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Access the platform at `http://127.0.0.1:8000/`.

## Contributing

Contributions are encouraged! Here are some ways you can help:

- Fix existing bugs
- Improve features or add new ones
- Optimize the search engine

If you're interested, don't hesitate to submit a pull request. Let's make Maktabati better together!

---

For advanced search engine details, refer to `search_engine.md`.

Happy coding! 🎉
