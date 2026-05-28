import time
import os
import re

def tail_log_file(file_path):
    try:
        with open(file_path, "r") as f:
          f.seek(0, os.SEEK_SET)
          print("[*] Started monitoring auth.log")
          while True:
            line = f.readline()
            if not line:
              time.sleep(0.5)
              continue
            yield line.strip()
    except FileNotFoundError:
      print(f"[-] Error: File not found at {file_path}")
    except KeyboardInterrupt:
      print("\n Stopped monitoring auth.log. Exiting cleanly")
    except Exception as e:
      print(f"[-] An error occured inside the streamer: {e}")
        
      
