django-async-tests
==================

Test project for testing against the experimental ``asyncio`` support in https://github.com/erm/django/tree/async/. Requires an ASGI server to run, you can use `uvicorn <https://github.com/encode/uvicorn/>`_, `daphne <https://github.com/django/daphne/>`_, or `hypercorn <https://pgjones.gitlab.io/hypercorn/>`_.

Testing
-------

ASGI
++++

- Install the requirements in `requirements/asgi.txt`

- Run the application with ASGI server:

.. code::
    
    $ uvicorn asgiproj.asgi:application

WSGI
++++

- Install the requirements in `requirements/wsgi.txt`

- Run the application with WSGI server:

.. code::
    
    $ gunicorn asgiproj.wsgi:application



Read more about potential async support in Django `here <https://www.aeracode.org/2018/06/04/django-async-roadmap/>`_.

