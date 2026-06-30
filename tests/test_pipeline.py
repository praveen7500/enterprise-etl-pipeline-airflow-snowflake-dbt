import subprocess


def test_pipeline():

    result = subprocess.run(

        [

            "python",

            "scripts/run_pipeline.py"

        ]

    )

    assert result.returncode == 0
