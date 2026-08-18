In WPA2, it is a process between station and the access point (AP) that takes place in 4 steps

1. AP sends a random number (anonce)
	Client receives the anonce and generates PTK (Pair-Wise transient key)
	Client already has Pair-Wise Master Key (PMK), Station Nonce (snonce), and now with access to anonce
2. Client sends snonce, anonce, pmk with MIC (Message Integrity Check)
	MIC helps AP to determine if the PMK was tempered
	Using this info AP derives PTK that derived by the STA using the same algorithm
3. Using PTK, AP generates GTK (Group Temporal Key) and encrypts it using PTK as a key for KEK algorithm 
	AP sends the GTK along with anonce and MIC
4. Station (client) decryptes the GTK using PTK. 
	After MIC verification, STA (client) sends the ack to the AP that the handshake is completed and the keys were installed successfully.