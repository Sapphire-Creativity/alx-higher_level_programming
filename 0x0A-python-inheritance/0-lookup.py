#!/usr/bin/python3

def lookup(obj):
    attributes_and_methods = []
    
    for attribute_name in dir(obj):
        
        if callable(getattr(obj, attribute_name)):
            attributes_and_methods.append(f"{attribute_name}()")
        
        else:
            attributes_and_methods.append(attribute_name)
            
    return attributes_and_methods
