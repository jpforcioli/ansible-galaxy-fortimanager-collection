#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_system_report_setting
short_description: Report settings.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.10"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Frank Shen (@fshen01)
    - Hongbin Lu (@fgtdev-hblu)
notes:
    - Running in workspace locking mode is supported in this FortiManager module, the top
      level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
    - To create or update an object, use state present directive.
    - To delete an object, use state absent directive.
    - Normally, running one module can fail when a non-zero rc is returned. you can also override
      the conditions to fail or succeed with parameters rc_failed and rc_succeeded

options:
    bypass_validation:
        description: only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters
        required: false
        type: bool
        default: false
    workspace_locking_adom:
        description: the adom to lock for FortiManager running in workspace mode, the value can be global and others including root
        required: false
        type: str
    workspace_locking_timeout:
        description: the maximum time in seconds to wait for other user to release the workspace lock
        required: false
        type: int
        default: 300
    state:
        description: the directive to create, update or delete an object
        type: str
        required: true
        choices:
          - present
          - absent
    rc_succeeded:
        description: the rc codes list with which the conditions to succeed will be overriden
        type: list
        required: false
    rc_failed:
        description: the rc codes list with which the conditions to fail will be overriden
        type: list
        required: false
    system_report_setting:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            aggregate-report:
                type: str
                default: 'disable'
                description:
                 - 'Enable/disable including a group report along with the per-device reports.'
                 - 'disable - Exclude a group report along with the per-device reports.'
                 - 'enable - Include a group report along with the per-device reports.'
                choices:
                    - 'disable'
                    - 'enable'
            hcache-lossless:
                type: str
                default: 'disable'
                description:
                 - 'Usableness of ready-with-loss hcaches.'
                 - 'disable - Use ready-with-loss hcaches.'
                 - 'enable - Do not use ready-with-loss hcaches.'
                choices:
                    - 'disable'
                    - 'enable'
            ldap-cache-timeout:
                type: int
                default: 60
                description: 'LDAP cache timeout in minutes, default 60, 0 means not use cache.'
            max-table-rows:
                type: int
                default: 10000
                description: 'Maximum number of rows can be generated in a single table.'
            report-priority:
                type: str
                default: 'auto'
                description:
                 - 'Priority of sql report.'
                 - 'high - High'
                 - 'low - Low'
                 - 'auto - Auto'
                choices:
                    - 'high'
                    - 'low'
                    - 'auto'
            template-auto-install:
                type: str
                default: 'default'
                description:
                 - 'The language used for new ADOMs (default = default).'
                 - 'default - Default.'
                 - 'english - English.'
                choices:
                    - 'default'
                    - 'english'
            week-start:
                type: str
                default: 'sun'
                description:
                 - 'Day of the week on which the week starts.'
                 - 'sun - Sunday.'
                 - 'mon - Monday.'
                choices:
                    - 'sun'
                    - 'mon'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: Report settings.
      fmgr_system_report_setting:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         system_report_setting:
            aggregate-report: <value in [disable, enable]>
            hcache-lossless: <value in [disable, enable]>
            ldap-cache-timeout: <value of integer>
            max-table-rows: <value of integer>
            report-priority: <value in [high, low, auto]>
            template-auto-install: <value in [default, english]>
            week-start: <value in [sun, mon]>

'''

RETURN = '''
request_url:
    description: The full url requested
    returned: always
    type: str
    sample: /sys/login/user
response_code:
    description: The status of api request
    returned: always
    type: int
    sample: 0
response_message:
    description: The descriptive message of the api response
    type: str
    returned: always
    sample: OK.

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.NAPI import NAPIManager
from ansible_collections.fortinet.fortimanager.plugins.module_utils.NAPI import check_galaxy_version
from ansible_collections.fortinet.fortimanager.plugins.module_utils.NAPI import check_parameter_bypass


def main():
    jrpc_urls = [
        '/cli/global/system/report/setting'
    ]

    perobject_jrpc_urls = [
        '/cli/global/system/report/setting/{setting}'
    ]

    url_params = []
    module_primary_key = None
    module_arg_spec = {
        'bypass_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
        'rc_succeeded': {
            'required': False,
            'type': 'list'
        },
        'rc_failed': {
            'required': False,
            'type': 'list'
        },
        'system_report_setting': {
            'required': False,
            'type': 'dict',
            'options': {
                'aggregate-report': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'default': 'disable',
                    'type': 'str'
                },
                'hcache-lossless': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'default': 'disable',
                    'type': 'str'
                },
                'ldap-cache-timeout': {
                    'required': False,
                    'default': 60,
                    'type': 'int'
                },
                'max-table-rows': {
                    'required': False,
                    'default': 10000,
                    'type': 'int'
                },
                'report-priority': {
                    'required': False,
                    'choices': [
                        'high',
                        'low',
                        'auto'
                    ],
                    'default': 'auto',
                    'type': 'str'
                },
                'template-auto-install': {
                    'required': False,
                    'choices': [
                        'default',
                        'english'
                    ],
                    'default': 'default',
                    'type': 'str'
                },
                'week-start': {
                    'required': False,
                    'choices': [
                        'sun',
                        'mon'
                    ],
                    'default': 'sun',
                    'type': 'str'
                }
            }

        }
    }

    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_report_setting'),
                           supports_check_mode=False)

    fmgr = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
        fmgr.process_partial_curd()
    else:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()