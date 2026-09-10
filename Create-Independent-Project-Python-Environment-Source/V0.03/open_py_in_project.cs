using System;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Windows.Forms;

[assembly: AssemblyTitle("OpenPyInProject")]
[assembly: AssemblyProduct("OpenPyInProject")]
[assembly: AssemblyDescription("OpenPyInProject")]
[assembly: AssemblyFileVersion("0.3.0.0")]
[assembly: AssemblyInformationalVersion("V0.03")]

internal static class Program
{
    private const string MarkerName = "use_project_env.on";

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
        bool useProject = project != null && File.Exists(Path.Combine(project, MarkerName));

        string codeExe = FindCodeExe();
        if (codeExe == null)
        {
            MessageBox.Show("VS Code was not found.", "Open with project environment");
            return;
        }

        var psi = new ProcessStartInfo();
        psi.FileName = codeExe;
        psi.UseShellExecute = false;
        if (useProject)
        {
            psi.Arguments = "-n \"" + project + "\" \"" + pyfile + "\"";
        }
        else
        {
            psi.Arguments = "\"" + pyfile + "\"";
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
