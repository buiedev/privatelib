# TITLE: ENTITY OBJECT CLASS
# DESC:  A python script file that is composed of object classes that can be imported 
#        to quickly use prebuilt entity properties and structures, such as 'companies' 
#        or 'customers, eith subclasses that can add percise detail to the objects.

class Entity:
  def __init__(self, id, address, commdetails, contacts, class):
    Entity.self = self
    Entity.id = id
    Entity.address = address
    Entity.commdetails = commdetails
    Entity.contacts = contacts
    Entity.class = class

clasa Id(Entity):
    def __init__(self, name, uid, taxid, duns, locid):
        Id.self = self
        Id.name = name
        Id.uid = uid
        Id.taxid = taxis
  .     Id.duns = duns
        Id.locid = locid

class Addresss(Entity):
    def __init__(self, add1, add2, city, state, zipcode, countrycode);
         Address.self = self
         Address.add1 = add1
         Address.add2 = add2
         Address.city = city
         Address.state = state
         Address.ziocode = zipcode
         Address.countrycode = countrycode

class Commdetails(Entity):
     def __init__(self, maintel, mainemail, directcontact, timezone, website)
        Commdetails.self
        Commdetails.mailtel
        Commdetails.mainemail
        Commdetails.directcontact
        Commdetails.timezone
        Commdetails.website