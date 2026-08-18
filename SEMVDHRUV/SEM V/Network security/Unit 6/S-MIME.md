Secure Multipurpose Internet Mail Extension (S/MIME) is a security enhancement to the existing MIME framework

S/MIME provides encryption and digital signatures to each mail to enhance the security of the mail services


## Operational Description

S/MIME provides for four message-related services.
- authentication
- confidentialilty
- compression
- email compatibility

### Authentication (Signing Mails)
provided by means of a digital signature. commonly RSA with SHA-256 is used

Sequence 
1. The sender creates a message.
2. SHA-256 is used to generate a 256-bit message digest of the message.
3. The message digest is encrypted with RSA using the sender’s private key
	1. and the result is appended to the message.
	2. Also appended is identifying information for the signer
	3. enable the receiver to retrieve the signer’s public key.
4. The receiver uses RSA with the sender’s public key to decrypt and recover the
message digest.
5. The receiver generates a new message digest for the message and compares
it with the decrypted hash code. If the two match, the message is accepted as
authentic

### Confidentiality (Encrypting Mails)
provides it by encrypting the message. Most commonly RSA 128 bit key is used.

Sequence
1. Sender generates a 128 bit key called ***content encryption key*** to encrypt the mails to be sent
2. Message is ***encrypted*** to using the key
3. The content encryption key is then encrypted using the ***receiver's public key***
4. Receiver ***decrypts*** the content encryption key using theirs's private key
5. Receiver uses the content encryption key to ***decrypt*** the contents of the mail


### Signing and Encrypting the Mail
![[Pasted image 20251112130237.png| 600]]

### Compression
* S/MIME can **compress messages** to save transmission and storage space.
* Compression can occur **before or after** signing and encryption.
**RFC 5751 guidelines:**
* Avoid compressing **binary encrypted data** — little to no size reduction.
* **Base64-encoded encrypted data** may benefit from compression.
* If using a **lossy compression algorithm**, **compress before signing** to prevent signature mismatches.

### Choosing Cryptographic Suites
* **If recipient capabilities known:** use the **highest-preference** algorithm supported by both.
* **If past messages exist:** use the **same algorithm** as last signed & encrypted message from recipient.
* **If recipient’s capabilities unknown:**
  * **Willing to risk incompatibility:** use **Triple DES**.
  * **Not willing to risk incompatibility:** use **RC2/40**.

| **Operation**                                 | **MUST Support** | **SHOULD Support**                                                                              |
| --------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------- |
| **Create message digest**                     | SHA-256          | SHA-1<br>Receiver SHOULD support MD5 (for backward compatibility)                               |
| **Form digital signature**                    | RSA with SHA-256 | DSA with SHA-256<br>RSASSA-PSS with SHA-256<br>RSA with SHA-1<br>DSA with SHA-1<br>RSA with MD5 |
| **Encrypt session key for transmission**      | RSA encryption   | RSAES-OAEP<br>Diffie–Hellman ephemeral-static mode                                              |
| **Encrypt message with one-time session key** | AES-128 CBC      | AES-192 CBC<br>AES-256 CBC<br>Triple DES CBC                                                    |

### S/MIME Messages
