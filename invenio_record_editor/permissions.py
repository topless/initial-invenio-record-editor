# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Record-Editor is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module serving a generic record editor."""


class AllowAll():
    """Default editor permission without restrictions."""

    def __init__(self, action):
        """Initialize a permission object."""
        pass

    def can(self):
        """Determine access."""
        return True
