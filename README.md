# THE BLOG MANSION :unicorn: :black_heart:

*A Django site for my personal blog. Written in Python, HTML, and CSS. For unicorns! :unicorn: :black_heart:*

## About :books:

Because I saw the movie *The Fifth Estate*, I got the bright idea to practice some Python + Django and restart my blog!
That's what this is. I'll be writing about different things here and maybe also sometimes also other people will write things here.

## Features :test_tube:

- polished and optimized code
- easy to use
- classic and elegant design

## Demo :see_no_evil:

You can visit the deployed web app here: [VISIT](https://blvckuncrn.pythonanywhere.com/):see_no_evil:.

## Setup :hammer:

If you want to try out this site for yourself, make sure you have the following tools installed:

- Python 3+
- Git
- Pipenv

1.) Clone the source code:
```bash
$ git clone https://github.com/iamtheblackunicorn/TheBlogMansion.git
```
2.) `cd` into the source's root:
```bash
$ cd TheBlogMansion
```
3.) Install all dependencies:
```bash
pipenv install
```
4.) Make "migrations" and set everything up.
```bash
$ pipenv shell
(TheBlogMansion) $ python manage.py makemigrations
(TheBlogMansion) $ python manage.py migrate
```
5.) Set up a local user and follow the on-screen instructions:
```bash
(TheBlogMansion) $ python manage.py createsuperuser
```
6.) Launch the development server:
```bash
(TheBlogMansion) $ python manage.py runserver
```

## Contributing :pick:
Fork the repository, execute the steps from above, make the changes you need, and test them.
Once you have done that, push your changes and file a pull request. I will review it and merge it if it adds value.

## Changelog :black_nib:

### Version 1.0.0: ***Initial release***

- This is the initial release of *The Blog Mansion*.
- Optimized and polished.

## Note :scroll:

- *The Blog Mansion :unicorn: :black_heart:* by Alexander Abraham :black_heart: a.k.a. *"The Black Unicorn" :unicorn:*
- This software is licensed under the MIT license.
