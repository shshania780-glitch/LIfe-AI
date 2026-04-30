#!/usr/bin/env python
"""
Run both Django and Streamlit servers
"""

import subprocess
import sys
import os
import time
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.absolute()

def run_servers():
    """Run Django and Streamlit servers"""
    
    print("=" * 60)
    print("🎯 Life AI - Django & Streamlit Setup")
    print("=" * 60)
    
    # Check if virtual environment exists
    venv_path = PROJECT_ROOT / "venv"
    if not venv_path.exists():
        print("\n❌ Virtual environment not found!")
        print("Please create it with: python -m venv venv")
        return
    
    # Activate virtual environment commands
    if sys.platform == "win32":
        activate_cmd = str(venv_path / "Scripts" / "activate.bat")
        activate_shell = "cmd.exe"
        sep = "&"
    else:
        activate_cmd = f"source {venv_path}/bin/activate"
        activate_shell = "/bin/bash"
        sep = "&&"
    
    print("\n✅ Virtual environment found")
    print(f"📁 Project root: {PROJECT_ROOT}")
    
    # Django server setup
    django_dir = PROJECT_ROOT / "config"
    print(f"\n🚀 Starting Django server...")
    print(f"   Directory: {django_dir}")
    print(f"   URL: http://localhost:8000")
    
    # Streamlit app setup
    streamlit_app = PROJECT_ROOT / "streamlit_app.py"
    print(f"\n🚀 Starting Streamlit dashboard...")
    print(f"   URL: http://localhost:8501")
    
    print("\n" + "=" * 60)
    print("⚠️  Make sure you have:")
    print("   1. Created and applied migrations: python manage.py migrate")
    print("   2. Created a superuser: python manage.py createsuperuser")
    print("   3. Installed requirements: pip install -r requirements.txt")
    print("=" * 60)
    print("\nPress Ctrl+C to stop all servers\n")
    
    time.sleep(2)
    
    # Start Django server
    try:
        django_process = subprocess.Popen(
            [sys.executable, "manage.py", "runserver"],
            cwd=str(django_dir),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("✅ Django server started")
    except Exception as e:
        print(f"❌ Failed to start Django: {e}")
        return
    
    time.sleep(3)
    
    # Start Streamlit server
    try:
        streamlit_process = subprocess.Popen(
            [sys.executable, "-m", "streamlit", "run", str(streamlit_app)],
            cwd=str(PROJECT_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("✅ Streamlit server started")
    except Exception as e:
        print(f"❌ Failed to start Streamlit: {e}")
        django_process.terminate()
        return
    
    print("\n" + "=" * 60)
    print("🎉 All servers are running!")
    print("=" * 60)
    print("\n📱 Access your application:")
    print("   Django Admin:       http://localhost:8000/admin")
    print("   Django App:         http://localhost:8000")
    print("   Streamlit Dashboard: http://localhost:8501")
    print("\n" + "=" * 60)
    
    try:
        # Wait for both processes
        while True:
            if django_process.poll() is not None:
                print("\n⚠️  Django process ended")
            if streamlit_process.poll() is not None:
                print("\n⚠️  Streamlit process ended")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down servers...")
        django_process.terminate()
        streamlit_process.terminate()
        
        # Wait for processes to finish
        try:
            django_process.wait(timeout=5)
            streamlit_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            django_process.kill()
            streamlit_process.kill()
        
        print("✅ All servers stopped")
        sys.exit(0)


if __name__ == "__main__":
    run_servers()
