# -*- coding: utf-8 -*-

class FakeRes:
    
    def __init__(self, number):
        self._name = "r{number}".format(number=number+1)
        self._owner = None
        
    def name(self):
        return self._name
    
    def owner(self):
        return self._owner
    
    def reset(self):
        self._owner = None
        
    def set_owner(self, owner):
        self._owner = owner
        
    def has_owner(self):
        return self._owner is not None
    
class FakeDataBase:
    
    def __init__(self, number_of_res):
        self.rescale(number_of_res)
       
    def rescale(self, number_of_res):
        self._res = [FakeRes(number) for number in range(number_of_res)] 
       
    def get_allocated(self):
        return {res.name() : res.owner() for res in self._res if res.has_owner()}

    def get_deallocated(self):
        return [res.name() for res in self._res if not res.has_owner()]
    
    def get_allocated_by_user(self, owner):
        return [res.name() for res in self._res if res.owner() == owner]
    
    def reset(self):
        for res in self._res:
            res.reset()
            
    def allocate(self, owner):
        for res in self._res:
            if not res.has_owner():
                res.set_owner(owner)
                return res.name()
        return None
    
    def deallocate(self, res_name):
        for res in self._res:
            if res.name() == res_name:
                if res.has_owner():
                    res.reset()
                    return True
                else:
                    break
        return False
    