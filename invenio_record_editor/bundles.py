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
    "node_modules/test-invenio-record-editor-js/dist/inline.bundle.js",
    "node_modules/test-invenio-record-editor-js/dist/polyfills.bundle.js",
    "node_modules/test-invenio-record-editor-js/dist/vendor.bundle.js",
    "node_modules/test-invenio-record-editor-js/dist/main.bundle.js",
    "node_modules/test-invenio-record-editor-js/dist/0.chunk.js",
    depends=("node_modules/test-invenio-record-editor-js/dist/*.js"),
    output="gen/invenio-record-editor-js.%(version)s.js",
    npm={"test-invenio-record-editor-js": "0.0.1"},
)

css = NpmBundle(
    "node_modules/test-invenio-record-editor-js/dist/styles.bundle.css",
    depends=("node_modules/test-invenio-record-editor-js/dist/*.css"),
    output="gen/invenio-record-editor-js.%(version)s.css",
    npm={"test-invenio-record-editor-js": "0.0.1"},
)
