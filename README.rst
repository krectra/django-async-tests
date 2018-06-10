django-async-tests
==================

Test project for testing against the experimental ``asyncio`` support in https://github.com/erm/django/tree/async/. Requires an ASGI server to run, you can use `uvicorn <https://github.com/encode/uvicorn/>`_, `daphne <https://github.com/django/daphne/>`_, or `hypercorn <https://pgjones.gitlab.io/hypercorn/>`_.

You may run the application with this command:

.. code::
    
    $ uvicorn asgiproj.asgi:application


Read more about potential async support in Django `here <https://www.aeracode.org/2018/06/04/django-async-roadmap/>`_.

