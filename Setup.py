import subprocess
import sys

def install_packages(requirements_file):
    """Install packages from a requirements.txt file."""
    try:
        with open(requirements_file, 'r') as file:
            packages = file.read().splitlines()
            for package in packages:
                if package.strip():  # Ensure the package is not an empty line
                    print(f"Installing {package}...")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print("All packages installed successfully.")
    except FileNotFoundError:
        print(f"Error: {requirements_file} not found.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {e.cmd}")

if __name__ == "__main__":
    requirements_file = "requirements.txt"  # Modify this path if your file is located elsewhere
    install_packages(requirements_file)
