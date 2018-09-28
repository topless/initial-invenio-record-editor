# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Record-Editor is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Minimal Flask application example.

SPHINX-START

First install Invenio-Record-Editor, setup the application by running:

.. code-block:: console

   $ pip install -e .[all]
   $ cd examples
   $ ./app-setup.sh

Next, start the development server:

.. code-block:: console

   $ export FLASK_APP=app.py FLASK_DEBUG=1
   $ flask run

and open the example application in your browser:

.. code-block:: console

    $ open http://127.0.0.1:5000/

To reset the example application run:

.. code-block:: console

    $ ./app-teardown.sh

SPHINX-END
"""

from __future__ import absolute_import, print_function

from flask import Flask
from flask_babelex import Babel
from invenio_access import InvenioAccess
from invenio_assets import InvenioAssets
from invenio_i18n import InvenioI18N

from invenio_record_editor import InvenioRecordEditor
from invenio_record_editor.views import create_editor_blueprint

app = Flask(__name__)
Babel(app)
InvenioI18N(app)
InvenioAssets(app)
InvenioAccess(app)
InvenioRecordEditor(app)

blueprint = create_editor_blueprint(app)
app.register_blueprint(blueprint)
