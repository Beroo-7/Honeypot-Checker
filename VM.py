import platform
import subprocess

def check_cpu_vendor():
    try:
        output = subprocess.check_output(['wmic', 'cpu', 'get', 'manufacturer']).decode().strip().lower()
        if 'intel' in output or 'amd' in output:
            return True
        return False
    except Exception as e:
        print(f"Error checking CPU vendor: {e}")
        return False

def check_system_manufacturer():
    try:
        output = subprocess.check_output(['wmic', 'computersystem', 'get', 'manufacturer']).decode().strip().lower()
        if 'microsoft' not in output.lower() and 'vmware' not in output.lower() and 'virtual' not in output.lower() and 'vm' not in output.lower() and 'parallels' not in output.lower():
            return True
        return False
    except Exception as e:
        print(f"Error checking system manufacturer: {e}")
        return False

def check_system_type():
    try:
        output = platform.machine().lower()
        if 'amd64' in output or 'x86_64' in output:
            return True
        return False
    except Exception as e:
        print(f"Error checking system type: {e}")
        return False

def main():
    is_physical = True

    # Check CPU vendor
    if check_cpu_vendor():
        print("CPU vendor check: Machine is likely a physical machine.")
    else:
        print("CPU vendor check: Machine is likely a virtual machine.")
        is_physical = False

    # Check system manufacturer
    if check_system_manufacturer():
        print("System manufacturer check: Machine is likely a physical machine.")
    else:
        print("System manufacturer check: Machine is likely a virtual machine.")
        is_physical = False

    # Check system type (64-bit)
    if check_system_type():
        print("System type check: Machine is likely a physical machine.")
    else:
        print("System type check: Machine is likely a virtual machine.")
        is_physical = False

    if is_physical:
        print("\nFinal assessment: Machine is likely a physical machine.")
    else:
        print("\nFinal assessment: Machine is likely a virtual machine.")

if __name__ == "__main__":
    main()
