import os

hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)
  if response == 0:
    print("✓")
  else:
    print("✘")
    return