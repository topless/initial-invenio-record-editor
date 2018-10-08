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
    depends=("node_modules/test-invenio-record-editor-js/dist/*.js"),
    filters="uglifyjs",
    output="gen/invenio-record-editor-js.%(version)s.js",
    npm={"test-invenio-record-editor-js": "0.0.11"},
)
"""Default Editor JavaScript bundle with Angular4."""

css = NpmBundle(
    "node_modules/test-invenio-record-editor-js/dist/styles.bundle.css",
    filters="cleancssurl",
    output="gen/invenio-record-editor-js.%(version)s.css",
)
"""Default Editor CSS bundle with bootstrap, font-awesome, kate, toastr"""
