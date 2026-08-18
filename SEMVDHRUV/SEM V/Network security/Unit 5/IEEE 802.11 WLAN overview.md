
# IEEE 802.11 WLAN Architecture

### Basic Service Set

- A set of stations controlled by a single coordination function.
- Coordination function The logical function that determines when a station operating within a BSS is permitted to transmit and may be able to receive PDUs.
![[IMG-20251119154126253.png|400]]

## Extended Service Set
- A set of one or more interconnected BSSs and integrated LANs that appear as a single BSS to the LLC layer at any station associated with one of these BSSs.
![[IMG-20251119154126332.png|400]]

## Access point (AP)
Any entity that has station functionality and provides access to the distribution system via the wireless medium for associated stations.
## Distribution system (DS)
A system used to interconnect a set of BSSs and integrated LANs to create
an ESS.
## MAC protocol data unit (MPDU)
The unit of data exchanged between two peer MAC entities using the services of the physical layer.

## MAC service data unit (MSDU)
Information that is delivered as a unit between MAC users. Station Any device that contains an IEEE 802.11 conformant MAC and physical layer.

# Operation

1. Access points periodically broadcast a beacon that contains SSID and security level
2. Subscriber stations listen to these beacons and determine the signal strength of the Network
3. Subscriber stations can also send a 'probe' to find a AP. This can be useful to find Networks that don't broadcast beacon
4. AP authenticates with the subscribers stations using shared key
5. Subscriber stations and AP communicate through encrypted mediums
6. Subscriber stations can a "Disassociate" message and log off 

# Services

![[IMG-20251119154126402.png]]