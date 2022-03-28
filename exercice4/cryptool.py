#|-----------------------|
#   EXTERNAL IMPORTS     |
#|-----------------------/

from bcrypt import hashpw, checkpw, gensalt
from hashlib import _Hash, md5

##########################################################
# EXTERNAL IMPORTS                                       #
##########################################################


#|-------------------------------------------------------|
#   Methods                                              |
#|-------------------------------------------------------/

class Cryptographe:
    
    def __init__(self, secure, rounds=12, prefix=b'2b') -> None:
        self.secure = secure
        self.rounds = rounds
        self.prefix = prefix
        self.salt = gensalt(
            rounds=self.rounds, 
            prefix=self.prefix
            )
        
        
    def encrypt_bcrypt(self, pwd) -> bytes:
        """_summary_
        
        H(p)
        Encrypt password by returning the hash of it 
        using the bcrypt.haspw() and bcrypt.gensalt()
        functions.

        Args:
            pwd (_type_ == str): _description_
            password to hash.

        Returns:
            bytes: _description_
            the hashed password.
        
        """
        return hashpw(
            f"{pwd}".encode(),
            self.salt
        )


    def encrypt_hashlib(self, pwd, secure=False) -> _Hash:
        """_summary_
        
        H(p)
        Encrypt password by returning the hash of it 
        using the hashlib.md5() function.
        
        Args:
            pwd (_type_ == str): _description_
            password to hash.

        Returns:
            _Hash: _description_
            the hashed password.
            
        """
        return md5(pwd, usedforsecurity=secure)


    def check(pwd, hash) -> bool:
        """_summary_
        
        H(p)
        Encrypt password by returning the hash of it 
        using the hashlib.md5() function.
        
        Args:
            pwd (_type_ == str): _description_
            password.
            hash (_type_ == bytes): _description_
            the hash that should corresponds to the
            password.

        Returns:
            bool: _description_
            the hashed password.
            
        """
        return checkpw(pwd, hash)

