import subprocess
import sys

print("=== Running Tests ===")
test_result = subprocess.run([sys.executable, "-m", "pytest", "tests"], capture_output=True, text=True)
print(test_result.stdout)
if test_result.returncode != 0:
    print("Tests Failed! Aborting build.")
    exit(1)

print("=== Building Docker Image ===")
build_result = subprocess.run(["docker", "build", "-t", "devops_project:latest", "."], text=True)
print(build_result)

print("=== Build Complete ===")