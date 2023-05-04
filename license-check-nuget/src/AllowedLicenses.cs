using System.Text.Json.Serialization;

public class AllowedLicenses
{
    public List<string> Permissive { get; set; } = new();

    public List<string> Copyleft { get; set; } = new();

    public List<string> Packages { get; set; } = new();
}