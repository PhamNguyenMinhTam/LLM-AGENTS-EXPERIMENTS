# E06: --config conditions/<level>.yaml chọn điều kiện; runtime dùng chung.
from pathlib import Path
from scripts.run_experiment import main

if __name__ == "__main__":
    main(str(Path(__file__).with_name("config.yaml")))
