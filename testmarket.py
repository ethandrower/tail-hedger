from ib.ext.Contract import Contract
from ib.opt import ibConnection, message
from time import sleep
import requests

import pprint






#globals
contract_count = 0
countract_limit = 10






# print all messages from TWS
def watcher(msg):
    
    print msg
    #if msg is ContractDetails:
    #print("contract fond")

# show Bid and Ask quotes
def my_BidAsk(msg):
    if msg.field == 1:
        print ('%s:%s: bid: %s' % (contractTuple[0],
                       contractTuple[6], msg.price))
    elif msg.field == 2:
        print ('%s:%s: ask: %s' % (contractTuple[0], contractTuple[6], msg.price))

def makeStkContract(contractTuple):
    newContract = Contract()
    newContract.m_symbol = contractTuple[0]
    #newContract.m_localSymbol = contractTuple[0]
    newContract.m_secType = contractTuple[1]
    newContract.m_exchange = contractTuple[2]
    newContract.m_currency = contractTuple[3]
    newContract.m_expiry = contractTuple[4] 
  # newContract.m_strike = contractTuple[5]
  #  newContract.m_right = contractTuple[6] 
    newContract.m_multiplier = 100
    print ('Contract Values:%s,%s,%s,%s,%s,%s,%s:' % contractTuple)
    return newContract

  
  
  #  self.reqContractDetails(209, ContractSamples.EurGbpFx())
   # self.reqContractDetails(210, ContractSamples.OptionForQuery())
  #  self.reqContractDetails(211, ContractSamples.Bond())




def contractDetails(contract):
  #  print("contract details received" + str(contract) )
    #print(str(contract.MarketName))
    #print(dir(contract))
    #print(contract.values)
    #var = contract.values()

    global contract_count += 1
    if contract_count < contract_
    print(str(contract.contractDetails.m_summary.m_strike))


    contract_info = {'contract': contract.contractDetails.m_summary.m_strike,
            'price' : ##some price goes here.....

            }
    requests.post("http://localhost/contract", data=contract_info)
   # pp = pprint.PrettyPrinter(width=41)
    #pp.pprint(contract)
   # print(contract.m_summary)
    #print(str(contract.items))
    #print(contract.ContractMonth)
    #print(contract.marketName.get())
    ##d = contract.__dict__
    #print(str(d))
   # print(contract.summary)



if __name__ == '__main__':
    con = ibConnection()
    #con.registerAll(watcher)
    con.register(watcher, 'Error')
    con.register(contractDetails, 'ContractDetails')

    showBidAskOnly = False  # set False to see the raw messages
    if showBidAskOnly:
        con.unregister(watcher, message.tickSize, message.tickPrice,
                       message.tickString, message.tickOptionComputation)
        con.register(my_BidAsk, message.tickPrice)
    con.connect()
    sleep(1)
    tickId = 1

    # Note: Option quotes will give an error if they aren't shown in TWS
    contractTuple = ('TSLA', 'STK', 'SMART', 'USD', '', 0.0, '')
    contractTuple = ('XSP', 'OPT', 'CBOE', 'USD', '20170915' , 175, 'PUT' )
    #contractTuple = ('QQQQ', 'OPT', 'SMART', 'USD', '20070921', 47.0, 'CALL')
    #contractTuple = ('ES', 'FUT', 'GLOBEX', 'USD', '200709', 0.0, '')
    #contractTuple = ('ES', 'FOP', 'GLOBEX', 'USD', '20070920', 1460.0, 'CALL')
    #contractTuple = ('EUR', 'CASH', 'IDEALPRO', 'USD', '', 0.0, '')


    contract = Contract()
    contract.symbol = "FISV"
    contract.secType = "OPT"
    contract.exchange = "SMART"
    contract.currency = "USD"

    con.reqContractDetails(101, contract)

    stkContract = makeStkContract(contractTuple)
    con.reqContractDetails(101, stkContract)

    print ('* * * * REQUESTING MARKET DATA * * * *')
    #con.reqMktData(tickId, stkContract, '', False)
    sleep(15)
    print ('* * * * CANCELING MARKET DATA * * * *')
  #  con.cancelMktData(tickId)
    sleep(1)
    con.disconnect()
    sleep(1)
