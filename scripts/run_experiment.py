import argparse
import json

from controller.experiment_runner import run_experiment


def main(default_config=None):
    parser = argparse.ArgumentParser(description="Chạy thí nghiệm agent độc lập")
    parser.add_argument("--config", default=default_config, required=default_config is None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        result = run_experiment(args.config, args.dry_run)
    except (ValueError, OSError, NotImplementedError) as exc:
        parser.exit(2, f"{type(exc).__name__}: {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
