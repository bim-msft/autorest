# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .a import A


class B(A):
    """B.

    :param status_code:
    :type status_code: str
    :param text_status_code:
    :type text_status_code: str
    """

    _attribute_map = {
        'status_code': {'key': 'statusCode', 'type': 'str'},
        'text_status_code': {'key': 'textStatusCode', 'type': 'str'},
    }

    def __init__(self, status_code=None, text_status_code=None):
        super(B, self).__init__(status_code=status_code)
        self.text_status_code = text_status_code