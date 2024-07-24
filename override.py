class bank:
    def interest(self):
        return 10;
class global_ime(bank):
    def interest(self):
        return 13;
class nabil(bank):
    def interest(self):
        return 14;
class nic_asia(bank):
    def interest(self):
        return 12;
obj1 = bank()
obj2 = global_ime()
obj4 = nabil()
obj3 = nic_asia()
print("Bank Interest: " ,obj1.interest());
print("Global Interest: ",obj2.interest());
print("NIC Asia Interest:",obj3.interest());
    
