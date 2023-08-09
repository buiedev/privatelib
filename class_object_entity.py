# TITLE: ENTITY OBJECT CLASS
# DESC:  A python script file that is composed of object classes that can be imported 
#        to quickly use prebuilt entity properties and structures, such as 'companies' 
#        or 'customers, eith subclasses that can add percise detail to the objects.

class Entity:
  def __init__(self, id, address, commdetails, contacts, class):
    Entity.self = self
    Entity.id = identity 
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
