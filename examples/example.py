# import ratemyprofessor
# import csv
# import re
# reviews=[]

# # with open("users_rows.csv") as prof_rows:
# #     reader = csv.DictReader(prof_rows)
# #     for row in reader:
# #         professor = ratemyprofessor.get_professor_by_school_and_name(
# #             ratemyprofessor.get_school_by_name("San Jose State University"), row["name"])
# #         if professor is not None:
# #             # reviews.append([1,row["id"],])
# #             print("%s works in the %s Department of %s." % (professor.name, professor.department, professor.school.name))
# #             print("Rating: %s / 5" % professor.rating)
# #             print("Difficulty: %s / 5" % professor.difficulty)
# #             print("Total Ratings: %s" % professor.num_ratings)
# #             ratings = professor.get_ratings()
# #             for rating in ratings:
# #                 print(f"Date: {rating.date}, Rating: {rating.rating}, Comment: {rating.comment}")
# #             if professor.would_take_again is not None:
# #                 print(("Would Take Again: %s" % round(professor.would_take_again, 1)) + '%')
# #             else:
# #                 print("Would Take Again: N/A")

# # def save_to_csv(filename, data):
# #     with open(filename, 'w', encoding="utf-8", newline='') as file:
# #         writer = csv.writer(file)
# #         writer.writerow(["user_id","professor_id","course_number","department","content","quality","difficulty","grade","tags","take_again","is_user_anonymous"])
# #         writer.writerows(data)

# # save_to_csv('reviews.csv',reviews)

# professor = ratemyprofessor.get_professor_by_school_and_name(ratemyprofessor.get_school_by_name("San Jose State University"), "David Taylor")
# if professor is not None:
    
#     # reviews.append([1,row["id"],])
#     # print("%s works in the %s Department of %s." % (professor.name, professor.department, professor.school.name))
#     # print("Course: %s" % professor.department)
#     # print("Rating: %s / 5" % professor.rating)
#     # print("Difficulty: %s / 5" % professor.difficulty)
#     # print("Total Ratings: %s" % professor.num_ratings)
    
#             # ratings.append(Rating(rating=rating["helpfulRating"], difficulty=rating["difficultyRating"],
#             #                       comment=rating["comment"], class_name=rating["class"], date=date,
#             #                       take_again=take_again, grade=rating["grade"], thumbs_up=rating["thumbsUpTotal"],
#             #                       thumbs_down=rating["thumbsDownTotal"], online_class=online_class, credit=credit,
#             #                       attendance_mandatory=attendance_mandatory))

#     ratings = professor.get_ratings()
#     for rating in ratings:
#         print(dir(rating))
#     # print(ratings)
#     # for rating in ratings:
#     #     class_name = rating.class_name
#     #     match = re.match(r"([A-Za-z]+)(\d+.*)", class_name)
#     #     department,course_number = None,None
#     #     if match:
#     #         department = match.group(1)
#     #         course_number = match.group(2)
#     #     else:
#     #         department=class_name
#     #         course_number = "-1"
#     #     print(rating.date, end=" ")
#     #     for tag in rating.tags:
#     #         print(tag, end =" ")
#     #     print()
#         #everything here except tags 
#         # "class name for tags = {Tag-bs9vf4-0 hHOVKF}"    
        

#         # print(department+ " " + course_number)
        
#         #print(f"Date: {rating.date}, Rating: {rating.rating}, Content: {rating.comment}, Diffifculty:{rating.difficulty}, Grade: {rating.grade}, Take Again: {rating.take_again},  ")
#     # if professor.would_take_again is not None:
#     #     print(("Would Take Again: %s" % round(professor.would_take_again, 1)) + '%')
#     # else:
#     #     print("Would Take Again: N/A")
