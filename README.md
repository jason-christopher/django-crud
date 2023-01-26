# Lab 28 - Django CRUD

## Author: Jason Christopher

### Description

* Basic Django app with four pages (snack_list, snack_detail, snack_update, and snack_delete) that includes some snacks. The "home" page is the "snack_list" template that has all the snacks in a card. The user can click on each snack to update or delete it. The nav bar at the top allows users to go to the Home page or to add a snack for anywhere in the site.
* Using `/admin` at the end od the URL will bring the user to the Django admin portal where they can sign in(username: admin, password: 12345) to add/delete/modify snacks.

### Links and Resources

* Django
* Tailwind
* Flowbite

### Setup

1. Create and activate virtual environment
2. Run `pip install django`
3. Run `pip install -r requirements.txt`
4. Run `python manage.py runserver` (URL link will show if installation worked) - starts the development server (not used for production). Creates `db.sqlite3` file in `root`.
5. Run `python manage.py migrate` to apply un-applied migrations to the `admin`, `auth`, `contenttypes`, `sessions` apps
6. Run `python manage.py test` to run all tests.
