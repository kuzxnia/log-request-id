log-request-id
=================

Log-Request-ID is an extension to handle request-IDs logs in popular python api frameworks. 

Currently supported frameworks: flask

Requirements
------------

-  python (3.6+)

Instalation
-----------

Install using ``pip``

::

   pip install log-request-id


Usage
-----


1. Set ``LOG_REQUEST_ID_FRAMEWORK_SUPPORT`` to point to your framework of choice (section currently supported).

.. code:: txt

    LOG_REQUEST_ID_FRAMEWORK_SUPPORT=flask

2. Init request-ID handler

  -  Flask, with
     ``log_request_id.flask.init_flask_request_id_handler``

  .. code:: python

     from log_request_id import init_flask_request_id_handler

     def create_flask_app():
         app = Flask()
         init_flask_request_id_handler(app)
