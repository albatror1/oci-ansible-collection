#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_resource_manager_stack
short_description: Manage a Stack resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Stack resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a stack in the specified compartment.
      You can create a stack from a Terraform configuration.
      The Terraform configuration can be directly uploaded or referenced from a source code control system.
      You can also create a stack from an existing compartment.
      You can also upload the Terraform configuration from an Object Storage bucket.
      For more information, see
      L(To create a stack,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Tasks/managingstacksandjobs.htm#createstack-all).
    - "This resource has the following action operations in the M(oracle.oci.oci_resource_manager_stack_actions) module: change_compartment,
      detect_stack_drift."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Unique identifier (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) of the compartment in which the stack
              resides.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - The stack's display name.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Description of the stack.
            - This parameter is updatable.
        type: str
    config_source:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            config_source_type:
                description:
                    - Specifies the `configSourceType` for uploading the Terraform configuration.
                    - This parameter is updatable.
                type: str
                choices:
                    - "ZIP_UPLOAD"
                    - "GIT_CONFIG_SOURCE"
                    - "OBJECT_STORAGE_CONFIG_SOURCE"
                    - "COMPARTMENT_CONFIG_SOURCE"
                    - "TEMPLATE_CONFIG_SOURCE"
                required: true
            working_directory:
                description:
                    - File path to the directory from which Terraform runs.
                      If not specified, the root directory is used.
                      This parameter is ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`.
                    - This parameter is updatable.
                type: str
            zip_file_base64_encoded:
                description:
                    - ""
                    - This parameter is updatable.
                    - Applicable when config_source_type is 'ZIP_UPLOAD'
                    - Required when config_source_type is 'ZIP_UPLOAD'
                type: str
            configuration_source_provider_id:
                description:
                    - Unique identifier (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm))
                      for the Git configuration source.
                    - This parameter is updatable.
                    - Required when config_source_type is 'GIT_CONFIG_SOURCE'
                type: str
            repository_url:
                description:
                    - The URL of the Git repository.
                    - This parameter is updatable.
                    - Applicable when config_source_type is 'GIT_CONFIG_SOURCE'
                type: str
            branch_name:
                description:
                    - The name of the branch within the Git repository.
                    - This parameter is updatable.
                    - Applicable when config_source_type is 'GIT_CONFIG_SOURCE'
                type: str
            region:
                description:
                    - "The name of the bucket's region.
                      Example: `PHX`"
                    - This parameter is updatable.
                    - Applicable when config_source_type is 'OBJECT_STORAGE_CONFIG_SOURCE'
                    - Required when config_source_type is one of ['COMPARTMENT_CONFIG_SOURCE', 'OBJECT_STORAGE_CONFIG_SOURCE']
                type: str
            namespace:
                description:
                    - The Object Storage namespace that contains the bucket.
                    - This parameter is updatable.
                    - Applicable when config_source_type is 'OBJECT_STORAGE_CONFIG_SOURCE'
                    - Required when config_source_type is 'OBJECT_STORAGE_CONFIG_SOURCE'
                type: str
            bucket_name:
                description:
                    - The name of the bucket that contains the Terraform configuration files.
                    - This parameter is updatable.
                    - Applicable when config_source_type is 'OBJECT_STORAGE_CONFIG_SOURCE'
                    - Required when config_source_type is 'OBJECT_STORAGE_CONFIG_SOURCE'
                type: str
            compartment_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to use for creating the stack.
                      The new stack will include definitions for supported resource types in scope of the specified compartment OCID (tenancy level for root
                      compartment, compartment level otherwise).
                    - Required when config_source_type is 'COMPARTMENT_CONFIG_SOURCE'
                type: str
            services_to_discover:
                description:
                    - "Filter for L(services to use with Resource
                      Discovery,https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services).
                      For example, \\"database\\" limits resource discovery to resource types within the Database service.
                      The specified services must be in scope of the given compartment OCID (tenancy level for root compartment, compartment level otherwise).
                      If not specified, then all services at the scope of the given compartment OCID are used."
                    - Applicable when config_source_type is 'COMPARTMENT_CONFIG_SOURCE'
                type: list
                elements: str
            template_id:
                description:
                    - ""
                    - Required when config_source_type is 'TEMPLATE_CONFIG_SOURCE'
                type: str
    variables:
        description:
            - "Terraform variables associated with this resource.
              Maximum number of variables supported is 250.
              The maximum size of each variable, including both name and value, is 8192 bytes.
              Example: `{\\"CompartmentId\\": \\"compartment-id-value\\"}`"
            - This parameter is updatable.
        type: dict
    terraform_version:
        description:
            - "The version of Terraform to use with the stack. Example: `0.12.x`"
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags associated with this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    stack_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the stack.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Stack.
            - Use I(state=present) to create or update a Stack.
            - Use I(state=absent) to delete a Stack.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create stack
  oci_resource_manager_stack:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    config_source:
      # required
      config_source_type: ZIP_UPLOAD
      zip_file_base64_encoded: zip_file_base64_encoded_example

      # optional
      working_directory: working_directory_example

    # optional
    display_name: display_name_example
    description: description_example
    variables: null
    terraform_version: terraform_version_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update stack
  oci_resource_manager_stack:
    # required
    stack_id: "ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    config_source:
      # required
      config_source_type: ZIP_UPLOAD
      zip_file_base64_encoded: zip_file_base64_encoded_example

      # optional
      working_directory: working_directory_example
    variables: null
    terraform_version: terraform_version_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update stack using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_resource_manager_stack:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    config_source:
      # required
      config_source_type: ZIP_UPLOAD
      zip_file_base64_encoded: zip_file_base64_encoded_example

      # optional
      working_directory: working_directory_example
    variables: null
    terraform_version: terraform_version_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete stack
  oci_resource_manager_stack:
    # required
    stack_id: "ocid1.stack.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete stack using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_resource_manager_stack:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
stack:
    description:
        - Details of the Stack resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the stack.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Unique identifier (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the compartment where the stack is
                  located.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Human-readable name of the stack.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the stack.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - "The date and time at which the stack was created.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the stack.
                  For more information about stack lifecycle states in Resource Manager, see
                  L(Key Concepts,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__StackStates).
            returned: on success
            type: str
            sample: CREATING
        config_source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                config_source_type:
                    description:
                        - The type of configuration source to use for the Terraform configuration.
                    returned: on success
                    type: str
                    sample: ZIP_UPLOAD
                working_directory:
                    description:
                        - File path to the directory to use for running Terraform.
                          If not specified, the root directory is used.
                          This parameter is ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`.
                    returned: on success
                    type: str
                    sample: working_directory_example
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to use
                          for creating the stack. The new stack will include definitions for supported
                          resource types in this compartment.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                region:
                    description:
                        - The region to use for creating the stack. The new stack will include definitions for
                          supported resource types in this region.
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                services_to_discover:
                    description:
                        - "Filter for L(services to use with Resource
                          Discovery,https://www.terraform.io/docs/providers/oci/guides/resource_discovery.html#services).
                          For example, \\"database\\" limits resource discovery to resource types within the Database service.
                          The specified services must be in scope of the given compartment OCID (tenancy level for root compartment, compartment level
                          otherwise).
                          If not specified, then all services at the scope of the given compartment OCID are used."
                    returned: on success
                    type: list
                    sample: []
                configuration_source_provider_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Git configuration source.
                    returned: on success
                    type: str
                    sample: "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx"
                repository_url:
                    description:
                        - The URL of the Git repository for the configuration source.
                    returned: on success
                    type: str
                    sample: repository_url_example
                branch_name:
                    description:
                        - The name of the branch in the Git repository for the configuration source.
                    returned: on success
                    type: str
                    sample: branch_name_example
                namespace:
                    description:
                        - The Object Storage namespace that contains the bucket.
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket_name:
                    description:
                        - "The name of the bucket that contains the Terraform configuration files.
                          Maximum file size (applies to each file in the bucket): 100 MB. (In a bucket, a file is an object.)"
                    returned: on success
                    type: str
                    sample: bucket_name_example
        variables:
            description:
                - "Terraform variables associated with this resource.
                  Maximum number of variables supported is 250.
                  The maximum size of each variable, including both name and value, is 8192 bytes.
                  Example: `{\\"CompartmentId\\": \\"compartment-id-value\\"}`"
            returned: on success
            type: dict
            sample: {}
        terraform_version:
            description:
                - "The version of Terraform specified for the stack. Example: `0.12.x`"
            returned: on success
            type: str
            sample: terraform_version_example
        stack_drift_status:
            description:
                - Drift status of the stack.
                  Drift refers to differences between the actual (current) state of the stack and the expected (defined) state of the stack.
            returned: on success
            type: str
            sample: NOT_CHECKED
        time_drift_last_checked:
            description:
                - "The date and time when the drift detection was last executed.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "config_source": {
            "config_source_type": "ZIP_UPLOAD",
            "working_directory": "working_directory_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "region": "us-phoenix-1",
            "services_to_discover": [],
            "configuration_source_provider_id": "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx",
            "repository_url": "repository_url_example",
            "branch_name": "branch_name_example",
            "namespace": "namespace_example",
            "bucket_name": "bucket_name_example"
        },
        "variables": {},
        "terraform_version": "terraform_version_example",
        "stack_drift_status": "NOT_CHECKED",
        "time_drift_last_checked": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.resource_manager import ResourceManagerClient
    from oci.resource_manager.models import CreateStackDetails
    from oci.resource_manager.models import UpdateStackDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StackHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "stack_id"

    def get_module_resource_id(self):
        return self.module.params.get("stack_id")

    def get_get_fn(self):
        return self.client.get_stack

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stack, stack_id=self.module.params.get("stack_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_stacks, **kwargs)

    def get_create_model_class(self):
        return CreateStackDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_stack,
            call_fn_args=(),
            call_fn_kwargs=dict(create_stack_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateStackDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_stack,
            call_fn_args=(),
            call_fn_kwargs=dict(
                stack_id=self.module.params.get("stack_id"),
                update_stack_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_stack,
            call_fn_args=(),
            call_fn_kwargs=dict(stack_id=self.module.params.get("stack_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


StackHelperCustom = get_custom_class("StackHelperCustom")


class ResourceHelper(StackHelperCustom, StackHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            config_source=dict(
                type="dict",
                options=dict(
                    config_source_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "ZIP_UPLOAD",
                            "GIT_CONFIG_SOURCE",
                            "OBJECT_STORAGE_CONFIG_SOURCE",
                            "COMPARTMENT_CONFIG_SOURCE",
                            "TEMPLATE_CONFIG_SOURCE",
                        ],
                    ),
                    working_directory=dict(type="str"),
                    zip_file_base64_encoded=dict(type="str"),
                    configuration_source_provider_id=dict(type="str"),
                    repository_url=dict(type="str"),
                    branch_name=dict(type="str"),
                    region=dict(type="str"),
                    namespace=dict(type="str"),
                    bucket_name=dict(type="str"),
                    compartment_id=dict(type="str"),
                    services_to_discover=dict(type="list", elements="str"),
                    template_id=dict(type="str"),
                ),
            ),
            variables=dict(type="dict"),
            terraform_version=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            stack_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="stack",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
