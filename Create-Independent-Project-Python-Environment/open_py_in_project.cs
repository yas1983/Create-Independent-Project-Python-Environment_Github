using System;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Windows.Forms;

[assembly: AssemblyTitle("\u7528\u9879\u76ee\u73af\u5883\u6253\u5f00")]
[assembly: AssemblyProduct("\u7528\u9879\u76ee\u73af\u5883\u6253\u5f00")]
[assembly: AssemblyDescription("\u7528\u9879\u76ee\u73af\u5883\u6253\u5f00")]
[assembly: AssemblyFileVersion("1.0.0.0")]
[assembly: AssemblyInformationalVersion("1.0.0.0")]

internal static class Program
{
    [STAThread]
    private static void Main(string[] args)
    {
        if (args.Length < 1 || string.IsNullOrWhiteSpace(args[0]))
        {
            MessageBox.Show("Open a .py file with this program.", "Open with project environment");
            return;
        }

        string pyfile;
        try
        {
            pyfile = Path.GetFullPath(args[0]);
        }
        catch (Exception ex)
        {
            MessageBox.Show("Could not open that file.\n" + ex.Message, "Open with project environment");
            return;
        }

        string project = FindProjectFolder(Path.GetDirectoryName(pyfile));
        string codeExe = FindCodeExe();
        if (codeExe == null)
        {
            MessageBox.Show("VS Code was not found.", "Open with project environment");
            return;
        }

        var psi = new ProcessStartInfo();
        psi.FileName = codeExe;
        psi.UseShellExecute = false;
        if (project != null)
        {
            psi.Arguments = "-n \"" + project + "\" \"" + pyfile + "\"";
        }
        else
        {
            psi.Arguments = "-n \"" + pyfile + "\"";
        }

        try
        {
            Process.Start(psi);
        }
        catch (Exception ex)
        {
            MessageBox.Show("Could not start VS Code.\n" + ex.Message, "Open with project environment");
        }
    }

    private static string FindProjectFolder(string startFolder)
    {
        string folder = startFolder;
        while (!string.IsNullOrEmpty(folder))
        {
            string venvPy = Path.Combine(folder, ".venv", "Scripts", "python.exe");
            if (File.Exists(venvPy))
            {
                return folder;
            }

            DirectoryInfo parent = Directory.GetParent(folder);
            if (parent == null)
            {
                break;
            }

            folder = parent.FullName;
        }

        return null;
    }

    private static string FindCodeExe()
    {
        string[] candidates = new string[]
        {
            @"D:\Programs\Microsoft VS Code\Code.exe",
            Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
                @"Programs\Microsoft VS Code\Code.exe"),
            @"C:\Program Files\Microsoft VS Code\Code.exe"
        };

        foreach (string path in candidates)
        {
            if (File.Exists(path))
            {
                return path;
            }
        }

        return null;
    }
}
