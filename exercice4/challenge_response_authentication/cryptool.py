#|-----------------------|
#   EXTERNAL IMPORTS     |
#|-----------------------/

from hashlib import md5, sha1
from os import urandom
import datetime
import hmac
import secrets

#######################################################################################
# CLASS                                                                               #
#######################################################################################

class Cryptographe:
    """_summary_
    The Cryptographe class is an utilitary class that 
    regroups cryptographic functions.
    """    

#|------------------------------------------------------------------------------------|
#   Methods              |
#|-----------------------/

    @staticmethod
    def createNonce(username):
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
        k = str(datetime.datetime.utcnow()) * secrets.token_hex(16) + username
        
        # compute s using the time and the username.
        s = secrets.token_hex(32)
        
        # Computing the nonce as a string.
        return hmac.new(k.encode('ascii'), 
                        s.encode('ascii'), 
                        sha1)\
                        .hexdigest()

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


