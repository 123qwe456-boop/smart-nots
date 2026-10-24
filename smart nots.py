# 1. Skill: Using read(n) to peek at the first few characters of the file
with open("notes.txt", "r") as file_peek:
    preview = file_peek.read(30)
    print("--- File Preview ---")
    print(preview)
    print("--------------------\n")

# 2. Skill: Using readlines() to pull all lines into a list
with open("notes.txt", "r") as file_lines:
    all_lines = file_lines.readlines()

clean_lines = []

# 3. Skill: Looping line by line through the captured lines
for line in all_lines:
    # 4. Skill: Filtering with startswith() to find valid items
    if line.startswith("IMPORTANT:") or line.startswith("TODO:"):
        clean_lines.append(line)

# 5. Skill: Writing selected lines to a new file
with open("clean_notes.txt", "w") as clean_file:
    clean_file.writelines(clean_lines)

print(f"Success! Filtered out {len(all_lines) - len(clean_lines)} junk lines.")
print("Your clean notes have been saved to 'clean_notes.txt'.")
