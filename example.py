from ratemyprofessor import * 
import csv
import re
import time
reviews=[]

start = time.time()
with open("users_rows.csv") as prof_rows:
    reader = csv.DictReader(prof_rows)
    for row in reader:
        professor = get_professor_by_school_and_name(
            get_school_by_name("San Jose State University"), row["name"])
        if professor is not None and professor.school.name == "San Jose State University":
            ratings = professor.get_ratings()
            for rating in ratings:
                year = rating.date.year
                if year >= 2015:
                    class_name = rating.class_name
                    department,course_number = None,None
                    if "-" in class_name:
                        split = class_name.split("-")
                        department = split[0]
                        course_number = split[1]
                    else:
                        match = re.match(r"([A-Za-z]+)(\d+.*)", class_name)
                        if match:
                            department = match.group(1)
                            course_number = match.group(2)
                        else:
                            continue
                    reviews.append([1,row["email"].replace("@sjsu.edu", ""),rating.date,course_number,department,rating.comment,rating.rating,rating.difficulty,rating.grade,rating.rating_tags,rating.take_again,False])
                    #print(f"Date: {rating.date}, Rating: {rating.rating}, Content: {rating.comment}, Diffifculty:{rating.difficulty}, Grade: {rating.grade}, Take Again: {rating.take_again},  ")

def save_to_csv(filename, data):
    with open(filename, 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["user_id","professor_id","created_at","course_number","department","content","quality","difficulty","grade","tags","take_again","is_user_anonymous"])
        writer.writerows(data)

save_to_csv('reviews.csv',reviews)
end = time.time()
print("took " + str(end - start) + " seconds")