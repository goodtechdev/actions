### License report
The `license-report.py` script takes a folder of license reports as generated in the GitHub action, and generates a single file with all the packages and their licenses in a standardized format.
See the `/test` folder for the resulting `license-report.json` it creates from the license report files in the `/test/Licenses` folder.
The `LicenseReport.xslx` file contains a query on the resulting json file to import the data into Excel