import sys
from pathlib import Path
from contextlib import contextmanager
from typing import List
from argparse import ArgumentParser
import signal


@contextmanager
def stderr_as_out():
    stdout = sys.stdout
    sys.stdout = sys.stderr
    yield
    sys.stdout = stdout


def handle_sigint(*args):
    """Makes output cleaner sent SIGINT (ctrl-c)"""
    with stderr_as_out():
        print("")
    sys.exit(1)


def find_envs(cur_dir: Path, recursive: bool = False) -> List[Path]:
    search_pattern = "**/Scripts/activate" if recursive else "*/Scripts/activate"
    return [env_path for env_path in cur_dir.glob(search_pattern)]


def print_envs(envs: List[Path]) -> None:
    max_name_len = max([len(env.parent.parent.name) for env in envs])
    for idx, env in enumerate(envs):
        env_dir = env.parent.parent
        name_str = f"({env_dir.name})"
        print(f"[{idx}]: {name_str:^{max_name_len+3}} - {env_dir}")


def ask_user_to_choose_env(envs: List[Path]) -> Path:
    max_idx = len(envs) - 1
    while True:
        idx = input("Activate environment (index): ")
        try:
            idx = int(idx)
        except ValueError:
            print("Index must be a integer")
            continue

        if (idx < 0) or (idx > max_idx):
            print(f"Index must be in range [0, {max_idx}]")
            continue
        else:
            break

    return envs[idx]


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_sigint)
    parser = ArgumentParser(
        prog="activate",
        description="""
            Activates a virtual environment if found in the current directory. 
            If multiple are found the user may choose the environment. 
            All user-communication is written through stderr to not conflict with calling programs.
        """.strip(),
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        default=False,
        help="Recursivly searches through the directory for virtual environments",
    )
    with stderr_as_out():
        # We re-direct the parsing output to stderr as e.g -h argument will produce ouput
        # This would break the ps1/bat files which uses this script
        args = parser.parse_args()

        envs = find_envs(cur_dir=Path("."), recursive=args.recursive)

        if not envs:
            print("No virtual envs found")
            exit(1)
        elif len(envs) > 1:
            print_envs(envs)
            env = ask_user_to_choose_env(envs)
        else:
            env = envs[0]

    # Write env to stdout for the wrapping shell scripts to grab it
    print(str(env))
    exit(0)