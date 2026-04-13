import os
import sys
import subprocess
import re

def run(cmd):
    print(f"> {cmd}")
    subprocess.check_call(cmd, shell=True)

def update_version(version):
    print(f"Updating version → {version}")

    with open("pyproject.toml", "r") as f:
        content = f.read()

    content = re.sub(
        r'version\s*=\s*".*?"',
        f'version = "{version}"',
        content
    )

    with open("pyproject.toml", "w") as f:
        f.write(content)

def clean():
    print("Cleaning build...")
    os.system("rmdir /s /q build 2>nul")
    os.system("rmdir /s /q dist 2>nul")
    os.system("rmdir /s /q *.egg-info 2>nul")

def main():
    if len(sys.argv) < 2:
        print("Usage: python release.py <version>")
        sys.exit(1)

    version = sys.argv[1]

    update_version(version)
    clean()

    # build
    run("python -m build")

    # upload
    run("twine upload dist/*")

    # git commit + tag
    run(f'git add .')
    run(f'git commit -m "release: v{version}"')
    run(f'git tag v{version}')
    run(f'git push')
    run(f'git push origin v{version}')

    print(f"\n Released version {version}")

if __name__ == "__main__":
    main()