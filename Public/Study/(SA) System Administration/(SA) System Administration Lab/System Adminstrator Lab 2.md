---

Title: "System Adminstrator Lab 2"

Status:

marker:

tags:

Date: "2026.01.22"

Time: "13:11"

---
# **Experiment 2: Managing Users and Groups in Linux**

---
**Name:** Tejas Sahoo
**Roll Number:** K057

## **Aim**

To create and manage user and group accounts on the Linux OS.

---

## **Learning Outcomes**

1. Create new users and groups.
2. Modify user and group properties.
3. Disable and safely remove a user account.

---

## **Theory**

User management is critical for maintaining a secure system. Ineffective privilege management often leads to compromise.

- Users can be human or system application accounts.
- **Groups** logically organize users for a shared purpose.
- File ownership and permissions are tied to **UID** (User ID) and **GID** (Group ID).
- A **User Private Group (UPG)** is created automatically when a new user is added.
- The **`umask`** controls default file permissions.
- Group information is stored in `/etc/group`.

---

## **Procedure & Observations**

---

### **Task 1: Creating a User Account**

![[IMG-20260420174732554.png]]

```bash
# Read manual
man adduser

# Create users (as root)
adduser --disabled-password --gecos ',' tejas1
adduser --disabled-password --gecos ',' tejas2
adduser --disabled-password --gecos ',' tejas3

# Verify in /etc/passwd
grep 'tejas' /etc/passwd
```

**Output:**
```
tejas2:x:1003:1003::/home/tejas2:/bin/bash
tejas1:x:1004:1004:,:/home/tejas1:/bin/bash
tejas3:x:1005:1005:,:/home/tejas3:/bin/bash
```

**Observation:** Users `tejas1` (UID 1004), `tejas2` (UID 1003), `tejas3` (UID 1005) were created, each with a home directory under `/home/` and default shell `/bin/bash`.

---

### **Task 2: Creating a New Group**

```bash
# Read manual
man addgroup

# Create group
addgroup mpstme

# Verify in /etc/group
grep 'mpstme' /etc/group
```

**Output:**
```
mpstme:x:1006:
```

**Observation:** Group `mpstme` was created with GID `1006` and verified in `/etc/group`.

---

### **Task 3: Enrolling a User in Another Group**

```bash
# Check current group membership
groups tejas1

# Add users to group mpstme
adduser tejas1 mpstme
adduser tejas2 mpstme

# Verify membership
groups tejas1
groups tejas2
```

**Output:**
```
tejas1 : tejas1 users
tejas1 : tejas1 users mpstme
tejas2 : tejas2 users mpstme
```

**Observation:** `tejas1` and `tejas2` were enrolled in group `mpstme`. Membership verified with `groups` command.

---

### **Task 4: Change Default Shell**

```bash
# Read manual
man chsh

# Change shell of tejas1 to /bin/sh
chsh -s /bin/sh tejas1

# Verify
grep 'tejas1' /etc/passwd
```

**Output:**
```
tejas1:x:1004:1004:,:/home/tejas1:/bin/sh
```

**Observation:** Default shell of `tejas1` was changed from `/bin/bash` to `/bin/sh` and verified in `/etc/passwd`.

---

### **Task 5: User Profile Security**

```bash
# Check home directory permissions
ls -ld /home/tejas1

# Remove world-readable permission
chmod o-r /home/tejas1

# Verify
ls -ld /home/tejas1
```

**Output:**
```
drwxr-xr-x 5 tejas1 tejas1 4096 Feb 23 12:45 /home/tejas1
drwxr-x--x 5 tejas1 tejas1 4096 Feb 23 12:45 /home/tejas1
```

**Observation:** World-readable (`o-r`) permission was removed from the home directory. Permissions changed from `drwxr-xr-x` to `drwxr-x--x`, securing the user profile.

---

### **Task 6: Temporarily Disable / Enable Account**

```bash
# Set password first
echo 'tejas1:pass123' | chpasswd

# Lock the account
passwd -l tejas1

# Unlock the account
passwd -u tejas1
```

**Output:**
```
passwd: password changed.
passwd: password changed.
```

**Observation:** Account lock and unlock operations completed successfully. The `!` prefix added to the password hash in `/etc/shadow` during lock was removed on unlock.

---

### **Task 7: Deleting User and Group**

```bash
# Copy home directory before deletion
cp -r /home/tejas3 /root/tejas3_backup
echo 'Backup done'

# Delete user
deluser tejas3

# Delete group
delgroup mpstme

# Verify deletion
grep tejas3 /etc/passwd || echo 'tejas3: deleted'
grep mpstme /etc/group  || echo 'mpstme: deleted'
```

**Output:**
```
Backup done
tejas3: deleted
mpstme: deleted
```

**Observation:** `tejas3`'s home directory was backed up to `/root/tejas3_backup` before deletion. User and group were removed successfully.

---

## **Result**

User creation, group assignment, shell configuration, account locking/unlocking, and safe deletion were all successfully performed and verified in Kali Linux using root privileges.

---

## **Review Questions**

1. **What privileges are required to create a user in Ubuntu?**
   → Root (`sudo`) privileges are required to create a user.

2. **Which file stores user and group information?**
   → `/etc/passwd` stores user info; `/etc/group` stores group info; `/etc/shadow` stores passwords.

3. **What modes are supported by `adduser` and `addgroup`?**
   → Interactive mode (guided prompts) and non-interactive mode (with `--disabled-password` or flags).

4. **Which commands change ownership and permissions of files?**
   → `chown` changes ownership; `chmod` changes permissions.

5. **Does deleting an account delete the home directory?**
   → Not by default with `deluser`; use `deluser --remove-home` to also delete the home directory.

6. **How can you ensure home directories are not world-readable?**
   → Use `chmod o-rwx /home/<user>` or set `umask 077` in `/etc/profile` or `/etc/login.defs`.

---

## **Conclusion**

This experiment demonstrated effective user and group management in Kali Linux. User creation, group assignment, security configuration, account locking, and safe deletion were successfully performed and verified using root privileges.

---

## **See Also**

- [[System Adminstrator Lab 1]] — The `/home`, `/etc/passwd`, `/etc/group`, and `/etc/shadow` files modified here are part of the Linux file hierarchy studied in Lab 1
- [[System Adminstrator Lab 5]] — `chown -R $USER:$USER` and `chmod -R 755` used in Lab 5's virtual host setup are user/permission commands covered here

---

# References


###### Information
- date: 2026.01.22
- time: 13:11
