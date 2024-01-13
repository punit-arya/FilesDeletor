import os

def filesDeletor(dir):
	for (currDir, subDirs, files) in os.walk(dir):
		# print(currDir, ":", sep = "")
		# for d in sorted(subDirs):
		# 	print("\t", d, sep = "")
		for f in sorted(files):
			print(currDir + os.sep, f, sep = "")
			name, ext = os.path.splitext(f)
			# print("name:", name)
			# print("ext:", ext)
			if name.endswith(" (1)"):
				origName = name.removesuffix(" (1)")
				# print("origName:", origName)
				if origName + ext in files and os.stat(currDir + os.sep + origName + ext).st_mtime == os.stat(currDir + os.sep + f).st_mtime and os.stat(currDir + os.sep + origName + ext).st_size == os.stat(currDir + os.sep + f).st_size:
					print("Duplicate found!")

if __name__ == "__main__":
	filesDeletor("/home/punit/doc/_Office/Mobileum")