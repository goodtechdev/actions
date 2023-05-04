import os
import json
import sys

workflow_error = "::error::"
local_error = "Error: "
error = workflow_error if os.getenv('CI') else local_error

licenses_file = "licenses.json"
allowed_licenses_file = "allowed_licenses.json"
if not os.path.exists(allowed_licenses_file):
    print(error + "No allowed_licenses.json file found!")
    sys.exit(1)

f1 = open(licenses_file)
f2 = open(allowed_licenses_file)
packages = json.load(f1)
allowed_licenses = json.load(f2)
f1.close()
f2.close()

copyleft_error_packages = []
license_error_packages = []

if "permissive" not in allowed_licenses:
    allowed_licenses["permissive"] = []

if "copyleft" not in allowed_licenses:
    allowed_licenses["copyleft"] = []

if "packages" not in allowed_licenses:
    allowed_licenses["packages"] = []


copyleft_error = """The included package(s) listed below use a copyleft licence.
Please ensure that your code will not be subject to a copyleft license as a consequence.
\nWhen OK, add the package(s) to \"packages\" in the \"allowed_licenses.json\" file:{packages}"""

license_error = """The included package(s) listed below have licences that haven't been whitelisted in \"allowed_licences.json\".
\nYou may whitelist the licence type or package, or remove the package entirely: {packages}"""


for package in packages:
    if any(
        license in package["License"].split("; ")
        for license in allowed_licenses["permissive"]
    ):
        pass
    elif any(
        license in package["License"].split("; ")
        for license in allowed_licenses["copyleft"]
    ):
        if package["Name"] not in allowed_licenses["packages"]:
            copyleft_error_packages.append(package)
    else:
        if package["Name"] not in allowed_licenses["packages"]:
            license_error_packages.append(package)


def format_line(package):
    return "{:<20}: {}".format(package["Name"], package["License"])


def list_formatting(packages):
    return "\n\n" + "\n".join(format_line(package) for package in packages) + "\n"


if copyleft_error_packages:
    print(
        error + copyleft_error.format(packages=list_formatting(copyleft_error_packages))
    )
if license_error_packages:
    print(
        error + license_error.format(packages=list_formatting(license_error_packages))
    )

exit_code = 1 if copyleft_error_packages or license_error_packages else 0
sys.exit(exit_code)
