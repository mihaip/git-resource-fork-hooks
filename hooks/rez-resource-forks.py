#!/usr/bin/python

import os.path
import subprocess

# We're most likely in .git/hooks/post-merge, find the root of the repo
root_dir = __file__
while os.path.basename(root_dir) != ".git":
    root_dir = os.path.dirname(root_dir)
root_dir = os.path.abspath(os.path.dirname(root_dir))

sdk_path = subprocess.check_output(["xcrun", "--sdk", "macosx", "--show-sdk-path"]).strip()
all_files = subprocess.check_output(["git", "ls-tree", "--name-only", "-r", "HEAD"]).split("\n")
resource_fork_count = 0
for file in all_files:
    if not file.endswith(".r"):
        continue
    file_rpath = os.path.join(root_dir, file)
    file_path = os.path.join(root_dir, file[:-2])
    if os.path.exists(file_path):
        with open(file_rpath, "r") as r_file:
            if "/* Resource fork of" not in r_file.readline():
                continue
        subprocess.check_output([
            "Rez",
            "-isysroot", sdk_path,
            "-o", file_path,
            "-m", # Don't change modification date
            "Carbon.r",
            file_rpath])
        resource_fork_count += 1

if resource_fork_count:
    print ("Resource forks were reconstructed from %d parallel .r files" % resource_fork_count)
