# Info
In this Django project that called 'comment8or'. I try to customize it and override its site title, site header, and index header from AdminSite interface. Also, I replaced the logout message with template and setting it in as custom SiteAdmin object.

## Prerequisite

To get started with the project files, you'll need to:
1. Install [Python](https://www.python.org/downloads/)
2. Install [PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html#standalone)
3. Install [DB Browser for SQLite](https://sqlitebrowser.org/dl/)


## How it was done
1. The Comment8or admin site will be referred to as Comment8or administration. This will appear on the site header with  index title - Comment8or site admin.
2. For the title header, it will say c8 site admin.
3. The default Django admin logout message is Thanks for spending some quality time with the Web site today. In Comment8or, it will say Bye from c8admin.
4. But firstly created a new Django project called comment8or, an app called messageboard, and run the migrations.
5. Then created a superuser called c8admin.
6. Inside the project, create an admin.py file that implements a custom SiteAdmin object, where mentioned attributes (index_title, title_header, site_header, and logout_template) were overridden.
7. Added a custom Config & AdminConfig subclasses to messageboard/admin_apps.py.
8. Replaced the admin app with the custom AdminConfig subclass in comment8or/settings.py

## Testing

1. Open a Terminal and run the following command `python manage.py runserver`
2. Open up a web browser and go to http://127.0.0.1:8000/admin
3. Admin cookies: 
   - username: **c8admin**
   - password: **qBRhes_VD7Dvr5~G**