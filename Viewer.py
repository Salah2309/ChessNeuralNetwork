#This file is ment to run with selected node to show!

import subprocess

def launch_live_server(file_path):
    try:
        subprocess.Popen(['live-server', file_path])
        print(f"Live server launched for {file_path}")
    except FileNotFoundError:
        print("Live server not found. Make sure it's installed globally via npm.")

launch_live_server("Frontend/index.html")
