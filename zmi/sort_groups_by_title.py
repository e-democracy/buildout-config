## Script (Python) "sort_groups_by_title"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=groups
##title=Sort Groups by Title
##
def alpha_sort(a, b):
    alpha = a.title_or_id().lower()
    beta = b.title_or_id().lower()
    if alpha < beta:
        retval = -1
    elif alpha == beta:
        retval = 0
    else:
        retval = 1
    return retval
    
retval = groups
retval.sort(alpha_sort)
return retval
