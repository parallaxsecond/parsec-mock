import socket

import base64

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = "./parsec.sock"
print("connecting to %s" % server_address)

sock.connect(server_address)
exit_code = 0

try:
    # Send data
    message = "EKfAXh4AAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAA"
    bin_message = base64.b64decode(message)

    expected_response = "EKfAXh4AAQAAAAAAAAAAAAAAAAAAAAIAAAAAAAEAAAAAAAAACAE="
    bin_expected = base64.b64decode(expected_response)

    print('sending "%s"' % message)
    sock.sendall(bin_message)

    received_data = sock.recv(4096)
    print("received {}".format(base64.b64encode(received_data).decode("ascii")))
    if bin_expected == received_data:
        print("Received expected response")
    else:
        print("Did not get expected response")
        exit_code = 1
finally:
    print("closing socket")
    sock.close()
    exit(exit_code)
