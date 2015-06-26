# bitmask-root
Administrative service for bitmask client.

# Installation
1- Install TAP driver for windows in third-party\tap-windows directory.
2- Copy .ovpn config file to third-party\openvpn.
3- Add an environment variable named BITMASK_HOME and save bitmask-root directory as value.
4- Install windows service by following command (Run command prompt as administrator): 

```batch
windows_installer.py -install
```

5- Then start windows service:

```batch
windows_installer.py -start
```

# Usage
bitmask-root has four functionality that you can call them as a rpcclient, functionalities that bitmask-root supports are :

1- start_firewall
2- stop_firewall
3- start_openvpn
4- stop_openvpn

# Example
```code
client = RPCClient("tcp://%s:%s" % (127.0.0.1, 8080))
client.start_firewall()
```

