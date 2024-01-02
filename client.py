html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebSocket Chat</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #d0d0f0;
            margin: 0;
            padding: 20px;
        }
        
        h1 {
            color: #33a;
        }
        
        form {
            display: flex;
            margin-top: 20px;
        }
        
        input {
            flex: 3;
            padding: 10px;
            font-size: 16px;
        }
        
        button {
            padding: 10px 15px;
            font-size: 16px;
            background-color: #4c4ff0;
            color: white;
            border: ridge;
            cursor: pointer;
            flex: 1;
        }
        
        ul {
            list-style-type: none;
            padding: 0;
        }
        
        li {
            background-color: #fff;
            padding: 10px;
            margin-top: 10px;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <h1>WebSocket Chat</h1>
    <form action="" onsubmit="sendMessage(event)">
        <input type="text" id="messageText" autocomplete="off" placeholder="Type your message here"/>
        <button>Send</button>
    </form>
    <ul id='messages'></ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/chat");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
</body>
</html>
"""