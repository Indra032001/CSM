#CMS
class client:
    def __init__(self,idt,cn,cm,fn,tos,mb):
        self.client_id=idt
        self.client_name=cn
        self.client_mobile=cm
        self.firm_name=fn
        self.type_of_service=tos
        self.monthly_budget=mb

    def __str__(self):
        return f'\nClient ID:\t\t{self.client_id},\nClient Name:\t\t{self.client_name},\nClient Mobile.No:\t{self.client_mobile},\nCliernt Firm Name:\t{self.firm_name},\nClient Service Type:\t{self.type_of_service},\nClient Monthly Budget:\t{self.monthly_budget}'

Client_list = []

def find_client(client_id):
        client_found = False
        for client in Client_list:
            if client_id == client.client_id:
                client_found = client
        return client_found

def obj():
    for objs in Client_list:
        print(objs)
   
while True:
    ch = int(input('\n Enter Choice:\n1.ADD CLIENT\n2.SHOW ALL CLIENT\n3.UPDATE A CLIENT\n4.DELETE A CLIENT\n5.EXIT\n'))
    match ch:
        case 1:
                 No = int(input('Enter Number Of Client To Code:'))
                 for i in range(No):
                     print('ADD CLIENT')
                     print('\tSTATIC\t\tDATA\n')
                     idt = (input('Enter Client ID:\t'))
                     if len(idt)==0:
                         print('....Enter Proper ID....')
                         break
                     cn = input('Enter Client Name:\t')
                     cm = int(input('Enter Client Mobile.No:\t'))
                     fn = input('Enter Client Firm Name:\t')
                     tos = input('Enter Type of Service:\t')
                     mb = float(input('Enter Monthly Budget:\t'))
                    
                     client_duplicate=find_client(idt)
                     if client_duplicate:
                         print()
                         print('Client Already Exists')
                         Client_list.remove(client_duplicate)
                         break
                     else:
                         c1 = client(idt,cn,cm,fn,tos,mb)
                         Client_list.append(c1)
                         print('....CLIENT ADDED SUCSESSFULLY....')
                                           
        case 2:
                 print('SHOW ALL CLIENTS')
                 srno = 1
                 for clients in Client_list:
                     print('SRNO:',srno,'/',len(Client_list))
                     print(clients)
                     srno += 1
                 
        case 3:
                 print('UPDATE A CLIENT')
                 i = (input('Enter Client ID For UPDATE:\t'))
                 client_found = find_client(i)
                 if client_found:
                     while True:
                         ch=int(input('\nEnter Choice\n1:UPDATE BUDGET\n2:UPDATE NAME\n3:UPDATE MOBILE\n4:UPADTE FIRM_NAME\n5:UPADTE TYPE_OF_SERVICE\n6:EXIT THE LOOP'))
                         match ch:
                             case 1:
                                 mb = int(input('ENTER UPDATE BUDGET:'))
                             case 2:
                                 cn = input('ENTER UPDATE NAME:')     
                             case 3:
                                 cm = input('ENTER UPDATE MOBILE:')                                
                             case 4:
                                 fn = input('ENTER UPADTE FIRM_NAME:')                                 
                             case 5:
                                 tos = input('ENTER UPADTE TYPE_OF_SERVICE:')                                 
                             case 6:
                                 print('ÍNVALID CHOICE')
                                 break
                                 
                                
                     client_found.monthly_budget = mb           
                     client_found.client_name = cn
                     client_found.client_mobile = cm
                     client_found.firm_name = fn
                     client_found.type_of_service = tos
                     print('CLIENT UPDATED')
                 else:
                     print('No such client found')
                 
        case 4:
                 print('DELETE A CLIENT')
                 i=(input('Enter Client ID For DELETE:\t'))
                 client_found = find_client(i)
                 if client_found:
                     while True:
                         ch=int(input('\nEnter Choice:\n1.DELETE ID\n2.DELETE NAME\n3.DELETE MOBILE\n4.DELETE FIRM NAME\n5.DELETE TYPE OF SERVICE\n6.DELETE MONTHLY BUDGET\n7.DELETE WHOLE CLIENT\n'))
                         obj_no=int(input('Enter Number of Object to be operated:\t'))
                         ob=obj_no-1
                         match ch:
                             case 1:
                                 del(Client_list[ob].client_id)
                                 break
                             case 2:
                                 del(Client_list[ob].client_name)
                                 break
                             case 3:
                                 del(Client_list[ob].client_mobile)
                                 break
                             case 4:
                                 del(Client_list[ob].firm_name)
                                 break
                             case 5:
                                 del(Client_list[ob].type_of_service)
                                 break
                             case 6:
                                 del(Client_list[ob].monthly_budget)
                                 break
                             case 7:
                                 Client_list.remove(client_found)
                                 print('CLIENT DELETED')
                                 break
                     
                 else:
                     print('NO such Client Found')
                     
                 
        case 5:
                 print('EXIT')
                 break
        case _:
            print('INVALID CHOICE')
                 
