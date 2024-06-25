# Honeypot-Checker
Detects if a Windows system is physical or virtual based on CPU, manufacturer, and architecture. Useful for cybersecurity assessments.

Honeypot Checker
Overview:
The "Honeypot Checker" script is a Python tool designed to determine whether a Windows system is likely a physical machine or a virtual machine. It performs various checks based on hardware characteristics that are indicative of virtualization, helping cybersecurity professionals identify potential honeypot setups or virtual environments during security assessments.

Key Features:

Detects CPU vendor (Intel or AMD) to distinguish physical hardware from virtualized environments.

Checks system manufacturer information to identify common virtualization vendors (Microsoft, VMware, etc.).

Verifies system architecture (64-bit) as typically found in physical machines.

Usage:

Clone the repository and run the script on a Windows system.
Follow the prompts to see if the system is likely physical or virtual based on the checks performed.
Why Use Honeypot Checker?

Useful for cybersecurity specialists conducting assessments to quickly identify virtualized environments that may be used for testing or deception purposes.
Helps enhance the accuracy of security assessments by distinguishing between real and virtual machines.

Contributing:
Contributions are welcome! Fork the repository, make your changes, and submit a pull request. Please ensure your contributions align with the project's goals and follow best practices.

Disclaimer:
This tool is intended for educational and cybersecurity assessment purposes. Use responsibly and with appropriate permissions.
