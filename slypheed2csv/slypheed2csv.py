import argparse
import pandas as pd
import xml.etree.ElementTree as ET


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Convert Slypheed address book to CSV")
    parser.add_argument(
        "addressbook",
        metavar="ADDRESS_BOOK.xml",
        type=argparse.FileType("r"),
        help="Slypheed address book",
        default="",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="output.csv",
        type=argparse.FileType("w"),
        help="CSV version of the address book",
        default="",
    )
    args = parser.parse_args()

    # Read XML file
    tree = ET.parse(args.addressbook)
    root = tree.getroot()
    contacts = {}
    for person in root:
        uid = person.attrib.pop("uid")
        contacts[uid] = person.attrib

    # Create a pd.DataFrame out of the collected dicts
    # and export it as a CSV file
    df = pd.DataFrame.from_dict(data=contacts, orient="index")
    df.to_csv(args.output, index=False)
