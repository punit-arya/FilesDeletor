import os

def deleteDuplicateFiles(directory):
	for (currentDirectory, subdirectories, files) in os.walk(directory):
		# print(currentDirectory, ":", sep = "")
		# for d in sorted(subdirectories):
		# 	print("\t", d, sep = "")
		for f in sorted(files):
			print(currentDirectory + os.sep + f, sep = "")
			name, extension = os.path.splitext(f)
			if name.endswith(" (2)"):
				originalName = name.removesuffix(" (2)")
				if originalName + extension in files and abs(os.stat(currentDirectory + os.sep + originalName + extension).st_mtime - os.stat(currentDirectory + os.sep + f).st_mtime) <= 120 and os.stat(currentDirectory + os.sep + originalName + extension).st_size == os.stat(currentDirectory + os.sep + f).st_size:	# Could use math.isclose(1000, 1004, abs_tol = 5).
					print("\tDeleting...", end = "")
					os.remove(currentDirectory + os.sep + f)
					print(" done.")

if __name__ == "__main__":
	deleteDuplicateFiles("/home/punit/doc/_Office/Mobileum")
