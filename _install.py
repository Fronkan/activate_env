from argparse import ArgumentParser
from pathlib import Path
import shutil

parser = ArgumentParser(
    "active_env_installer",
    description="Copies the relevant files into the directory passed to the command.",
)
parser.add_argument(
    "install_dir", help="Directory to which files are copied",
)
args = parser.parse_args()

install_dir = Path(args.install_dir)
assert install_dir.exists(), "The supplied directory doesn't exists"
assert install_dir.is_dir(), "The installation path must be a directory"

activate_env_dir = Path(__file__).parent

files = [
    activate_env_dir / "activate.bat",
    activate_env_dir / "activate.ps1",
    activate_env_dir / "_find_virtual_env.py",
]

for file in files:
    shutil.copy2(file, install_dir)
