// Class that maps the json string output by the dotnet-project-licenses command with --json option
public class Package
{
    public string PackageName { get; set; } = "";
    public string PackageVersion { get; set; } = "";
    public string PackageUrl { get; set; } = "";
    public string Copyright { get; set; } = "";

    public List<string> Authors { get; set; } = new();
    public string Description { get; set; } = "";
    public string LicenseUrl { get; set; } = "";
    public string LicenseType { get; set; } = "";

    public class Repository
    {
        public string Type { get; set; } = "";
        public string Url { get; set; } = "";
        public string Commit { get; set; } = "";
    }
}