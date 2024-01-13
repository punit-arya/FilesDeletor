import os

def deleteDuplicateFiles(dir):
	for (currDir, subDirs, files) in os.walk(dir):
		# print(currDir, ":", sep = "")
		# for d in sorted(subDirs):
		# 	print("\t", d, sep = "")
		for f in sorted(files):
			print(currDir + os.sep + f, sep = "")
			name, ext = os.path.splitext(f)
			if name.endswith(" (2)"):
				origName = name.removesuffix(" (1)")
				# print("origName:", origName)
				if origName + ext in files and abs(os.stat(currDir + os.sep + origName + ext).st_mtime - os.stat(currDir + os.sep + f).st_mtime) <= 120 and os.stat(currDir + os.sep + origName + ext).st_size == os.stat(currDir + os.sep + f).st_size:	# Could use math.isclose(1000, 1004, abs_tol = 5).
					print("\tDeleting...", end = "")
					os.remove(currDir + os.sep + f)
					print(" done")

if __name__ == "__main__":
	deleteDuplicateFiles("/home/punit/doc/_Office/Mobileum")