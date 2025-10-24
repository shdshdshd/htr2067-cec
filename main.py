#!/usr/bin/env python3
import subprocess
import select
import time

def run_cec_client():
    # Start cec-client process
    process = subprocess.Popen(['cec-client'], 
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             universal_newlines=True)
    return process

def send_audio_mode_request():
    # Send the system audio mode request
    subprocess.run(['cec-ctl', '--to', '5', '--system-audio-mode-request', 'phys-addr=0.0.0.0'])

def main():
    process = run_cec_client()
    
    # Create file descriptors for select
    poll = select.poll()
    poll.register(process.stdout.fileno(), select.POLLIN)
    
    print("Listening for CEC events...")
    
    try:
        while True:
            # Check for new output
            if poll.poll(1000):  # 1 second timeout
                line = process.stdout.readline()
                if not line:
                    break
                    
                # Look for the specific message
                if "making Playback 1 (4) the active source" in line:
                    print("Active source message detected!")
                    send_audio_mode_request()
                    
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        # Cleanup
        process.terminate()
        process.wait()

if __name__ == "__main__":
    main()
