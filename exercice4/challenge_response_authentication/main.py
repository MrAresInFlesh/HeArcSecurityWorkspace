#|------------------------------------------------------------------------------------|
#   EXTERNAL IMPORTS     |
#|-----------------------/

from colorama import Fore, Style

import pwinput
import sys

#|------------------------------------------------------------------------------------|
#   INTERNAL IMPORTS     |
#|-----------------------/

from client import Client
from cryptool import Cryptographe
from server import Server


#######################################################################################
# MAIN                                                                                #
#######################################################################################

SHOW_PROCESS = True

#|------------------------------------------------------------------------------------|
#|  Methods              |
#|-----------------------/

def display_infos(show_process):
    """
    Display some information to the user
    """
    print(f"|--------------------------------------------------")
    print(f"|\tExit: {Fore.RED} Press Ctrl+C {Style.RESET_ALL}")
    print(f"|\tShow process mode set to : " + \
        f"{Fore.LIGHTCYAN_EX} { show_process } {Style.RESET_ALL}")
    print(f"|\tSet debug mode to false?\n|\tPress 'y' " + \
          f"if you do not want to see the process, anything else to continue.")
    if input(f"|\t") == 'y':
        return False
    return True

def display_response(crypted_password, server_check):
    """
    The function takes in the crypted password and the server check 
    and displays the results.
    
    :param crypted_password: The password that the client has sent to the server
    :param server_check: a tuple of the form (server_check, result)
    """
    print(f"|--------------------------------------------------")
    
    print(f"|\tcrypt response pwd of the user using nonce of server :" + \
        f"\n|\t{Fore.LIGHTMAGENTA_EX} { crypted_password } {Style.RESET_ALL}")
    
    print(f"|\tserver check using the crypt pwd and the client pwd  :" + \
        f"\n|\t{Fore.LIGHTMAGENTA_EX} { server_check[0] } {Style.RESET_ALL}")
    
    print(f"|\tresult of the check_password function was            :" + \
        f"\n|\t{Fore.LIGHTYELLOW_EX} { server_check[1] } {Style.RESET_ALL}")

def check_exit():
    print(f"\n|Try again?" + \
        f"\n|\tpress 'n' for no, else anything to continue.")
    
    if(input("|\t") == 'n'):
        sys.exit()

#|------------------------------------------------------------------------------------|
#|  Program              |
#|-----------------------/

if __name__=="__main__":
    
    print(f"\n___________________________________________________")
    print(f"|Exercice 4 - Challenge response")

#|------------------------------------------------------------------------------------|
#####|  Initializing         |
#####|-----------------------/

    try:
        # Creating the server and activating it.
        print(f"|--------------------------------------------------")
        server = Server("ʕ•́ᴥ•̀ʔ")
        print(f"|\tServer name: [" + \
                f"{Fore.LIGHTBLUE_EX} { server.name } {Style.RESET_ALL}] is activated.")
        server.activate(True)

        # Creating the client
        client = Client(input("|\tEnter a name: "),
                    pwinput.pwinput(prompt="|\tPassword: ", mask='*')
                )
        print(f"|\tUser " +\
            f"{Fore.GREEN} { client.name } {Style.RESET_ALL} successfully created.")

    except Exception:
        print("|\tSomething went wrong.")


#|------------------------------------------------------------------------------------|
#####|Challenge Handshake Authentication |
#####|-----------------------------------/
    
    try:
        while server.activated:
            
            # Showing some useful infos to the user.
            SHOW_PROCESS = display_infos(SHOW_PROCESS)

            # Registering the client to the list of clients of the server
            print(f"|--------------------------------------------------")
            print(f"|\tRegistering client " +\
                f"{Fore.GREEN} { client.name } {Style.RESET_ALL} to the server.")
            server.register_client(client)
            print(f"|\tServer name: { server.name } " + \
                f"| status: {Fore.GREEN} { server.activated } {Style.RESET_ALL}")

            while server.activated:
                
                print(f"|\t{Fore.GREEN} { client.name } {Style.RESET_ALL}, " + \
                    f"you can now try to connect to the server:")
                
                if SHOW_PROCESS:
                    print(f"|")
                    print(f"|\tSending challenge to { client.name }:")
                
                password = pwinput.pwinput(prompt="|\tEnter password to connect: ", mask='*')
                
                if SHOW_PROCESS:
                    print(f"|")
                    print(f"|\tentered password was    : " + \
                        f"{Fore.CYAN} { password } {Style.RESET_ALL}")
                    print(f"|\ttreatment of the answer ...")
                
                server.nonce = server.cipher.createNonce(server.secret)
                
                crypted_password = client.response(password, server.nonce)
                
                if SHOW_PROCESS:
                    print(f"|")
                    print(f"|\tserver nonce sent was   :\n|\t" + \
                          f"{Fore.YELLOW} { server.nonce } {Style.RESET_ALL}")
                    print(f"|\tcrypted response was    :\n|\t" + \
                          f"{Fore.LIGHTMAGENTA_EX} { crypted_password } {Style.RESET_ALL}")
                    print(f"|")
                    print(f"|\t{Fore.CYAN}checking if answer is correct.{Style.RESET_ALL}")

                server_check = server.check_client_password(client, crypted_password)

                if server_check[1]:
                    
                    if SHOW_PROCESS:
                        display_response(crypted_password, server_check)

                    print(f"|\t{ Fore.GREEN } Correct { Style.RESET_ALL } password." + \
                          f"\n|\tYou can now access your workspace.")
                    
                    server.activate(True)
                                        
                    check_exit()
     
                else:
                    
                    if SHOW_PROCESS:
                        display_response(crypted_password, server_check)

                    print(f"|--------------------------------------------------")
                    print(f"|\t{Fore.RED}Wrong{Style.RESET_ALL} password. Try again?")
                    check_exit()


    except KeyboardInterrupt:
        pass
    
    

