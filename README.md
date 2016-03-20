# bitmask-root
bitmask-root is an administrative service module which helps bitmask client to work on windows as well as other operating systems.

# Installation
First of all generate binaries and third parties, to do this simply run buildexe.py then you'll see dist and third-party directories
which contain executable win32 files. Install Openvpn and TUN/TAP driver which have been downloaded by buildexe.py in third-party directory, finally install windows service by following command (Run command prompt as administrator): <br />

```batch
windows_installer.exe install
```

Then start windows service:<br />

```batch
windows_installer.exe start
```

# Usage
bitmask-root has four important functionalities which you can call them as a rpc client:
<br />
<ul>
<li>start_firewall()</li>
<li>stop_firewall()</li>
<li>start_openvpn(certificate path,log path)</li>
<li>stop_openvpn()</li>
</ul>

# Example
```code
client = RPCClient("tcp://%s:%s" % (127.0.0.1, 8080))
client.start_firewall()
```

