#|----------------------------------------------------------------------------|
#   INTERNAL IMPORTS     |
#|-----------------------/

from cryptool import Cryptographe
from client import Client

###############################################################################
# CLASS                                                                       #
###############################################################################

class Server:
    """_summary_
    Server class that contains the logic behind the pattern
    client-server. A Server has a name, a 'secret' which 
    is shared with the client. It has also nonce, which is
    changed every time a challenge is send to the client.
    It is voluntarily simple, as it should show the process
    behind a challenge-response authentication protocol.
    
    _methods:
        - activate(self, trigger: bool) -> None
        - check_password(self, client: Client, password) -> bool
        - register_client(self, client: Client) -> None
    """

    #|------------------------------------------------------------------------|
    #   Constructor          |
    #|-----------------------/

    def __init__(self, name) -> None:
        self.name = name
        self.secret = 'secret'
        self.cipher = Cryptographe()
        self.nonce = self.cipher.createNonce(self.secret)
        self.activated = False
        self.clients = list()
        
    def __str__(self) -> str:
        return "\n" + \
            "| Name : " + self.name + \
            "| Secret : " + self.secret + \
            "| Nonce : " + self.nonce + \
            "| Activate : " + self.activated + \
            "| Clients : " + len(self.clients)

    #|------------------------------------------------------------------------|
    #   Methods              |
    #|-----------------------/

    def activate(self, trigger: bool) -> None:
        """
        It computes the expected value of the server.
        This is just to do the go and out when using
        the loop in the main program.
        :param trigger: bool
        :type trigger: bool
        """
        self.activated = trigger
        
    def check_client_password(self, client: Client, password) -> bool:
        """
        Given a client, check if the client's password 
        matches the password associated with the client's
        name
        
        :param client: The client object that we want 
        to check the password for.
        :type client: Client
        :return: Nothing
        """
        hash = Cryptographe\
            .encrypt_hashlib(str(\
                (client.password + self.nonce))\
                .encode()
            )
            
        return (hash.hexdigest(), hash.hexdigest() == password)
    
    def register_client(self, client: Client) -> None:
        """
        Add a new client to the list of clients.
        
        :param client: The client object who is 
        registering.
        :type client: Client
        """
        hash = Cryptographe\
            .encrypt_hashlib(str(\
                (client.password + self.nonce))\
                .encode()
            )
            
        self.clients.append([client, hash.hexdigest(), self.secret])
