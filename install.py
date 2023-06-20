import subprocess

def install_libraries():
    libraries = [
        'python3-nmap',  # Required for Nmap
        'git',  # Required for Seeker
        'whois',  # Required for Whois
        'foremost',  # Required for Foremost
        'hydra'  # Required for Hydra
    ]

    for library in libraries:
        print(f"[*] Installing {library}...")
        subprocess.call(['sudo', 'apt', 'install', '-y', library])

def main():
    install_libraries()

if __name__ == "__main__":
    main()
