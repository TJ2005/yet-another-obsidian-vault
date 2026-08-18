---

Title: "System Adminstrator Lab 1"

Status:

marker:

tags:

Date: "2026.01.08"

Time: "13:11"

---
# **Experiment 1: Install Ubuntu OS & Study Its File System**

---


## **Aim**

To install the Ubuntu Linux operating system and study its hierarchical file system structure and important directories.

---

## **Learning Objectives**

1. Install Ubuntu Linux on a system or virtual machine.
2. Understand the Linux directory hierarchy.
3. Identify the purpose of important system directories.
4. Use basic Linux commands to explore the file system.

---

## **Prerequisites**

- Basic knowledge of operating systems
- Basic understanding of computer hardware
- Familiarity with command-line interface (optional)

---

## **Software / Hardware Requirements**

| Component | Specification |
|-----------|--------------|
| OS | Ubuntu 20.04 LTS / 22.04 LTS |
| Processor | Intel/AMD x64 |
| RAM | Minimum 4 GB |
| Storage | Minimum 25 GB free space |
| Virtualization | VirtualBox / VMware (optional) |
| Bootable USB | Rufus / Balena Etcher |

---

## **Theory**

### Ubuntu Operating System

![[IMG-20260420174731668.png]]

Ubuntu is an open-source, Linux-based OS developed by Canonical Ltd., widely used in desktops, servers, cloud platforms, and embedded systems.

### Linux File System

Linux follows a hierarchical tree structure starting from the root directory `/`. Every file and directory is organized under this root.

![[IMG-20260420174731732.png]]

### Important Directories

| Directory | Description |
|-----------|-------------|
| `/` | Root directory – top of the file system |
| `/bin` | Essential binary executables |
| `/boot` | Boot loader and kernel files |
| `/dev` | Device files |
| `/etc` | System configuration files |
| `/home` | User home directories |
| `/lib` | Shared libraries |
| `/media` | Mounted removable media |
| `/mnt` | Temporary mount point |
| `/opt` | Optional software packages |
| `/proc` | Process information (virtual) |
| `/root` | Home directory of root user |
| `/sbin` | System binaries |
| `/tmp` | Temporary files |
| `/usr` | User utilities and applications |
| `/var` | Variable files (logs, mail, cache) |

---

## **Procedure**

### Part A: Installation of Ubuntu OS (Virtual Machine)

1. Download Ubuntu ISO from the official website.
2. Install VirtualBox / VMware.
3. Create a new VM: Type = Linux, Version = Ubuntu (64-bit).
4. Allocate RAM: 2–4 GB, Storage: 25 GB (dynamic).
5. Attach Ubuntu ISO and start VM.
6. Select **Install Ubuntu** and follow on-screen instructions:
   - Language & keyboard layout
   - Normal installation with automatic partitioning
7. Create username and password, then reboot.

---

### Part B: Studying Ubuntu File System

**Step 1:** Login and open Terminal (`Ctrl + Alt + T`).

**Step 2:** Execute basic commands.

`pwd`

![[IMG-20260420174731755.png]]

`ls`

![[IMG-20260420174731817.png]]

`ls /`

![[IMG-20260420174731837.png]]

`ls -l`

![[IMG-20260420174731900.png]]

`tree -L 1 /`

![[IMG-20260420174731929.png]]

![[IMG-20260420174731972.png]]

---

### Task 1: Exploring Key Directories

![[IMG-20260420174732015.png]]

**`/bin`** – Essential binary executables.
- `ls` – Lists files and directories.
- `cp` – Copies files or directories.
- `rm` – Deletes files or directories.

**`/boot`** – OS startup files: `vmlinuz` (kernel), `initrd.img` (RAM disk), `grub` (bootloader).

**`/dev`** – Hardware device files: `sda` (disk), `tty` (terminal), `null` (null device).

**`/etc`** – Configuration files: `passwd`, `fstab`, `hosts`.

**`/home`** – User personal directories: `kali/`, `Desktop/`, `Documents/`.

**`/lib`** – Shared libraries: `libc.so`, `ld-linux.so`, `modules/`.

**`/media`** – Removable media mounts: `usb0`, `cdrom`.

**`/mnt`** – Temporary mount points created by admin.

**`/opt`** – Optional/third-party software packages.

**`/proc`** – Virtual FS for runtime info: `cpuinfo`, `meminfo`, `uptime`.

**`/root`** – Root user's home: `.bashrc`, `.profile`.

**`/sbin`** – Admin binaries: `ifconfig`, `reboot`, `fdisk`.

**`/tmp`** – Temporary cache and socket files.

**`/usr`** – User utilities: `bin/`, `lib/`, `share/`.

**`/var`** – Frequently changing files: `log/`, `cache/`, `mail/`.

---

**Step 3:** Navigate to important directories.

`cd /etc` → `ls`

![[IMG-20260420174732055.png]]

![[IMG-20260420174732099.png]]

`cd /home` → `ls`

![[IMG-20260420174732139.png]]

![[IMG-20260420174732185.png]]

`cd /var/log` → `ls`

![[IMG-20260420174732249.png]]

![[IMG-20260420174732270.png]]

---

### My Own 5 Extra Commands

| Command | Purpose |
|---------|---------|
| `whoami` | Displays the current logged-in user |
| `uname -a` | Displays system and kernel information |
| `df -h` | Shows disk space usage in human-readable format |
| `du -sh ~` | Displays total disk usage of the user home directory |
| `stat <file>` | Detailed file info: permissions, ownership, timestamp |

![[IMG-20260420174732335.png]]

![[IMG-20260420174732355.png]]

![[IMG-20260420174732405.png]]

![[IMG-20260420174732432.png]]

![[IMG-20260420174732530.png]]

---

## **Observations**

From `ls -l /` output:
- Permissions are displayed as `rwx` (read/write/execute) for owner, group, and others.
- System directories (`/etc`, `/usr`, `/var`, `/bin`) have `drwxr-xr-x` — root has full access, others have read+execute.
- `/root` and `/lost+found` have `drwx------` — restricted to root only.
- Symbolic links start with `l`: `bin -> usr/bin`, `lib -> usr/lib`.
- Most system files are owned by `root:root`; user dirs like `/home/kali` are owned by the respective user.

### Summary Table

| Command | Purpose |
|---------|---------|
| `pwd` | Displays present working directory |
| `ls` | Lists directory contents |
| `ls -l` | Detailed list with permissions |
| `cd` | Change directory |
| `tree` | Display directory tree |
| `df -h` | Disk usage |
| `mount` | Mounted file systems |

---

## **Result**

Ubuntu Linux OS was successfully installed and the Linux file system structure was studied. The purpose and organization of major system directories were understood using terminal commands.

---

## **Precautions**

1. Ensure sufficient disk space before installation.
2. Do not delete system files or directories.
3. Use `sudo` commands carefully.
4. Follow proper shutdown procedure.

---

## **Viva-Voce Questions**

1. **What is the root directory in Linux?**
   → `/` is the top-level directory; all other files and directories are stored under it.

2. **Difference between `/bin` and `/sbin`?**
   → `/bin` has basic commands for all users; `/sbin` has system administration commands for root.

3. **Purpose of `/etc` directory?**
   → Stores system-wide configuration files and settings required for operation.

4. **Why is `/proc` a virtual file system?**
   → It doesn't store real files on disk; it provides live info about processes and hardware.

5. **Difference between `/home` and `/root`?**
   → `/home` has directories of normal users; `/root` is the home directory of the root user.

---

## **Conclusion**

This lab helped in understanding the Linux file system structure and the purpose of important directories. Basic knowledge of file permissions and system organization was gained using terminal commands.

---

## **See Also**

- [[System Adminstrator Lab 2]] — Users are stored in `/etc/passwd` and home dirs in `/home` — both covered here; `chmod`/`chown` concepts from Lab 2 apply to file permissions studied here
- [[System Adminstrator Lab 5]] — Apache's config dir `/etc/apache2`, web root `/var/www`, and log dir `/var/log/apache2` are all part of the file hierarchy covered here

---

# References


###### Information
- date: 2026.01.08
- time: 13:11