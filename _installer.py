from argparse import ArgumentParser
from pathlib import Path
import shutil
import os

py_files = [
    "_find_virtual_env.py"
]

shells_files={
    "cmd":"activate_env.bat",
    "ps1":"activate_env.ps1",
}

class Installer:

    def __init__(self, install_dir: Path, activate_env_dir:Path):
        self.install_dir = install_dir
        self.activate_env_dir = activate_env_dir

    def install(self, cmd=False, ps1=False):
        files = [*py_files]
        if cmd:
            files.append(shells_files["cmd"])
        if ps1:
            files.append(shells_files["ps1"])

        for file in files:
            file_path = self.activate_env_dir/file
            shutil.copy2(file_path, self.install_dir)

    def uninstall(self):
        files_to_delete = [
            *py_files,
            *shells_files.values(),
        ]
        for file_name in files_to_delete:
            file_path = self.install_dir/file_name
            if file_path.exists():
                os.remove(file_path.resolve())


if __name__ == "__main__":
    parser = ArgumentParser(
        "active_env_installer",
        description="Copies the relevant files into the directory passed to the command. At least one target shell must be shell must be choosen",
    )
    parser.add_argument(
        "install_dir", help="Directory to which files are copied",
    )
    parser.add_argument(
        "-p","--powershell", action="store_true", default=False, help="Install powershell activation script (.ps1)"
    )
    parser.add_argument(
        "-c","--cmd","--cmder", action="store_true", default=False, help="Install cmd/cmder activation script (.bat)"
    )
    parser.add_argument(
        "-u", "--uninstall", action="store_true", default=False, help="Removes all files created by installer in <install_dir>. All other flags are ignored"
    )
    parser.add_argument(
        "--clean", action="store_true", default=False, help="Runs uninstall on <install_dir> before copying the new files to <install_dir>"
    )
    args = parser.parse_args()

    install_dir = Path(args.install_dir)
    assert install_dir.exists(), "The supplied directory doesn't exists."
    assert install_dir.is_dir(), "The installation path must be a directory."

    activate_env_dir = Path(__file__).parent

    installer = Installer(install_dir, activate_env_dir)

    if args.uninstall:
        installer.uninstall()
    elif not any([args.cmd, args.powershell]) :
        print("Nothing to do, no shell choosen for installation.")
        print("Use -h or --help for detailed help.")
        parser.print_usage()
        exit(1)
    else:
        if args.clean:
            installer.uninstall()
        input("waiting")
        installer.install(
            cmd=args.cmd,
            ps1=args.powershell
        )


    exit(0)