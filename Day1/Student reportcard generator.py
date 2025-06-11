def generate_report(name,marks,subject="Python"):
    average=sum(marks)/len(marks)
    grade ="A" if average>=90 else "B" if average>=75 else "C"
    print(f"{name}'s {subject} Report\nMarks : {marks}\nAverage:{average}\nGrade: {grade}\n")
generate_report("Ayush",[85,92,78])