#|----------------------------------------------------------------------------|
#   INTERNAL IMPORTS     |
#|-----------------------/

from cryptool import Cryptographe

###############################################################################
# CLASS                                                                       #
###############################################################################

class Client:
    """_summary_
    Client class that contains the logic behind the pattern
    client-server. A client has a name, a password and a 
    'secret' which is shared with the server.
    It is voluntarily simple, as it should show the process
    behind a challenge-response authentication protocol using
    the CHAP protocol.
    
    _methods: 
        - client_response(self, password, nonce) -> str
    """

    #|------------------------------------------------------------------------|
    #   Constructor          |
    #|-----------------------/

    def __init__(self, name, password) -> None:
        self.name = name
        self.secret = 'secret'
        self.password = password
            
    def __str__(self) -> str:
        return  "\n" + \
            "| Name : " + self.name + \
            "| Secret : " + self.secret + \
            "| Password : " + self.password
    
    #|------------------------------------------------------------------------|
    #   Methods              |
    #|-----------------------/

    def response(self, password, nonce) -> str:
        """_summary_
        The function takes in a password and a nonce and 
        returns a hash of the password and nonce
        
        :param password: The password that the client has
        entered.
        
        :param nonce: A random string of characters that 
        is used to make sure that the client and server
        have the same session key.
        
        :return: The client response is being returned.
        """
        hash = Cryptographe.encrypt_hashlib(str(password + nonce).encode())
        return hash.hexdigest()
