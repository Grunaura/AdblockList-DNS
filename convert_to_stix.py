import json
import uuid
from datetime import datetime
import argparse


def convert_to_stix(domains, output_file):
    """
    Converts a list of DNS block domains into STIX format.

    Args:
        domains (list): List of domain strings to be converted.
        output_file (str): Path to save the generated STIX JSON file.
    """
    try:
        stix_bundle = {
            "type": "bundle",
            "id": f"bundle--{uuid.uuid4()}",
            "objects": []
        }

        for domain in domains:
            stix_bundle["objects"].append({
                "type": "indicator",
                "id": f"indicator--{uuid.uuid4()}",
                "pattern": f"[domain-name:value = '{domain}']",
                "valid_from": datetime.utcnow().isoformat() + "Z",
                "created_by_ref": "identity--adblocklist-dns",
                "labels": ["malicious-activity"],
                "description": f"Blocked domain: {domain}"
            })

        with open(output_file, 'w') as out:
            json.dump(stix_bundle, out, indent=4)

        print(f"STIX file created successfully: {output_file}")

    except Exception as e:
        print(f"Error during conversion: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a list of DNS block domains to STIX format.")
    parser.add_argument("--domains", nargs='+', required=True, help="List of domain strings to be converted.")
    parser.add_argument("--output", required=True, help="Path to save the output STIX JSON file.")

    args = parser.parse_args()

    convert_to_stix(args.domains, args.output)
