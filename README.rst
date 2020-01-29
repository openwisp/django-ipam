django-ipam
===========

.. image:: https://travis-ci.org/openwisp/django-ipam.svg
   :target: https://travis-ci.org/openwisp/django-ipam

.. image:: https://coveralls.io/repos/openwisp/django-ipam/badge.svg
  :target: https://coveralls.io/r/openwisp/django-ipam
  
.. image:: https://requires.io/github/openwisp/django-ipam/requirements.svg?branch=master
  :target: https://requires.io/github/openwisp/django-ipam/requirements/?branch=master
  :alt: Requirements Status


------------

Django-ipam is part of the `OpenWISP project <http://openwisp.org>`_.

.. image:: http://netjsonconfig.openwisp.org/en/latest/_images/openwisp.org.svg
  :target: http://openwisp.org
  :scale: 50

------------

.. contents:: **Table of Contents**:
   :backlinks: none
   :depth: 2

------------

Available Features
==================

* IPv4 and IPv6 IP address management
* IPv4 and IPv6 Subnet management
* Automatic free space display for all subnets
* Visual display for a specific subnet
* IP request module
* RESTful API to for CRUD operations
* Possibility to search for an IP or subnet
* CSV Import and Export of subnets and their IPs

------------

Project Goals
=============

* Provide a django reusable app with features of IP Address management
* Provide abstract models which can be extended into other django based apps

------------

Dependencies
============

* Python 3.4 or higher
* Django 2.0 or higher

------------

Installation for development
============================

Install ``django-ipam`` for development using following commands:

.. code-block:: shell

    git clone https://github.com/openwisp/django-ipam.git
    cd django-ipam
    python setup.py develop
    pip install -r requirements-test.txt

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

Install development version
===========================

Install tarball:

.. code-block:: shell

    pip install https://github.com/openwisp/django-ipam/tarball/master

Alternatively you can install via pip using git:

.. code-block:: shell

    pip install -e git+git://github.com/openwisp/django-ipam#egg=django-ipam
    
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

Visual Display of subnets
=========================

Django-ipam provides a graphical representation of a subnet which shows the available free space under any subnet.

.. image:: https://raw.githubusercontent.com/openwisp/django-ipam/master/docs/images/visual-display.png

------------

RESTful API
===========

API Authentication
##################

The API authentication is based on session based authentication via Django REST framework.
This authentication scheme uses Django's default session backend for authentication.

.. code-block:: text

    http -a username:password <HTTP verb> <api url>

Pagination
##########

API pagination is provided with the help `page` parameter.
The default page size is 10 which can be overridden using the `page_size` parameter.

.. code-block:: text

    /api/v1/<api endpoint url>/?page=1&page_size=10


Get First Available IP
######################

A model method to fetch the next available IP address under a specific subnet. This method can also be accessed via a RESTful API.

`django_ipam/base/models.py <https://github.com/openwisp/django-ipam/blob/master/django_ipam/base/models.py#L35>`_

GET
+++

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

IpAddress-Subnet List and Create View
#####################################

An api enpoint to retrieve or create IP addresses under a specific subnet.

GET
+++

Returns the list of IP addresses under a particular subnet.

.. code-block:: text

    /api/v1/subnet/<subnet_id>/ip-address/

POST
++++

Create a new ``IP Address``.

.. code-block:: text

    /api/v1/subnet/<subnet_id>/ip-address/

===========    ========================================
Param          Description
===========    ========================================
ip_address     IPv6/IPv4 address value
subnet         Subnet UUID
description    Optional description for the IP address
===========    ========================================

Subnet List/Create View
#######################

An api endpoint to create or retrieve the list of subnet instances.

GET
+++

Returns the list of ``Subnet`` instances.

.. code-block:: text

    /api/v1/subnet

POST
++++

Create a new ``Subnet``.

.. code-block:: text

    /api/v1/subnet

=============    ========================================
Param            Description
=============    ========================================
subnet           Subnet value in CIDR format
master_subnet    Master Subnet UUID
description      Optional description for the IP address
=============    ========================================

Subnet View
###########

An api endpoint for retrieving, updating or deleting a subnet instance.

GET
+++

Get details of a ``Subnet`` instance

.. code-block:: text

    /api/v1/subnet/<subnet-id>

DELETE
++++++

Delete a ``Subnet`` instance

.. code-block:: text

    /api/v1/subnet/<subnet-id>

PUT
+++

Update details of a ``Subnet`` instance.

.. code-block:: text

    /api/v1/subnet/<subnet-id>

=============    ========================================
Param            Description
=============    ========================================
subnet           Subnet value in CIDR format
master_subnet    Master Subnet UUID
description      Optional description for the IP address
=============    ========================================

IP Address View
###############

An api enpoint for retrieving, updating or deleting a IP address instance.

GET
+++

Get details of an ``IP address`` instance.

.. code-block:: text

    /api/v1/ip-address/<ip_address-id>

DELETE
++++++

Delete an ``IP address`` instance.

.. code-block:: text

    /api/v1/ip-address/<ip_address-id>

PUT
+++

Update details of an ``IP address`` instance.

.. code-block:: text

    /api/v1/ip-address/<ip_address-id>

===========    ========================================
Param          Description
===========    ========================================
ip_address     IPv6/IPv4 value
subnet         Subnet UUID
description    Optional description for the IP address
===========    ========================================

Export Subnet View
##################

View to export subnet data.

POST
++++

.. code-block:: text

    /api/v1/subnet/<subnet-id>/export

Import Subnet View
##################

View to import subnet data.

POST
++++

.. code-block:: text

    /api/v1/import-subnet

------------

Exporting and Importing Subnet
==============================

One can easily import and export `Subnet` data and it's Ip Addresses using `django-ipam`.
This works for both IPv4 and IPv6 types of networks.

Exporting
#########

Data can be exported via the admin interface or by using a management command. The exported data is in `.csv` file format.

From management command
+++++++++++++++++++++++

.. code-block:: shell

    ./manage.py export_subnet <subnet value>

This would export the subnet if it exists on the database.

From admin interface
++++++++++++++++++++

Data can be exported from the admin interface by just clicking on the export button on the subnet's admin change view.

.. image:: https://raw.githubusercontent.com/openwisp/django-ipam/master/docs/images/export.png

Importing
#########

Data can be imported via the admin interface or by using a management command.
The imported data file can be in `.csv`, `.xls` and `.xlsx` format. While importing
data for ip addresses, the system checks if the subnet specified in the import file exists or not.
If the subnet does not exists it will be created while importing data.

From management command
+++++++++++++++++++++++

.. code-block:: shell

    ./manage.py import_subnet --file=<file path>

From admin interface
++++++++++++++++++++

Data can be imported from the admin interface by just clicking on the import button on the subnet view.

.. image:: https://raw.githubusercontent.com/openwisp/django-ipam/master/docs/images/import.png

CSV file format
+++++++++++++++

Follow the following structure while creating `csv` file to import data.

.. code-block:: text

    Subnet Name
    Subnet Value

    ip_address,description
    <ip-address>,<optional-description>
    <ip-address>,<optional-description>
    <ip-address>,<optional-description>

------------

Extending django-ipam
=====================

Extending API Views
###################

The base API view classes can be extended into other django applications.

.. code-block:: python

    # your app.api.views
    from ..models import Subnet, IpAddress

    from .generics import (
        BaseAvailableIpView, BaseExportSubnetView, BaseImportSubnetView, BaseIpAddressListCreateView,
        BaseIpAddressView, BaseRequestIPView, BaseSubnetListCreateView, BaseSubnetView,
    )


    class AvailableIpView(BaseAvailableIpView):
        subnet_model = Subnet
        queryset = IpAddress.objects.none()


    class RequestIPView(BaseRequestIPView):
        subnet_model = Subnet
        queryset = IpAddress.objects.none()


    class SubnetIpAddressListCreateView(BaseIpAddressListCreateView):
        subnet_model = Subnet


    class SubnetListCreateView(BaseSubnetListCreateView):
        queryset = Subnet.objects.all()


    class SubnetVew(BaseSubnetView):
        queryset = Subnet.objects.all()


    class IpAddressView(BaseIpAddressView):
        queryset = IpAddress.objects.all()


    class ImportSubnetView(BaseImportSubnetView):
        subnet_model = Subnet
        queryset = Subnet.objects.none()


    class ExportSubnetView(BaseExportSubnetView):
        subnet_model = Subnet
        queryset = Subnet.objects.none()

------------

`Support channels <http://openwisp.org/support.html>`_ |
`Issue Tracker <https://github.com/openwisp/django-ipam/issues>`_ |
`License <https://github.com/openwisp/django-ipam/blob/master/LICENSE>`_ |
