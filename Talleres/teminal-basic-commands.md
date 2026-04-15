# 🧪 Terminal Workshop: Linux + Windows Basics

## 🎯 Goal
By the end, you’ll be able to:
- Navigate the file system
- Create/delete files & folders
- View/edit content
- Search and filter data
- Chain commands
- Open projects in VS Code
- Understand admin/superuser privileges

---

# 🧩 Module 1 — Navigation

## 🔹 Core Commands

| Action | Linux | Windows |
|--------|-------|---------|
| Show current folder | `pwd` | `cd` |
| List files | `ls` | `dir` |
| Change directory | `cd folder` | `cd folder` |

## 🧪 Task 1: Explore your system

Linux:
    pwd
    ls

Windows:
    cd
    dir

Move into a folder:
    cd Documents

Go back:
    cd ..

---

# 🧩 Module 2 — Files & Folders

## 🔹 Core Commands

| Action | Linux | Windows |
|--------|-------|---------|
| Create folder | `mkdir test` | `mkdir test` |
| Create file | `touch file.txt` | `echo. > file.txt` |
| Delete file | `rm file.txt` | `del file.txt` |
| Delete folder | `rm -r test` | `rmdir /s test` |

## 🧪 Task 2: Build your workspace

    mkdir workshop
    cd workshop

Create files:
    touch notes.txt tasks.txt

Check:
    ls

Delete one file:
    rm tasks.txt

---

# 🧩 Module 3 — Viewing & Editing Content

## 🔹 Core Commands

| Action | Linux | Windows |
|--------|-------|---------|
| View file | `cat file.txt` | `type file.txt` |
| Add text | `echo "Hello" >> file.txt` | same |
| Clear screen | `clear` | `cls` |

## 🧪 Task 3: Write your first file

Add text:
    echo "I am learning terminal" >> notes.txt

View it:
    cat notes.txt

Add more lines:
    echo "This is fun" >> notes.txt

---

# 🧩 Module 4 — Search & Filters

## 🔹 Core Commands

| Action | Linux | Windows |
|--------|-------|---------|
| Search text | `grep "word" file.txt` | `findstr "word" file.txt` |

## 🧪 Task 4: Find something

    echo "apple" >> notes.txt
    echo "banana" >> notes.txt
    echo "apple pie" >> notes.txt

Search:
    grep "apple" notes.txt

---

# 🧩 Module 5 — Copy, Move, Rename

## 🔹 Core Commands

| Action | Linux | Windows |
|--------|-------|---------|
| Copy | `cp file1 file2` | `copy file1 file2` |
| Move/Rename | `mv file1 file2` | `move file1 file2` |

## 🧪 Task 5: Organize files

Copy:
    cp notes.txt backup.txt

Rename:
    mv backup.txt archive.txt

---

# 🧩 Module 6 — Combining Commands

## 🔹 Pipes (Linux)

    cat notes.txt | grep apple

## 🧪 Task 6: Filter smartly

    cat notes.txt | grep banana

---

# 🧩 Module 7 — VS Code from Terminal 🚀

## 🔹 Requirements
Make sure the `code` command works in your terminal.

If not:
- Open VS Code
- Press `Ctrl + Shift + P`
- Type: `Shell Command: Install 'code' command in PATH`

## 🔹 Core Commands

| Action | Command |
|--------|--------|
| Open current folder | `code .` |
| Open folder | `code myFolder` |
| Open file | `code file.txt` |
| Open new window | `code -n .` |

## 🧪 Task 7

    code .
    code notes.txt
    code -n .

---

# 🧩 Module 8 — Admin / sudo (⚠️ Important)

## 🔹 What is `sudo`?

In Linux, `sudo` means:
> "Run this command as a superuser (administrator)"

Example:
    sudo rm file.txt

This gives you **full system power**, including:
- Deleting protected files
- Installing software
- Changing system settings

⚠️ With great power comes great responsibility:
- You can break your system if you misuse it
- Always double-check commands before running with `sudo`

---

## 🔹 Windows Equivalent

Windows uses **Administrator privileges** instead of `sudo`.

To run as admin:
- Open terminal as Administrator
- Or right-click → "Run as administrator"

---

## 🔹 Common Admin Commands

Linux:
    sudo apt update
    sudo apt install nano

Windows:
    runas /user:Administrator cmd

---

## 🧪 Task 8 (Safe Practice)

Try a harmless command with sudo:

Linux:
    sudo ls

Windows (open admin terminal):
    dir

💡 Observe:
- You may be asked for your password
- Some commands only work with admin rights

---

## 🧠 Key Concept

Normal user → limited access  
Admin/sudo → full control  

Use `sudo` only when needed.

---

# 🏁 Final Challenge

Try without looking back:

1. Create a folder `project`
2. Create `data.txt`
3. Add 5 lines
4. Search for a word
5. Copy and rename file
6. Delete original
7. Open in VS Code
8. Run one command with sudo/admin

---

# 🚀 Next Steps

- Permissions (`chmod`, `icacls`)
- Processes (`ps`, `tasklist`)
- Networking (`ping`, `curl`)
- Git basics