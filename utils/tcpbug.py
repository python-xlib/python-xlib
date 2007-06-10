#!/usr/bin/python

import socket
import select
import sys
import os

def tcpbug(listenaddr, destaddr, outputfd):
    listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen.bind(listenaddr)
    listen.listen(1)

    client, addr = listen.accept()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(destaddr)

    cwbuf = swbuf = outbuf = ''

    while client or server or outbuf:
        readset = []
        if client:
            readset.append(client)
        if server:
            readset.append(server)

        writeset = []
        if cwbuf and client:
            writeset.append(client)
        if swbuf and server:
            writeset.append(server)
        if outbuf:
            writeset.append(outputfd)

        readset, writeset, e = select.select(readset, writeset, [])

        if client in readset:
            data = client.recv(2000)
            if data:
                swbuf = swbuf + data
                outbuf = outbuf + 'C%d\n%s' % (len(data), data)
            else:
                client = None

        if server in readset:
            data = server.recv(2000)
            if data:
                cwbuf = cwbuf + data
                outbuf = outbuf + 'S%d\n%s' % (len(data), data)
            else:
                server = None

        if client in writeset:
            n = client.send(cwbuf)
            cwbuf = cwbuf[n:]

        if server in writeset:
            n = server.send(swbuf)
            swbuf = swbuf[n:]

        if outputfd in writeset:
            n = os.write(outputfd, outbuf)
            outbuf = outbuf[n:]

        if client and not cwbuf and not server:
            client.close()
            client = None

        if server and not swbuf and not client:
            server.close()
            server = None

def main():
    try:
        lport = int(sys.argv[1])
        dhost = sys.argv[2]
        dport = int(sys.argv[3])
    except (IndexError, ValueError):
        sys.stderr.write('Usage: %s listenport desthost destport\n'
                         % sys.argv[0])
        exit(1)

    tcpbug(('', lport), (dhost, dport), 1)

if __name__ == '__main__':
    main()
