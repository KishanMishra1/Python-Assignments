#lex_auth_012693816757551104165

'''Care hospital wants to know the medical speciality visited by t
he maximum number of patients.
Assume that the patient id of the patient along with the medical
speciality visited by the patient is stored in a list.
The details of the medical specialities are stored in a dictionary as follows:
{
"P":"Pediatrics",
"O":"Orthopedics",
"E":"ENT
}

Write a function to find the medical speciality visited by the
maximum number of patients and return the name of the speciality.'''

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    countp=counto=counte=0
    for i in patient_medical_speciality_list:
        if i=='P':
            countp+=1

        elif i=='O':
            counto+=1
        elif i=="E":
            counte+=1
        else:
            pass
    if counto<countp>counte:
        return medical_speciality['P']
    elif countp<counto>counte:
        return medical_speciality['O']
    elif countp<counte>counto:
        return medical_speciality['E']
 



#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
