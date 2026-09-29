# f = open('/home/anjali/GitHub/demo-repo2/hey.txt', 'w')

# # print(f.read())

# f.write("This file is being written by Python file handling feature")
# f.close()
import json 

data = [
    {
        "userId": "usr_94f8a2bc",
        "username": "alex_dev99",
        "isActive": True,
        "profile": {
            "firstName": "Alex",
            "lastName": "Morgan",
            "email": "alex.morgan@example.com"
        },
        "roles": ["developer", "team-lead"],
        "projectsLogged": 2
    },
    {
        "userId": "usr_33b1c7da",
        "username": "sam_qa",
        "isActive": True,
        "profile": {
            "firstName": "Sam",
            "lastName": "Rivera",
            "email": "sam.rivera@example.com"
        },
        "roles": ["qa-engineer"],
        "projectsLogged": 5
    },
    {
        "userId": "usr_77e4f11b",
        "username": "clara_manager",
        "isActive": False,
        "profile": {
            "firstName": "Clara",
            "lastName": "Chen",
            "email": "clara.chen@example.com"
        },
        "roles": ["product-manager", "admin"],
        "projectsLogged": 0
    },
    {
        "userId": "usr_55d9b2ee",
        "username": "jordan_ops",
        "isActive": True,
        "profile": {
            "firstName": "Jordan",
            "lastName": "Smith",
            "email": "jordan.smith@example.com"
        },
        "roles": ["devops-engineer"],
        "projectsLogged": 3
    }
]


with open('/home/anjali/GitHub/demo-repo2/files/user_info.json', 'w') as json_file : 
    # data = json.load(json_file)
    json.dump(data, json_file, indent=4)
    print(data)

with open('/home/anjali/GitHub/demo-repo2/hey.txt', 'r') as f : 
    # print(f.read())
    while True : 
        text = f.readline()
        print(text)
        if not text : 
            break

with open('/home/anjali/GitHub/demo-repo2/files/student_marks.txt', 'r') as student_file : 
    i = 0
    while True : 
        i += 1
        all_marks = student_file.readline()
        
        if not all_marks : 
            print("File closed")
            break

        math_marks = all_marks.split(",")[0]
        english_marks = all_marks.split(",")[1]
        social_studies_marks = all_marks.split(",")[2]

        print(f'''Student {i} Marks Report : 
        Math : {math_marks}
        English :{english_marks}
        Social Studies :{social_studies_marks}''')