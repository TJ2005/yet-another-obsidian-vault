IEEE 802.1X Port-Based Network Access. It comprises of two important factors. 
- Data Line ( Controlled Part ) : responsible for the transmission of authenticated and encrypted data
- Auth Line ( Uncontrolled Part ): Responsible for the authentication of the supplicant.

Until the AS Authenticates a supplicant The authenticator only passes the control and authentication messages between the supplicant and the server over the uncontrolled part ( Auth Line ).

Once the authorization has been completed the data line is unblocked and the stacked data that was being sent is now forwarder to its meant decision.

A supplicant only send data if their state is authorized.

## **EAPOL (Extensible Authentication Protocol over LAN)**

### **Overview**

* **EAPOL** is a Layer 2 protocol defined in the **IEEE 802.1X standard**.
* It is used for **authentication control** between a **Supplicant** (client device) and an **Authenticator** (network device such as a switch or access point).
* EAPOL encapsulates and transports **EAP (Extensible Authentication Protocol)** messages over a **LAN** environment (Ethernet or wireless).

---

## **Common EAPOL Packet Types**

| **EAPOL Packet Type** | **Purpose / Function**                                                                                                                                                |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **EAPOL-Start**       | Sent by the **Supplicant** to discover the presence of an **Authenticator** and to signal readiness to begin authentication.                                          |
| **EAPOL-EAP**         | Used by the **Authenticator** to send **EAP-Request/Response** messages encapsulated within EAPOL frames. This is the **EAPOL frame type for carrying EAP messages**. |
| **EAPOL-Key**         | Used by the **Authenticator** to deliver **cryptographic keys** to the Supplicant once authentication is successful (e.g., session keys in WPA/WPA2).                 |
| **EAPOL-Logoff**      | Sent by the **Supplicant** to indicate that it wishes to **terminate the connection** or log off from the network.                                                    |

---

## **Operation Flow**

### **1. Initial Connection**

* When a **Supplicant** first connects to the LAN, it:

  * Does **not know** the **MAC address** of the Authenticator.
  * Does **not know** whether an Authenticator even exists on the LAN.

### **2. Discovery**

* The Supplicant sends an **EAPOL-Start** frame to a **special group multicast address** reserved for **IEEE 802.1X Authenticators**.
* This frame helps:

  * Detect the presence of an Authenticator.
  * Notify the Authenticator that the Supplicant is ready to authenticate.

### **3. Authenticator Response**

* In some cases, the Authenticator already knows a new device is connected (e.g., through **hardware notifications** such as link-up signals from a hub or switch port).
* The Authenticator may **initiate authentication** by sending its own message before receiving the EAPOL-Start.

### **4. Identity Request**

* The Authenticator sends an **EAP-Request/Identity** message encapsulated within an **EAPOL-EAP** frame.
* The Supplicant responds with an **EAP-Response/Identity** message (also inside EAPOL-EAP).

### **5. Key Exchange**

* After successful authentication (e.g., validated via a RADIUS server), the Authenticator uses **EAPOL-Key** packets to deliver **encryption keys** to the Supplicant.

### **6. Logoff**

* When the Supplicant wishes to disconnect, it sends an **EAPOL-Logoff** packet to inform the Authenticator to terminate the session and revoke network access.

---

## **EAPOL Packet Format**

| **Field**              | **Description**                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Protocol Version**   | Indicates the version of EAPOL being used. Ensures compatibility between devices.                            |
| **Packet Type**        | Specifies the type of EAPOL message (Start, EAP, Key, Logoff, etc.).                                         |
| **Packet Body Length** | Specifies the length of the packet body (if present). Used to determine how much data follows the header.    |
| **Packet Body**        | The actual payload of the EAPOL packet. This can be an EAP message, key information, or other relevant data. |

---

### **Simplified EAPOL Packet Example**

```
+---------------------+
| Protocol Version    |  (1 byte)
+---------------------+
| Packet Type         |  (1 byte)
+---------------------+
| Packet Body Length  |  (2 bytes)
+---------------------+
| Packet Body         |  (variable, optional)
+---------------------+
```

Example: An **EAPOL-EAP** packet will have an **EAP message** (such as EAP-Request Identity) in its **Packet Body**.

---

## **Summary**

* **EAPOL** acts as the **communication mechanism** between Supplicant and Authenticator at the data link layer.
* It is critical to **port-based network access control** in IEEE 802.1X.
* The **most common packet types** are:

  * **EAPOL-Start**
  * **EAPOL-EAP**
  * **EAPOL-Key**
  * **EAPOL-Logoff**
* Each serves a specific function — from session initiation to secure key exchange and session termination.
* The **EAPOL frame structure** ensures these control messages can be reliably transmitted over Ethernet before the data port is authorized.

---

