## Script (Python) "sort_category_keys"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=keys
##title=Sort Group Category Keys
##
def alpha_sort(a, b):
    alpha = a.lower()
    beta = b.lower()
    if alpha < beta:
        retval = -1
    elif alpha == beta:
        retval = 0
    else:
        retval = 1
    return retval
    
retval = keys
retval.sort(alpha_sort)
return retval
