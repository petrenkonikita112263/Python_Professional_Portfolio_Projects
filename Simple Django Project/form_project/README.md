# Django Form Example

## Info
Simple Django project - 'form_project' that has form_example app.
In file forms.py created simple HTML form with all elements but using django.forms package.
In views.py created view-based function form_example that created the form from forms.py and prints into console information
if the form is valid. In html page the generated form represented each element as single paragraph, it's generated crsf token.

## Running

1. Open a Terminal and run the following command `python manage.py runserver`
2. Open up a web browser and go to http://127.0.0.1:8000/form_example to see the page with html form.
3. Try to enter/select some data or not to see errors, and figure out from Django and form hints what to you shall enter.