import os, subprocess, sys, re
from tqdm import tqdm


# Check if exiftool is installed.
exiftool_check = subprocess.run(["exiftool", "-ver"], text=True, capture_output=True).stdout
if re.match(r"\d+\.\d+\n", str(exiftool_check)) is None:
    print("Exiftool not found!")
    sys.exit(1)

# Get directory of video files.
footage_dir = input("Directory of CDNG folders: ")

if not os.path.isdir(footage_dir):
    print(f"Invalid directory: {footage_dir}")

candidate_clips = os.listdir(footage_dir)

if input("Have you backed up this folder? (y/n): ").lower() != "y":
    print("Please back up your footage before running this program.")
    sys.exit(1)

print(f"Found {len(candidate_clips)} directories at {footage_dir}.")

for i, clip in enumerate(candidate_clips):
    dir_path = os.path.join(footage_dir, clip)
    files = os.listdir(dir_path)
    print(f"Starting clip {i}")

    for f in tqdm(files):
        if f.endswith(".dng"):
            file_path = os.path.join(dir_path, f)
            p = subprocess.run(["exiftool", "-UniqueCameraModel=", "-overwrite_original", file_path], capture_output=True)
            if p.returncode != 0:
                print("Ran into an exiftool error! uh oh")
                print("stderr:")
                print(p.stderr)
                print("stdout:")
                print(p.stdout)
                sys.exit(p.returncode)

print("Done!")


