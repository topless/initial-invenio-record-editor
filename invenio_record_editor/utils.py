# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Record-Editor is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module serving a generic record editor."""

from functools import wraps

from flask import abort, current_app
from flask_login import current_user


def need_editor_permissions(action):
    """Get permission for editor or abort.

    :param action: The action needed.
    """
    def decorator_builder(f):
        @wraps(f)
        def decorate(*args, **kwargs):
            check_permission(
                current_app.config['RECORD_EDITOR_VIEW_PERMISSION'](action)
            )
            return f(*args, **kwargs)
        return decorate
    return decorator_builder


def check_permission(permission):
    """Check if permission is allowed.

    If permission fails then the connection is aborted.
    :param permission: The permission to check.
    """
    if permission is not None and not permission.can():
        if current_user.is_authenticated:
            abort(403, 'You do not have a permission for this action')
        abort(401)
