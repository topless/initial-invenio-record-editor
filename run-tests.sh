#!/usr/bin/env sh
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Record-Editor is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

pydocstyle invenio_record_editor tests docs && \
isort -rc -c -df && \
check-manifest --ignore ".travis-*,examples/static*" && \
sphinx-build -qnNW docs docs/_build/html && \
python setup.py test
