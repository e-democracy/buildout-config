==============================
``buildout-config``
==============================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Buildout files for forums.e-democracy.org
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Bill Bushey`_
:Contact: Bill Bushey <bill.bushey@e-democracy.org>
:Date: 2013-01-09
:Organization: `E-Democracy`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 License`_
  by `E-Democracy`_.

Introduction
===========

This repository contains the buildout configuration that installs, runs, and
manages development for `forums.e-democracy.org`_, which is a custom instance
of `GroupServer`_.

Branches
========

master
------

master contains the buildout configuration that is currently running the 
production installation of `forums.e-democracy.org`_ or changes that will soon
be pushed to production. If you want to run the site that you see at
http://forums.e-democracy.org, this is the branch to use.

vanilla
-------

vanilla is the buildout configuration for installing the latest version of 
`GroupServer`_. It should be the same as master, except E-Democracy eggs have
been removed.

Installing
==========

To install `forums.e-democracy.org`_, please follow the instructions at 
http://pages.e-democracy.org/Installing_GroupServer_and_E-Democracy.

Resources
=========

- Code repository: https://github.com/e-democracy/buildout-config
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/edem

.. _GroupServer: http://groupserver.org/
.. _E-Democracy: http://e-democracy.org/
.. _forums.e-democracy.org: http://forums.e-democracy.org/
.. _Bill Bushey: http://groupserver.org/p/wbushey
.. _Creative Commons Attribution-Share Alike 3.0 License:
   http://creativecommons.org/licenses/by-sa/3.0/
