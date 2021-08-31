#!/usr/bin/env python

import json
import sys
import yaml

def main():
    with open("terraform.tfstate.json", "r") as handle:
        try:
            data = json.load(handle)
        except json.decoder.JSONDecodeError as error:
             print(error)
    resources = data["resources"]

    end_result = []

    for res_elements in resources:
        if res_elements["type"] == "oci_core_network_security_group_security_rule":
            # Creates list with NSG ids for all NSG-rules
            end_result.append(res_elements["instances"][0]["attributes"]["network_security_group_id"])

    # How many different NSGs we have (ocids)
    nsgs = sorted(set(end_result))

    # For loop goes thorugh all NSGs and count occurrences (1 NSG will appear per rule)
    for item in nsgs:
        print ("NSG: " + item[-5:] + " ; Number-of-rules: " + str(end_result.count(item)))

if __name__ == "__main__":
    main()




