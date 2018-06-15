django-async-tests
==================

Test project for testing against the experimental ``asyncio`` support in https://github.com/erm/django/tree/asgi/. 

Testing
-------

- Install the requirements in `requirements.txt`

ASGI
++++

- Run the application with ASGI server:

.. code::
    
    $ uvicorn asgiproj.asgi:application

WSGI
++++

- Run the application with WSGI server:

.. code::
    
    $ gunicorn asgiproj.wsgi:application

Reference
=========

Below are links to various ASGI-related projects and materials.

Django
------

`A Django Async Roadmap <https://www.aeracode.org/2018/06/04/django-async-roadmap/>`_

`Discussion thread on the django-developers mailing list <https://groups.google.com/forum/#!topic/django-developers/Kw7-xV6TrSM/>`_

`Django Channels <https://channels.readthedocs.io/>`_

ASGI
----
`ASGI (Asynchronous Server Gateway Interface) <https://asgi.readthedocs.io/>`_

`asgiref <https://github.com/django/asgiref/>`_

Servers
+++++++

`daphne <https://github.com/django/daphne/>`_

`uvicorn <https://github.com/uvicorn/>`_

`hypercorn <https://gitlab.com/pgjones/hypercorn/>`_

`fikki <https://github.com/erm/fikki/>`_

Frameworks
++++++++++

`quart <https://gitlab.com/pgjones/quart>`_

`afiqah <https://afiqah.readthedocs.io/>`_

Asyncio
-------

`asyncio <https://docs.python.org/3/library/asyncio.html>`_

`uvloop <https://github.com/MagicStack/uvloop/>`_

`Python & Async Simplified <https://www.aeracode.org/2018/02/19/python-async-simplified/>`_