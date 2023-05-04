import os
import sys
import json

# This script takes a folder of license reports
# and merges them together in a common format.
# The format can be read in excel using a query on the resulting json file.
# See LicenseReport.xlsx for reference


def standardize_packages(obj):
    if "Name" in obj and "Version" in obj and "License" in obj and "URL" in obj:
        return obj
    elif (
        "PackageName" in obj
        and "PackageVersion" in obj
        and "LicenseType" in obj
        and "PackageUrl" in obj
    ):
        return {
            "Name": obj["PackageName"],
            "Version": obj["PackageVersion"],
            "License": obj["LicenseType"],
            "URL": obj["PackageUrl"],
        }
    else:
        return None


def create_license_report_from_file(file_path):
    packages = []
    with open(file_path) as f:
        data = json.load(f)
        for obj in data:
            package = standardize_packages(obj)
            if package is None:
                continue
            packages.append(package)
    return packages


def create_license_report_from_folder(folder_path):
    files = os.listdir(folder_path)
    projects = {}
    for file in files:
        if file.endswith(".json"):
            file_path = os.path.join(folder_path, file)
            project_name = file.removesuffix(".json")
            projects[project_name] = create_license_report_from_file(file_path)
    return projects


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the folder path as an argument.")
        sys.exit(1)
    folder_path = sys.argv[1]
    non_duplicates = create_license_report_from_folder(folder_path)
    with open("license_report.json", "w") as report_file:
        report_file.write(json.dumps(non_duplicates))
