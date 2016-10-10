sbd - A python tool to convert Safari Books Online resources into PDF.
==================================

This project fetches relevant data from Safari Books Online pages and generates a single pdf with the content.

Installation
------------

1. Install sbd with pip

.. code-block:: bash

	$ pip install sbd

2. Install `wkhtmltopdf`_

* Debian/Ubuntu:

.. code-block:: bash

	$ sudo apt-get install wkhtmltopdf

* Windows and other options: check wkhtmltopdf `homepage <http://wkhtmltopdf.org/>`_ for binary installers

.. _wkhtmltopdf: http://wkhtmltopdf.org/


Usage
-----
.. code-block:: bash

	$ usage: sbd [-h] [-u LOGIN] [-p PASSWORD] safari_book_url

You need to pass the credentials to your Safari Books online account followed by the URL of the book you wish to download.

.. code-block:: bash

    $ sbd -u login -p password https://www.safaribooksonline.com/library/view/reactive-web-applications/9781633430099/

An alternative is to set your credentials in environmental variables:

.. code-block:: bash

	$ export SBD_LOGIN='your_login'
	$ export SBD_PASSWORD='your_password'
	$ sbd https://www.safaribooksonline.com/library/view/reactive-web-applications/9781633430099/




