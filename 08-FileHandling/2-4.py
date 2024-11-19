###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(position_file,'w') as f2:
   with open(employees_file,'r') as f1:
      for line in f1:
         if job_title in line:
            f2.write(line)