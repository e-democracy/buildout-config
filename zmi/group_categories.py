## Script (Python) "group_categories"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=groups=None
##title=Get the Categories and Groups
##
# Get all group-categories in a site

if groups == None:
    groupsObj = context.Scripts.get.groups_object()
    groups = filter(lambda x: getattr(x, 'is_group', 0),
                context.Scripts.get.object_values(groupsObj, 'Folder'))
                
categories = {}

for group in groups:
    category = group.getProperty('category',  'Uncategorised')
    categories[category] = categories.get(category, []) + [group]

#assert categories
return categories
