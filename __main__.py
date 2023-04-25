# __main__.py

import pulumi
from pulumi_azure_native import resources
from pulumi_azure_native import operationalinsights
from pulumi_azure_native import machinelearningservices
from pulumi_azure_native import storage
from pulumi_azure_native import datalakestore

import config

# Create an Azure Resource Group
resource_group = resources.ResourceGroup(config.RESOURCE_GROUP_NAME)

# Create an Azure Storage Account
storage_account = storage.StorageAccount(config.STORAGE_ACCOUNT_NAME, 
    resource_group_name=resource_group.name,
    sku=storage.SkuArgs(
        name=storage.SkuName.STANDARD_LRS,
    ),
    kind=storage.Kind.STORAGE_V2)

# Create an Azure Machine Learning Workspace
aml_workspace = machinelearningservices.Workspace(config.WORKSPACE_NAME,
    resource_group_name=resource_group.name,
    location=config.LOCATION,
    friendly_name=config.WORKSPACE_NAME,
    sku=machinelearningservices.SkuArgs(
        tier=config.SKU_TIER
    ),
    storage_account=storage_account.id
)