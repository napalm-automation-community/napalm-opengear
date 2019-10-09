# ? (10.230.3.144) at 74:83:ef:ee:ea:29 [ether] on eth1
# ? (10.230.3.16) at 74:83:ef:ee:f6:e1 [ether] on eth0
Value IP ([a-f0-9\.:]+)
Value MAC ([a-fA-F0-9:]+)
Value INTERFACE (\w+\d+)

Start
  ^\s*\?\s+\(${IP}\)\s+at\s+${MAC}\s+\[ether\]\s+on\s+${INTERFACE} -> Record
