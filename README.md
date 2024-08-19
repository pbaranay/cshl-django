# CSHL Django Demo

This repository is a demo of some general Django concepts, including:

* Creating a project
* Organizing your code into apps
* Function-based views
* URL routing
* Models and migrations
* Using the admin panel
* Using a model object Manager (`MyModel.objects`)

Keep in mind this is only an intro! There is much more to learn, and there are also more efficient ways to perform some of the tasks in this example, like [generic views](https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-display/).

## Running the demo

You can run the demo out of the box by starting a [Gitpod workspace](https://gitpod.io/). Create an empty repository in your own Django account, and follow this repository's [commit history](https://github.com/pbaranay/cshl-django/commits/main/), starting with the earliest commit (`ea82eb0`). You can add the code in each successive commit as you go; the commit description will sometimes give you additional commands to run or tasks to perform.

Once you have a Gitpod instance, remember to install Django:

```shell
pip install Django
```

Once you've gotten started, you can run the demo webserver with:

```shell
python manage.py runserver
```

(Make sure you're in the same directory as your `manage.py` file.)
