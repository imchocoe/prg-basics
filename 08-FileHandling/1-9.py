###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'
i=1
with open('it_company.csv','r') as file:
   for line in file:
      if job_title in line:
         print(i,'.',line, end="")
         i+=1