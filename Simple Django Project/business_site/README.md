# Info

In this Django project that called 'business'. It has app landing. Inside landing created the static folder with logo
image. And in parent folder static holds the css style file. After running it's only display a bit styled text with logo
image on main page.

Also the command `python manage.py collectstatic` was run that collected all static files for production in
static_production_test.

## Prerequisite

To get started with the project files, you'll need to:

1. Install [Python](https://www.python.org/downloads/)
2. Install [PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html#standalone)
3. Install [DB Browser for SQLite](https://sqlitebrowser.org/dl/)

## Testing

1. Open a Terminal and run the following command `python manage.py runserver`
2. Open up a web browser and go to http://127.0.0.1:8000/ to see the main page.
3. Navigate to http://127.0.0.1:8000/static/landing/logo.png to see the image being served in the browser.
4. Going to http://127.0.0.1:8000/static/main.css open the content of css file.