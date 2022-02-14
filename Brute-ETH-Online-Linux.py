
from eth_wallet import Wallet
from eth_wallet.utils import generate_entropy
from web3 import Web3, HTTPProvider
import multiprocessing
from multiprocessing import Pool

print("BY @XopMC for t.me/brythbit")
lang = int(input("Choose language for mnemonics words: 1 - English; 2 - Chinese Simplified; 3 - Chinese Traditional; 4 - French; 5 - Italian; 6 - Spanish; 7 - Japanese; 8 - Korean (input 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):  "))
n=int(input("How deep we going on Derivation path?/ На какую глубину опускаться по пути деривации?: "))
if lang == 1:
    LANGUAGE ="english"
    pass
elif lang == 2:
    LANGUAGE ="chinese_simplified"
    pass
elif lang == 3:
    LANGUAGE ="chinese_traditional"
    pass
elif lang == 4:
    LANGUAGE ="french"
    pass
elif lang == 5:
    LANGUAGE ="italian"
    pass
elif lang == 6:
    LANGUAGE ="spanish"
    pass
elif lang == 7:
    LANGUAGE ="japanese"
    pass
elif lang == 8:
    LANGUAGE ="korean"
    pass
else:
    print("ERROR!!! Please input correct number")
    quit()

#threadCount = input(' How many threads to run?:  ')
count = 0
found = 0

def ENT():
    global ENTROPY
    ENTROPY = generate_entropy(strength=128)

def ENT1():
    global ENTROPY
    ENTROPY = generate_entropy(strength=256)

def ETH(ind):
    
    def balance():
        w3 = Web3(Web3.HTTPProvider('http://173.212.227.224:8545'))
        get_balance = w3.eth.get_balance(address)
        return get_balance

    def transaction():
        w3 = Web3(Web3.HTTPProvider('http://173.212.227.224:8545'))
        get_transaction = w3.eth.get_transaction_count(address)
        return get_transaction



    PASSPHRASE = None
    #LANGUAGE ="english" # chinese_simplified, chinese_traditional, english
    global LANGUAGE
    wallet = Wallet()
    wallet.from_entropy(entropy=ENTROPY, passphrase=PASSPHRASE, language=LANGUAGE)
    wallet.from_index(44,harden=True)
    wallet.from_index(60, harden=True)
    wallet.from_index(0, harden=True)
    wallet.from_index(0)
    wallet.from_index(ind)
    address = wallet.address()
    priv = wallet.private_key()
    mnemonic = wallet.mnemonic()
    priv_imp = wallet.wallet_import_format()
    global count, found
    count+=1*int(thread)
    print("Address: ", address, "Transactions: ", transaction() , "Balance: ", balance(), "\n", "Mnemonic: " , mnemonic, "\n", "Derivation Path: m/44'/60'/0'/0/" + str(ind) +"\n"+ "PrivateKey: ", priv, "\n", "count: ", count, "  found: ", found)

    if transaction() != 0:
        found+=1
        file = open("found.txt", "a")
        file.write("Address: " + address + "\n" +
                "PrivKey: " + priv + "\n" +
                "PrivImp: " + priv_imp + "\n" +
                "Mnemonic: " + mnemonic + "\n" + "Derivation Path: m/44'/60'/0'/0/" + str(ind) + "\n"
                "==================================================" + "\n" + "\n")
        file.close()


def main():
    k=0
    while k<=n:
        ETH(k)
        k+=1



def seek():
    while True:
        ENT()
        main()
        ENT1()
        main()

if __name__ == '__main__':
    thread = int(input("How many core's to use?: "))
    for cpu in range(thread):
        multiprocessing.Process(target = seek).start()