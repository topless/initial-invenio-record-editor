# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Record-Editor is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module serving a generic record editor."""

# TODO: This is an example file. Remove it if you do not need it, including
# the templates and static folders as well as the test case.

from __future__ import absolute_import, print_function

from flask import Blueprint, render_template
# from flask_login import login_required

from . import config

blueprint = Blueprint(
    'invenio_record_editor',
    __name__,
    url_prefix= config.RECORD_EDITOR_URL_PREFIX,
    template_folder='templates',
    static_folder='static',
)


@blueprint.route('/')
# @login_required
def index():
    """Render a basic view."""
    return render_template(
        "invenio_record_editor/index.html",
        module_name='Invenio-Record-Editor')
