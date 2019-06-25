#!/bin/bash
oldnames=(
    "Application Name"
    "Application Details"
    "OdooModuleOdooTable"
    "group_odoorole"
    "Application Module Role"
    "odootable"
    "odoomodule"
    "odoorole"
    "Application Table Name"
)
newnames=(
    "GMC Module"
    "Employee Group Mediclaim"
    "GMCModulePolicyTable"
    "group_gmcadmin"
    "GMC Module Admin"
    "policytable"
    "gmcmodule"
    "gmcadmin"
    "Policy Data"
)

for arg; do
    if [ ! -f $arg ]; then
        echo "$arg: File not found!"
        continue
    fi
    echo "Performing replace on $arg"
    for i in "${!oldnames[@]}"; do
        sed -i "s/${oldnames[$i]}/${newnames[$i]}/g" $arg
    done
done
