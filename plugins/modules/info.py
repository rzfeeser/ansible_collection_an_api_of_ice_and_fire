#!/usr/bin/python

# Copyright: (c) 2018, RZFeeser <z@iris7.com>
# GNU General Public License v3.0+

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: rzfeeser.an_api_of_ice_and_fire.info

short_description: A module to get resources back from api of ice and fire

version_added: "1.1.0"

description:
    - A module to get resources back from api of ice and fire.
    - The resources are books, characters, and houses.
    - A user must pass the C(resource) and may optionally pass a C(resource_id)
      within that resource.

options:
    resource:
        description:
            - The resource to query.
            - Valid choices are books, characters, houses.
        required: true
        type: str
        choices:
            - books
            - characters
            - houses

    resource_id:
        description:
            - Specific resource ID within the resource collection.
            - If not provided, the root of the resource will be queried.
        required: false
        type: str

author:
    - Russell Zachary Feeser (@RZFeeser)
'''

EXAMPLES = r'''
- name: Query all books
  rzfeeser.an_api_of_ice_and_fire.info:
    resource: books
  register: results

- name: Query book 1
  rzfeeser.an_api_of_ice_and_fire.info:
    resource: books
    resource_id: 1
  register: results
'''

RETURN = r'''
aaoiaf_json:
    description: JSON returned by An API of Ice and Fire service.
    type: raw
    returned: always
    sample: {"url":"https://anapioficeandfire.com/api/books/1","name":"A Game of Thrones"}

status_code:
    description: HTTP response code returned from the API.
    type: int
    returned: always
    sample: 200

uri:
    description: URI that was requested.
    type: str
    returned: always
    sample: https://anapioficeandfire.com/api/books/1
'''

from ansible.module_utils.basic import AnsibleModule

try:
    import requests
    from requests.exceptions import RequestException
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


BASE_URL = "https://anapioficeandfire.com/api"


def build_uri(resource, resource_id=None):
    if resource_id:
        return f"{BASE_URL}/{resource}/{resource_id}"
    return f"{BASE_URL}/{resource}"


def run_module():

    module_args = dict(
        resource=dict(
            type="str",
            required=True,
            choices=["books", "characters", "houses"]
        ),
        resource_id=dict(
            type="str",
            required=False
        )
    )

    result = dict(
        changed=False,
        aaoiaf_json={},
        status_code=None,
        uri=None
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if not HAS_REQUESTS:
        module.fail_json(msg="The Python 'requests' library is required")

    resource = module.params["resource"]
    resource_id = module.params["resource_id"]

    uri = build_uri(resource, resource_id)
    result["uri"] = uri

    if module.check_mode:
        module.exit_json(**result)

    try:

        response = requests.get(uri, timeout=10)

        result["status_code"] = response.status_code

        try:
            result["aaoiaf_json"] = response.json()
        except ValueError:
            module.fail_json(msg="API did not return valid JSON", **result)

        if response.status_code != 200:
            module.fail_json(msg="API returned non-200 status code", **result)

    except RequestException as exc:
        module.fail_json(msg=f"HTTP request failed: {str(exc)}", **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
