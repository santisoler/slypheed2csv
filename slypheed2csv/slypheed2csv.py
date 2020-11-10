import argparse
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

    # Get every attribute of the contacts
    columns = []
    for person in contacts:
        for attribute in contacts[person]:
            if attribute not in columns:
                columns.append(attribute)

    # Create the CSV file
    args.output.write(",".join(columns) + "\n")
    for uid, person in contacts.items():
        line = []
        for attribute in columns:
            if attribute in person:
                line.append(person[attribute])
            else:
                line.append("")
        line = ",".join(line)
        args.output.write(line + "\n")
