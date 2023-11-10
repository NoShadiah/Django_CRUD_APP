# Django_first-app
This is my basic Django API app.
I was designed with the MVT architecture.
Quick start:
1. Check for your django version - py -m django --version
2. Create a django application - django-admin startproject recipeapp
   You will have the following structure:
  recipeapp/
    manage.py
    recipeapp/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
   These files are:

- The recipeapp/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
- The inner recipeapp/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. recipeapp.urls).
- recipeapp/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
- recipeapp/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
- recipeapp/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
- recipeapp/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.
- recipeapp/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.
4. Run the application - py manage.py runserver
With this recipe application, you can add, read update and delete 

**Landing page**

![recipe](https://github.com/NoShadiah/Django_first-app/assets/107610642/5c95d069-6704-431a-97b6-46470d15b1ab)

**All recipes page**
![recipes](https://github.com/NoShadiah/Django_first-app/assets/107610642/30c36261-4f36-4b7a-8841-de3a58aba446)

**Adding a recipe**
![add](https://github.com/NoShadiah/Django_first-app/assets/107610642/73c28c13-c92d-4eda-990e-254104acd993)

**Reading a recipe**
![read](https://github.com/NoShadiah/Django_first-app/assets/107610642/1d3ddd04-ca5c-4211-9116-0977e4aabdd5)
