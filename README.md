# FlaskWebsocketFailureTest

This small project is made to highlight a possible bugg in the Flask-SocketIO
Alternatively it will show where I'm doing it wrong...

## Error description

This project will load the page, and setup a socket to the Flask server, upon connection (`socket.on('connect'...`) an *Initial request* will be sent. For me, this request always works. However when I later send another request this will not always work (it's hard to give a precise number on how often this happens, but when following my rutien it will beat least 1/20 but often 1/5).
I'm not sure exactly what happens, however I know that no data is sent from the client to the server. In the client logs, I do see that a flush of the data seem to be missing (as discussed in [this SO question](http://stackoverflow.com/questions/36037064/socket-io-client-doesnt-flush)). But as the question descibes it's possible to see even before the send if it will succeed or not.

## Instructions

clone the repo, install the virtual environment, and start the server
```
git clone https://github.com/tb2johm/FlaskWebsocketFailureTest.git
cd FlaskWebsocketFailureTest
./install_virtual_environemnt
./venv/bin/python3 run.py
```

Now the simple webpage should be available at [localhost:3030](http://localhost:3030)

If the socket work you should see the text: *Hello World* and in an input box the text: `init ok`
There will also be a button *Send second request*. When pressing the button a request will (most of the times) be sent to the server, which will respond. Upon receive in the browser, the input box will show the text `second request ok!`

In the browser console activate the SocketIO log with the command `localStorage.debug = '*';`

Now it's just a matter of refreshing the page until the log looks like this:
```
engine.io-client:socket probe transport "websocket" opened +506ms socket.io-1.4.5.js:2:5354
engine.io-client:polling polling got data [object ArrayBuffer] +74ms socket.io-1.4.5.js:2:5354
engine.io-client:socket socket receive: type "noop", data "undefined" +6ms socket.io-1.4.5.js:2:5354
engine.io-client:polling polling +2ms socket.io-1.4.5.js:2:5354
engine.io-client:polling-xhr xhr poll +3ms socket.io-1.4.5.js:2:5354
engine.io-client:polling-xhr "xhr open GET: http://localhost:3030/socket.io/?EIO=3&transport=polling&t=LF7SkW4&sid=b5c0cae2bb11439e8af4d1eba4fafd98" +6ms socket.io-1.4.5.js:2:5354
engine.io-client:polling-xhr xhr data null +15ms socket.io-1.4.5.js:2:5354
engine.io-client:socket probe transport "websocket" pong +11ms socket.io-1.4.5.js:2:5354
```

(what we are looking for is that the row `..."websocket" opened...` is NOT followed by the row `..."Websocket" pong...`

Now the error has been reproduced, and if pressing the button that request will never reach the server. (After 60 seconds the socket will reset, and now it might work to press the button again)
