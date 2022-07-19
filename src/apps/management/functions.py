def passEncr(action, text):
    from django.core import signing
    if action == "encrypt":
        return signing.dumps(text)
    
    if action == "decrypt":
        return signing.loads(text)
