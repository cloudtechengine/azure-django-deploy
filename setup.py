import subprocess
import sys
from setuptools import setup, find_packages

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, '-m', 'venv', 'venv'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_dependencies()

    setup(
        name="ArticleProject",
        version="0.1",
        packages=find_packages(),
        author="Your Name",
        description="Description of your project",
        # Add more setup options as needed
    )
