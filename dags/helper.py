import sys
import subprocess
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


def execute_python(script):
    logger.info(f"Running {script}")

    subprocess.run(
        [sys.executable, script],
        check=True
    )

    logger.info(f"{script} completed successfully.")
