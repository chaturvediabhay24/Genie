import subprocess

def execute_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,  # Output as string instead of bytes
            shell=True,
            check=True  # Raises an exception if the command fails
        )
        return {
            'stdout': result.stdout.strip(),
            'stderr': result.stderr.strip(),
            'returncode': result.returncode
        }
    except subprocess.CalledProcessError as e:
        return {
            'stdout': e.stdout.strip() if e.stdout else None,
            'stderr': e.stderr.strip() if e.stderr else None,
            'returncode': e.returncode
        }

