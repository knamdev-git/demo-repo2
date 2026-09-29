# f = open('/home/anjali/GitHub/demo-repo2/hey.txt', 'w')

# # print(f.read())

# f.write("This file is being written by Python file handling feature")
# f.close()

with open('/home/anjali/GitHub/demo-repo2/hey.txt', 'r') as f : 
    # print(f.read())
    while True : 
        text = f.readline()
        print(text)
        if not text : 
            break

with open('/home/anjali/GitHub/demo-repo2/student_marks.txt', 'r') as student_file : 
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