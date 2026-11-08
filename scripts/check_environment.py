import importlib.metadata
import json
import platform
import shutil


def main():
    print(json.dumps({"os": platform.platform(), "machine": platform.machine(),
        "python": platform.python_version(), "git": shutil.which("git"),
        "ollama": shutil.which("ollama"),
        "packages": {p: importlib.metadata.version(p) for p in ["PyYAML", "pydantic", "python-dotenv"]}}, indent=2))


if __name__ == "__main__":
    main()
