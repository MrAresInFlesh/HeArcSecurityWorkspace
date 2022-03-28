"""

Simple example mutual authentication sequence:

- Server sends a unique challenge value sc to the client
- Client sends a unique challenge value cc to the server
- Server computes sr = hash(cc + secret) and sends to the client
- Client computes cr = hash(sc + secret) and sends to the server
- Server calculates the expected value of cr and ensures the client responded correctly
- Client calculates the expected value of sr and ensures the server responded correctly


"""

# Use of bcrypt: https://zetcode.com/python/bcrypt/
# to encrypt and hash data.

def cc():
    pass

def cr():
    pass

def sr():
    pass

if __name__=="__main__":
    
    print("Exercice 4 - Challenge response")
