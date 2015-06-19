from jsonrpc2_zeromq import RPCClient

client = RPCClient("tcp://127.0.0.1:8080")

while True:
    cmd = raw_input()

    try:
        if cmd == "stop":
            client.stop_firewall()
            print "Firewall Stoped!"

        if cmd == "start":
            client.start_firewall()
            print "Firewall Started!"
    except:
        print "Service Problem!"
        break



