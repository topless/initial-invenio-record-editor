# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Record-Editor is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.


"""Bundle definition for record editor."""

from __future__ import absolute_import, division, print_function

from invenio_assets import NpmBundle

js = NpmBundle(
    "node_modules/cds-record-editor/dist/inline.bundle.js",
    "node_modules/cds-record-editor/dist/polyfills.bundle.js",
    "node_modules/cds-record-editor/dist/styles.bundle.js",
    "node_modules/cds-record-editor/dist/vendor.bundle.js",
    "node_modules/cds-record-editor/dist/editor.module.chunk.js",
    "node_modules/cds-record-editor/dist/main.bundle.js",
    depends=("node_modules/cds-record-editor/dist/*.js"),
    output="gen/cds-record-editor.%(version)s.js",
    npm={
        "cds-record-editor": "^0.0.1"
    }
)
