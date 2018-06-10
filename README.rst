django-async-tests
==================

Test project for testing against https://github.com/erm/django/tree/async/ using an ASGI server. 

Requires an ASGI server to run, you can use `uvicorn <https://github.com/encode/uvicorn/>`_, `daphne <https://github.com/django/daphne/>`_, or `hypercorn. <https://pgjones.gitlab.io/hypercorn/>`_ I am using ``uvicorn`` for my testing, but any ASGI will work. 

You run the application with this command:

.. code::
    
    $ uvicorn asgiproj.asgi:application


Information about potential async support in Django available here: 

https://www.aeracode.org/2018/06/04/django-async-roadmap/
