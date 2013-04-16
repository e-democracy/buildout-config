## Script (Python) "collate_groups"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=site, user
##title=
##
group_membership = user.getGroups() or []
group_membership_ids = map(lambda x: x.split('_member')[0], group_membership)

userAuthenticated = user.has_role('Authenticated')
userAnonymous = user.has_role('Anonymous')
groupsObj = context.Scripts.get.groups_object()
groups = filter(lambda x: getattr(x, 'is_group', 0),
                context.Scripts.get.object_values(groupsObj, 'Folder'))

userGroups = (not userAnonymous) and filter(lambda x: x.getId() in group_membership_ids, groups) or []
nonUserGroups = filter(lambda x: x.getId() not in userGroups, groups)
joinableGroups = []
otherGroups = []
for group_object in nonUserGroups:
    if group_object.getProperty('join_condition', 'anyone') == 'anyone':
        joinableGroups.append(group_object)
    else:
        otherGroups.append(group_object)
    
return groupsObj, groups, userGroups, nonUserGroups, joinableGroups, otherGroups
