django-ipam
===========

.. image:: https://travis-ci.org/openwisp/django-ipam.svg
   :target: https://travis-ci.org/openwisp/django-ipam

.. image:: https://coveralls.io/repos/openwisp/django-ipam/badge.svg
  :target: https://coveralls.io/r/openwisp/django-ipam

------------

.. contents:: **Table of Contents**:
   :backlinks: none
   :depth: 3

------------

TODO: features we are working on during GSoC 18
===============================================

* IPv4 and IPv6 IP address management
* Section / Subnet management with nested subnets
* Automatic free space display for all subnets
* Visual display for a specific subnet
* IP request module
* RESTful API to for CRUD operations
* Possibility to search for an IP or subnet
* CSV Import and Export of subnets and their IPs

------------

Project Goals
=============

* provide a django reusable app with features of IP Address management
* provide abstract models which can be extended into other django based apps

------------

Dependencies
============

.. code-block:: shell

    Python 3.4 or greater

------------

Install Development Version
===========================

Install the development version using the following commands:

.. code-block:: shell

    git clone https://github.com/openwisp/django-ipam.git
    cd django-ipam
    python setup.py develop

Launch the development sever:

.. code-block:: shell

    cd tests/
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver

You can access the admin interface at `http://127.0.0.1:8000/admin/`.

------------

Run Tests
=========

Install test requirements:

.. code-block:: shell

    pip install -r requirements-test.txt

Then run the test suite:

.. code-block:: shell

    ./runtests.py

------------

Setup (Integrate into other Django Apps)
========================================

Add ``django_ipam`` to ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        # other apps
        'django_ipam',
    ]

Add the URLs to your main ``urls.py``:

.. code-block:: python

    urlpatterns = [
        # ... other urls in your project ...

        # django-ipam urls
        # keep the namespace argument unchanged
        url(r'^', include('django_ipam.urls', namespace='ipam')),
    ]

Then run:

.. code-block:: shell

    ./manage.py migrate

------------

RESTful API
===========

Get First Available IP
######################

A model method to fetch the next available IP address under a specific subnet. This method can also be accessed via a RESTful API.

`django_ipam/base/models.py <https://github.com/openwisp/django-ipam/blob/master/django_ipam/base/models.py#L35>`_

GET
++++
Returns the next available IP address under a subnet.

.. code-block:: text

    /api/v1/subnet/<subnet_id>/get-first-available-ip/

Request IP
##########

A model method to create and fetch the next available IP address record under a subnet.

POST
++++
Creates a record for next available IP address and returns JSON data of that record.

.. code-block:: text

    POST /api/v1/subnet/<subnet_id>/request-ip/

===========    ========================================
Param          Description
===========    ========================================
description    Optional description for the IP address
===========    ========================================

Response
++++++++

.. code-block:: json


    {
        "ip_address": "ip_address",
        "subnet": "subnet_uuid",
        "description": "optional description"
    }

------------

`Support channels <http://openwisp.org/support.html>`_ |
`Issue Tracker <https://github.com/openwisp/django-ipam/issues>`_ |
`License <https://github.com/openwisp/django-ipam/blob/master/LICENSE>`_ |
