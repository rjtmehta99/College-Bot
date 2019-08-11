# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 19:47:54 2019

@author: Rajat Mehta
"""

print('Please enter the course you\'re interested/enrolled in: \n')

course_type = input('Choose course type: \n1. Undergraduate\n2. Postgraduate\n3. P.hD.\n4. Certificate Courses\n')

if course_type == 1:
    response_stage_1 = input('Choose from these courses: \n1. B. Tech.\n2. B. Arch.\n3. B. Sc.\n4. B.A. (Hons)\n5. B.A.P.E.D\n6. B.B.A.\n7. B. Comm.\n8. B. Comm. (Hons) - Accounting\n9. B.C.A.\n10. B.H.M.\n11. L.L.B.\n12. B.A. L.L.B. Integrated\n13. B.B.A. L.L.B Integrated\n14. B. Des.\n')

    if response_stage_1 == 1:
        response_stage_2 = input('Choose B. Tech. Stream: \n1. Automobile Engineering\n2. Chemical Engineering\n3. Civil Engineering\n4. Computer Science and Engineering\n5. Computer and Communication Engineering\n6. Electrical and Electronics Engineering\n7. Electronics and Communication Engineering\n8. Information Technology\n9. Mechanical Engineering\n10. Mechatronics Engineering\n')

        if response_stage_2 == 1:
            course_code = 'btech_auto'
        elif response_stage_2 == 2:
            course_code = 'btech_chem'
        elif response_stage_2 == 3:
            course_code = 'btech_civ'
        elif response_stage_2 == 4:
            course_code = 'btech_cse'
        elif response_stage_2 == 5:
            course_code = 'btech_cce'
        elif response_stage_2 == 6:
            course_code = 'btech_eee'
        elif response_stage_2 == 7:
            course_code = 'btech_ece'
        elif response_stage_2 == 8:
            course_code = 'btech_it'
        elif response_stage_2 == 9:
            course_code = 'btech_mech'
        elif response_stage_2 == 10:
            course_code = 'btech_mecht'

elif course_type == 2:
    response_stage_1 = input('Choose from these courses: \n1. M. Tech.\n2. M. Arch.\n3. M. Comm.\n4. M.C.A.\n5. M.A. in Journalism\n6. L.L.M.\n7. M.B.A.')

    if response_stage_1 == 1:
        response_stage_2 = input('Choose M. Tech. Stream: \n1. Communication Systems\n2. Computer Aided Analysis and Design\n3. Computer Science and Engineering\n4. Data Science\n5. Environmental Engineering\n6. Information Security\n7. Manufacturing Engineering and Technology\n8. Power Electronics and Drives\n9. Structural Engineering\n10. VLSI and Embedded System Design\n')

        if response_stage_2 == 1:
            course_code = 'mtech_auto'
        elif response_stage_2 == 2:
            course_code = 'mtech_chem'
        elif response_stage_2 == 3:
            course_code = 'mtech_civ'
        elif response_stage_2 == 4:
            course_code = 'mtech_cse'
        elif response_stage_2 == 5:
            course_code = 'mtech_cce'
        elif response_stage_2 == 6:
            course_code = 'mtech_eee'
        elif response_stage_2 == 7:
            course_code = 'mtech_ece'
        elif response_stage_2 == 8:
            course_code = 'mtech_it'
        elif response_stage_2 == 9:
            course_code = 'mtech_mech'
        elif response_stage_2 == 10:
            course_code = 'mtech_mecht'























elif course_type == 3:
    ##TODO Add PhDs
elif course_type == 4:
    #Add Certificate courses














interested_in = input()
print('To chat with the bot, enter your query below. Send \'stop\', \'abort\' or \'quit\' to end chat')
while True:
    response = input()
    if response == 'stop' or response == 'abort' or response == 'quit':
        break