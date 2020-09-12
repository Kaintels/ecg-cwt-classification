import argparse
from utils.data_loader import FileLoader
parser = argparse.ArgumentParser(description="ECG-CWT-CLASSIFICATION-BOHB")
parser.add_argument("--random_seed", type=int, default=777)
parser.add_argument("--device", default="cuda")
parser.add_argument("--data_download", default=False, required=False)
parser.add_argument("--image_processing", default=False, required=False)
parser.add_argument("--signal_processing", default=False, required=False)

args = parser.parse_args()

print(args)

if args.data_download:
    import os
    os.system("data_download.bat")


method = FileLoader

FileLoader.unzip()