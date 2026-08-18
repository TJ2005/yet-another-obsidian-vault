# Dynamic Packet Filtering

A type of [[Packet Filtering Firewall]] that can automatically adapt its rules based on network conditions.

## Characteristics
- Can react to new emerging situations
- Updates and creates rules to deal with events automatically
- Provides adaptive security posture

## How It Works
- Monitors incoming traffic patterns
- Detects anomalies (e.g., malformed packets)
- Automatically creates temporary rules to block threats
- Example: Drops all packets from a particular address when a lot of them are malformed

## Granularity
Dynamic Packet filtering allows only a particular packet along with a particular source-destination pair, rather than allowing entire classes of traffic like [[Static Packet Filtering]].

## Advantages
- Adaptive to emerging threats
- More granular control than static filtering
- Reduces need for manual intervention

## Comparison
- More sophisticated than [[Static Packet Filtering]]
- Less resource-intensive than [[Stateful Packet Inspection]]
- Part of Fourth Generation in [[Firewall Generations]]

---
