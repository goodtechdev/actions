
# Actions repository
Reusable actions for use in github workflows

## License check
Automatic verification that all installed packages are license compliant according to the users own criteria.
There is also an option for creating a report which will be uploaded as an artifact in the calling workflow.
There are two versions of the license check action: One for python and one for C#/.NET.

### Inputs
- `entrypoint`: In both cases, an entrypoint is needed where the `allowed_licenses.json` configuration file has to be located(see following section) (default: `.`)
- `create-report`: If set to `"true"`, a report is uploaded as an artifact in the calling workflow (default: `"false"`)
- `file`: Only relevant for C#/.NET projects. Allows the user to point to a specific project or solution. The supplied path has to be **relative** to the `entrypoint`.

**_allowed_licences.json_**
```
{
    "permissive": [
        "MIT License",
	"BSD License",
	"Apache Software License",
    ],
    "copyleft": [
        "Mozilla Public License 2.0 (MPL 2.0)",
	"GNU Lesser General Public License v2 (LGPLv2)"
    ],
    "packages": [
    	"astroid"
    ]
}
```
Packages found to use any of the licenses listed under "permissive" are automatically approved for use.
Packages using "copyleft" licenses have to be manually added to the "packages"-list. This is used as a safeguard for accidentally subjecting the consuming software (yours) to a viral copyleft license.
In some cases, the software cannot automatically detect the license for a package. This requires the developer to verify the license manually, and add it to the "packages" list.

### License check for python
**Prerequisites:**
* Packages need to have been installed on the active runner ("pip install -r requirements.txt" has already run)
* The entrypoint points to a directory where both the _allowed_licenses.json_ and  _requirements.txt_ files reside.

**Example usage:** 
```
steps:
  - name: Set up Python 3.10
    uses: actions/setup-python@v4
    with:
      python-version: "3.10"
  - name: Install python packages
    run: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
  - name: License check
    uses: peromvikgoodtech/test-actions/license-check@main
    with:
      entrypoint: ./
      create-report: true
```
### License check for Nuget(C#/.NET)
**Prerequisites:**
* The entrypoint points to a directory where the _allowed_licenses.json_ file resides.
* If the project file is not in the same directory, you will have to supply a relative path to the `entrypoint` path.
* If you want to analyze a solution, you have to explicitly supply the path to the `.sln` file in the `"file"` input. 

**Example usage:**
```
steps:
  - name: Setup .NET
    uses: actions/setup-dotnet@v3
    with:
      dotnet-version: 6.0.x
  - name: License check
    uses: peromvikgoodtech/test-actions/license-check-nuget@main
    with:
      entrypoint: ./license-check-nuget/test
      file: TestProject.csproj
      create-report: true
```
