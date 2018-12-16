import asyncio


class Shutdown(Exception):
    pass


class ServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.write('welcome\n')

    def data_received(self, data):
        if not data:
            return
        message = data.decode('ascii')
        command = message.strip().split(' ')[0].lower()
        args = message.strip().split(' ')[1:]
        if not hasattr(self, 'command_%s' % command):
            self.write('invalid command:%s' % command)
            return
        try:
            return getattr(self, 'command_%s' % command)(*args)
        except Exception as ex:
            self.write('error:%s' % str(ex))

    def write(self, msg_str):
        msg_str += '\n'
        self.transport.write(msg_str.encode('ascii', 'ignore'))

    def command_add(self, *args):
        args = [int(i) for i in args]
        self.write("%d" % sum(args))

    def command_shutdown(self):
        self.write('okey, shutting down')
        raise KeyboardInterrupt

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ServerProtocol, '127.0.0.1', 8000)
    asyncio.async(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
