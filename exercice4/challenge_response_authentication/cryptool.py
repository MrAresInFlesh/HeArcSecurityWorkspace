#|-----------------------|
#   EXTERNAL IMPORTS     |
#|-----------------------/

from hashlib import md5, sha1
from secrets import token_hex
import datetime
import hmac

#######################################################################################
# CLASS                                                                               #
#######################################################################################

class Cipher:
    """_summary_
    The Cipher class is an utilitary class that 
    regroups cryptographic functions.
    """
    
    def __init__(self) -> None:
        self.nonces = list()

    #|--------------------------------------------------------------------------------|
    #   Methods              |
    #|-----------------------/

    def createNonce(self, username):
        """_summary_
        Create a random number, and then use HMAC to hash 
        it along with a timestamp and the username.
        
        Secret is generated using 'secrets' module, as this
        link show why.
        https://stackoverflow.com/questions/20936993/how-can-i-create-a-random-number-that-is-cryptographically-secure-in-python
        
        :param username: The username of the user
        :return: a string that is a hexadecimal digest of 
        the HMAC hash of the username and the current
        time.
        """
        
        # compute k using the time and the username.
        k = str(datetime.datetime.utcnow()) + username
        
        # compute s using.
        s = token_hex(32)
        
        # Computing the nonce as a string.
        nonce = hmac.new(k.encode('ascii'), 
                        s.encode('ascii'), 
                        sha1)\
                        .hexdigest()

        self.nonces.append(nonce)
        
        # Checking if the nonce is already in the list. 
        # If it is, it will generate a new one.
        for nnc in self.nonces:
            if self.nonces.count(nnc) > 1:
                while self.nonces.count(nnc) > 1:
                    nnc = hmac.new(k.encode('ascii'), 
                        (s + token_hex(32)).encode('ascii'),
                        sha1) \
                        .hexdigest()
                return nnc
        return nonce

    @staticmethod
    def encrypt_hashlib(pwd):
        """_summary_
        It takes a password as input and returns a hash 
        of the password.
        
        :param pwd: The password to be hashed
        
        :param secure: If True, the password is not 
        stored in memory.
        
        If False, the password is stored in
        memory, defaults to False (optional)
        
        :return: The return value is a string containing
        the hexadecimal representation of the binary data.
        """
        return md5(str(pwd).encode())


