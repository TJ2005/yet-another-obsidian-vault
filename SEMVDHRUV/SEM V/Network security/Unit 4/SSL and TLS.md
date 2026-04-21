
# SSL
SSL (Secure Sockets Layer) is a protocol that encrypts data between client and server to ensure secure, authenticated, and tamper-proof communication over the internet. It has been succeeded by TLS (Transport Layer Security), which is now the standard.

# TLS
TLS (Transport Layer Security) is a successor SSL. It is a cryptographic protocol that provides security services to various higher layer protocols like HTTP. 

## Key functions

Authentication: Verifies identities using certificates
Encryption: Encrypts the data so it remains confidential during transit
Integrity: Ensures the data isn't tampered during transmission

## Handshake process
1. Client hello - Client sends the list of supported versions and cipher suits.
2. Server hello -  Server selects the TLS version and a cipher suit based on its preference
3. 