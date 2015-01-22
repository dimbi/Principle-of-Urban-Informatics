import sys

db = {}
db_frequency = {}
db_agency = {}

names = ['Job ID','Agency','# Of Positions','Business Title','Civil Service Title','Salary Range From','Salary Range To','Salary Frequency','Work Location','Division /Work','Unit','Job Description','Minimum Qual Requirements','Preferred Skills','Additional Information','Posting Date']

def clear():
  # TODO Complete with your code and remove print below.
  print 'clear'    


# Inserts a job offer into the database.
def insert(fieldValues):
  # TODO Complete with your code and remove print below.
  #print 'insert ' + str(fieldValues)
  job_id      = fieldValues[0]
  job_details = fieldValues[1:]

  if job_id in db :
    pass
  else :
    frequency = fieldValues[7] #annual/monthly/weekly
    agency = fieldValues[1]
    frequency_id = -1
    if frequency in db_frequency :
      frequency_id = db_frequency[frequency]
    else :
      db_frequency[frequency] = len(db_frequency) #increment the value automatically
      frequency_id = db_frequency[frequency]
    
    db[job_id] = {}
    i = 1
    for detail in job_details :
      db[job_id][names[i]] = detail
      i += 1
    
print db

    #todo : split the job_details

# Updates all job offers that attend the field_name=old_value pair.
def update_all(params):
    query_field_name = params[0]
    query_field_value = params[1]
    update_field_name = params[2]
    update_field_value = params[3]

    # TODO Complete with your code and remove print below.
    print 'update_all set ' + update_field_name + '=' + update_field_value\
    + ' where ' + query_field_name + '=' + query_field_value

    # Prints number of updated rows in the database.
    updatedRowCount = 0
    print str(updatedRowCount)


# Deletes all job offers that attend the field_name=field_value pair.
def delete_all(params):
  field_name, field_value = params
  
  # TODO Complete with your code and remove print below.
  print 'delete_all where ' + field_name + '=' + field_value


# Prints all job offers that match the query field_name=field_value, one per
# line, semicolon-separated, with fields in the order defined in the assignment.
def find(params):
  field_name, field_value = params

  # TODO Complete with your code and remove print below.
  print 'find where ' + field_name + '=' + field_value


# Prints how many job offers match the query field_name=field_value.
def count(params):
  field_name, field_value = params

  # TODO Complete with your code and remove print below.
  print 'count job offers where ' + field_name + '=' + field_value


# Prints all job offers in the database, one per line, semicolon-separated, with
# fields in the order defined in the assignment.
def dump(params):
  # TODO Complete with your code and remove print below.
  sorted_keys = sorted(db.keys())

  for job_id in sorted_keys :
    job_details = db[job_id]

    output = ''
    
    for title in names:
      if title == 'Salary Frequency':
        frequency_value = ''

        frequency_id = job_details['Salary Frequency']
        
        for freq in db_frequency :
          if frequency_id == frequency_value :
            frequency_value = freq

            output =  output+'|'+str(frequency_value)
      else:
        output =  output+'|'+str(job_details[title])
        print job_id+output
     
    


# Prints all job offers, one per line, semicolon-separated, but only the
# specified fields, in the order specified for the view.
def view(fieldNames):
  # TODO Complete with your code and remove print below.
  print 'view for fields ' + str(fieldNames)


def executeCommand(commandLine):
  tokens = commandLine.split('|') #assume that this symbol is not part of the data
  command = tokens[0]
  parameters = tokens[1:]

  if command == 'insert':
    insert(parameters)
  elif command == 'delete_all':
    delete_all(parameters)
  elif command == 'update_all':
    update_all(parameters)
  elif command == 'find':
    find(parameters)
  elif command == 'count':
    count(parameters)
  elif command == 'count_unique':
    count_unique(parameters)
  elif command == 'clear':
    clear()
  elif command == 'dump':
    dump(parameters)
  elif command == 'view':
    view(parameters)
  else:
    print 'ERROR: Command %s does not exist' % (command,)
    assert(False)

def executeCommands(commandFileName):
  f = open(commandFileName)
  for line in f:
    executeCommand(line.strip())

if __name__ == '__main__':
  #TODO: You should load the data from the database here
  #print 'load'
  
  fjobs = open('jobs.db')
  ffrequency = open('frequency.db')

  for line in fjobs:
    tokens = line.split('|')
    job_id = tokens[0]
    db_jobid={}
    i = 0
    for value in tokens[1:]:
      db[jobid][names[i]] = value.strip()
      i += 1
    
  for line in ffrequency:
    tokens = line.split('|')
    frequency_id = tokens[0].strip('\n')
    frequency_value = tokens[1].strip('\n')
    db_frequency[frequency_id] = frequency_value 

 #   db[tokens[0]] = {} #for each token, store the value

  #  db[tokens[0]['Agency']] = tokens[1]
   # db[tokens[0]['# Of Positions']] = tokens[2]


  executeCommands(sys.argv[1])
  #TODO: You should save the data here
  print 'save'

  fjobs = open('jobs.db','w')
  ffrequency = open('frequency.db','w')

  sorted_keys = sorted(db.keys())

  for jobs in db:
    output = ''
    for title in names :
      output =  output+'|'+str(db[job_id][title])
    #print output
    fjobs.write(job_id+output+'\n') 

  for frequency in db_frequency:
    ffrequency.write(frequency+'|'+str(db_frequency[frequency])+'\n')

  #for frequency in db:
    #ffrequency.write()
