from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_send_message(data):
    message = data['message']
    emit('receive_message', {'message': message, 'sender': 'user'}, broadcast=True)
    
    # Automated response logic
    if "hi" in message.lower():
        response = "Hello! How can I assist you today?"
    elif "bye" in message.lower():
        response = "Goodbye! Have a great day!"
    else:
        response = "Thanks for your message!"

    # Send the automated response back to all clients
    emit('receive_message', {'message': response, 'sender': 'bot'}, broadcast=True)

if __name__ == '__main__':
    # Use 0.0.0.0 to make the server externally visible
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)
