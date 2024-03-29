import io
import os
import sqlite3
import time
import lzma

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
					os.rename(currentDirectory + os.sep + f, "/home/punit/trash")
					print(" done.")

def deleteSubsets(directory):
	for (currentDirectory, subdirectories, files) in os.walk(directory):
		for f in sorted(files):
			if f.endswith(".sqlite"):
				with open("history.sql", "a") as historyFile:
					connection = sqlite3.connect(currentDirectory + os.sep + f)
					# cursor = connection.cursor()
					# for table in ["moz_anno_attributes", "moz_annos", "moz_bookmarks", "moz_bookmarks_deleted", "moz_historyvisits", "moz_inputhistory", "moz_items_annos", "moz_keywords", "moz_meta", "moz_origins", "moz_places"]:
					# 	print("SELECT * FROM pragma_table_info(" + table + ");")
					# 	rows = cursor.execute("SELECT * FROM pragma_table_info(\"" + table + "\");")
					# 	open("../var/pragma_" + table + "_info.txt", "a").write("\n".join(map(str, rows.fetchall())))
					# 	print("SELECT * FROM " + table + ";")
					# 	rows = cursor.execute("SELECT * FROM " + table + ";")
					# 	open("../var/" + table + ".txt", "w").write("(")
					# 	open("../var/" + table + ".txt", "a").write(", ".join([col[0] for col in rows.description]))
					# 	open("../var/" + table + ".txt", "a").write(")\n")
					# 	open("../var/" + table + ".txt", "a").write("\n".join(map(str, rows.fetchall())))
					# rows = cursor.execute("SELECT url, title, visit_date FROM moz_historyvisits, moz_places WHERE moz_historyvisits.place_id = moz_places.id;")
					# # open("history.txt", "w").write("\n".join(map(str, rows.fetchall())))
					# for row in rows.fetchall():
					# 	historyFile.write("| ")
					# 	for index, cell in enumerate(row):
					# 		if index != 2:
					# 			historyFile.write(str(cell) + " | ")
					# 		elif index == 2:
					# 			historyFile.write(time.ctime(cell // 1000000) + " | ")
					# 	historyFile.write("\n")
					print(currentDirectory + os.sep + f + ":")
					for line in connection.iterdump():
						line = line.strip().replace("\n", "$$$$")
						# historyFile.seek(0, 0)
						# if line not in historyFile.readlines():
						# 	historyFile.seek(0, 2)
						# 	historyFile.write("%s\n" % line)
						historyFile.write("%s\n" % line)
					connection.close()
					os.system("sort history.sql | uniq > history_cleaned.sql ; mv history_cleaned.sql history.sql")
					data = open(currentDirectory + os.sep + f, "rb")
					with lzma.open(currentDirectory + os.sep + f + ".xz", "wb") as xZFile:
						xZFile.write(data.read())

if __name__ == "__main__":
	# deleteDuplicateFiles("/home/punit/doc/_Office/Mobileum")
	deleteSubsets("/home/punit/doc/_Misc/Logs/Browser")