import subprocess

def execute_python(script):

    subprocess.run(

        ["python", script],

        check=True
    )
