import base64

# app.enc read karo
encrypted = open('app.enc', 'r').read()

# Memory mein decode karo
decoded = base64.b64decode(encrypted).decode('utf-8')

# Direct execute karo
exec(decoded)
