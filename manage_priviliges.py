import manage_requests
import requests
import manage_xml
import _environment

users_for_roles = {"content editor":["user1","pswrd1"], "content creator":["user2","pswrd2"]}

expected_user_roles = {"content editor":['Workspace;Searches;Create/Modify','Workspace;Searches;Share/Unshare',"test1:test2:test3"],
                       "content creator":['Workspace;Searches;Create/Modify', 'Workspace;Searches;Share/Unshare',"test4:test5:test6"]}

def get_application_priviliges_for_role(env, role):
    #print(users_for_roles[role][0])
    #print(users_for_roles[role][1])

    request_specification = f"/rest/service/admin/users/?op=applicableapplicationprivileges"
    request = manage_requests.prepare_get_request(env, request_specification, users_for_roles[role][0], users_for_roles[role][1])
    get_response = requests.get(request)

    priviliges_list = manage_xml.extract_xml_elements_by_path(get_response.content, './/privilegeHierarchy')
    priviliges_text_list = list(map(lambda x: x.text, priviliges_list))
    return priviliges_text_list

def get_missing_priviliges(env):

    missing_priviliges_list = {}

    for item in expected_user_roles:
        if len(get_priviliges_missing_from_list(expected_user_roles[item], get_application_priviliges_for_role(env, item)))!= 0:
            missing_priviliges_list[item] = get_priviliges_missing_from_list(expected_user_roles[item], get_application_priviliges_for_role(env, item))
    return missing_priviliges_list


def get_priviliges_missing_from_list(priviliges, priviliges_list):

    missing_priviliges = [value for value in priviliges if value not in priviliges_list]
    return missing_priviliges

#print(get_missing_priviliges(_environment.uat))