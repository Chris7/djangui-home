=====
Djangui Home
=====

A basic app for organizing a djangui based app.

Quick start
-----------

1. Add "djguihome" to your INSTALLED_APPS setting in user_settings like this::

    INSTALLED_APPS += ('djguihome',)

2. Include the djguihome URLconf in your project urls.py like this::

    url(r'^/', include('djguihome.urls')),

3. Start the server and visit http://127.0.0.1:8000/
   to see Djangui Home.