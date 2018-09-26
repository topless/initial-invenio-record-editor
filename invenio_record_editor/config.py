# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Record-Editor is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module serving a generic record editor."""

from .permissions import default_permission

RECORD_EDITOR_DEFAULT_URL_PREFIX = '/'
"""Default URL we want to serve our editor application, i.e /editor."""

RECORD_EDITOR_DEFAULT_PERMISSION = default_permission
"""Default user permission to access the editor."""

RECORD_EDITOR_DEFAULT_VALUE = 'invenio-record-editor'
"""Default value for the application."""

RECORD_EDITOR_BASE_TEMPLATE = 'invenio_record_editor/base.html'
"""Default base template for the demo page."""
