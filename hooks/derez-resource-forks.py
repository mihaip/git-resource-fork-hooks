#!/usr/bin/python

import os.path
import subprocess

# We're most likely in .git/hooks/pre-commit, find the root of the repo
root_dir = __file__
while os.path.basename(root_dir) != ".git":
    root_dir = os.path.dirname(root_dir)
root_dir = os.path.abspath(os.path.dirname(root_dir))

sdk_path = subprocess.check_output(["xcrun", "--sdk", "macosx", "--show-sdk-path"]).strip()
# Ideally `git diff --cached --name-only` would be enough, but it will not
# detect modifications that only happen to the resource forks, so we
# need to run this over all existing files too.
all_files = set(
    subprocess.check_output(["git", "ls-tree", "--name-only", "-r", "HEAD"]).split("\n") +
    subprocess.check_output(["git", "diff", "--cached", "--name-only"]).split("\n"))
resource_fork_count = 0
for file in all_files:
    file_path = os.path.join(root_dir, file)
    if os.path.exists(file_path + "/..namedfork/rsrc"):
        r_contents = subprocess.check_output(["DeRez", "-isysroot", sdk_path, file_path, "Carbon.r"])
        file_rpath = file_path + ".r"
        with open(file_rpath, "w") as r_file:
            r_file.write("/* Resource fork of %s */\n" % file)
            r_file.write(r_contents)
        subprocess.check_output(["git", "add", file_rpath])
        resource_fork_count += 1

if resource_fork_count:
    print ("%d files had resource forks, for which parallel .r files were created. You may need to add them to set of git staged files." % resource_fork_count)
