=====
login 
=====

login is a simple Django app to conduct Web-based login. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "login" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'login',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('login/', include('login.urls')),

3. Run ``python manage.py migrate`` to create the login models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a login (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/login/ to participate in the login.
