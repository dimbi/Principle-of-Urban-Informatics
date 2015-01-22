##############################################
##############################################
#      Principle of urban infomatics GX5003  # 
#      Assignment 2                          #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
##############################################

import sys, os

############DEFINING GLOBAL VARIABLES#####################
db = {}
db_frequency = {}
db_agency = {}
db_requirement = {}
db_location = {}

names = ['Agency',
         '# Of Positions',
         'Business Title',
         'Civil Service Title',
         'Salary Range From',
         'Salary Range To',
         'Salary Frequency',
         'Work Location',
         'Division /Work Unit',
         'Job Description',
         'Minimum Qual Requirements',
         'Preferred Skills',
         'Additional Information',
         'Posting Date']


###################FUNCTIONS#########################

def clear():
  #print 'clear'    
  db.clear()
  db_frequency.clear()
  db_agency.clear()
  db_location.clear()
  db_requirement.clear()

# Inserts a job offer into the database.
def insert(fieldValues):
  #print 'insert'
  job_id      = fieldValues[0] #job_id
  job_details = fieldValues[1:] #job_details

  if job_id in db : #if the id exist in db, do nothing
    pass
  else :
    #for frequency
    frequency = fieldValues[7] #annual/monthly/weekly
    frequency_id = -1
    if frequency in db_frequency : #if value exist in db
      frequency_id = db_frequency[frequency]
    else :
      db_frequency[frequency] = len(db_frequency)
      frequency_id = db_frequency[frequency]
    
    #for agency
    agency = fieldValues[1] #agency
    agency_id = -1
    if agency in db_agency : #if value exist in db
      agency_id = db_agency[agency]
    else :
      db_agency[agency] = len(db_agency)
      agency_id = db_agency[agency]

    #for location
    location = fieldValues[8] #agency
    location_id = -1
    if location in db_location : #if value exist in db
      location_id = db_location[location]
    else :
      db_location[location] = len(db_location)
      location_id = db_location[location]

    #for requirement
    requirement = fieldValues[11] #requirement
    requirement_id = -1
    if requirement in db_requirement : #if value exist in db
      requirement_id = db_requirement[requirement]
    else :
      db_requirement[requirement] = len(db_requirement)
      requirement_id = db_requirement[requirement]

    db[job_id] = {}
    i = 0

    for detail in job_details :
      if i == 6: #Salary frequency
        db[job_id][names[i]] = db_frequency[detail]
      elif i == 0: #Salary agency
        db[job_id][names[i]] = db_agency[detail]
      elif i == 7: #location
        db[job_id][names[i]] = db_location[detail]
      elif i == 10: #min requirement
        db[job_id][names[i]] = db_requirement[detail]
      else:
        db[job_id][names[i]] = detail
      i += 1

# Updates all job offers that attend the field_name=old_value pair.
def update_all(params):
    #print 'update_all'
    query_field_name = params[0]
    query_field_value = params[1]
    update_field_name = params[2]
    update_field_value = params[3]

    updatedRowCount = 0
    to_update = {}
 
    #CHECKING SUB-DATABASE
    #For Salary Frequency
    if query_field_name == 'Salary Frequency':
      frequency_key = query_field_value
      for freq_key,freq_value in db_frequency.iteritems() :
        if freq_key == frequency_key :
          query_field_value = freq_value
    elif update_field_name == 'Salary Frequency':
      frequency_key = update_field_value
      if frequency_key in db_frequency:
        for freq_key,freq_value in db_frequency.iteritems() :
          if freq_key == frequency_key :
            update_field_value = freq_value
      else:
        db_frequency[frequency_key] = len(db_frequency)
        update_field_value = db_frequency[frequency_key]
    #For Agency
    if query_field_name == 'Agency':
      agency_key = query_field_value
      for agen_key,agen_value in db_agency.iteritems() :
        if agen_key == agency_key :
          query_field_value = agen_value
    elif update_field_name == 'Agency':
      agency_key = update_field_value
      if agency_key in db_agency:
        for agen_key,agen_value in db_agency.iteritems() :
          if agen_key == agency_key :
            update_field_value = agen_value
      else:
        db_agency[agency_key] = len(db_agency)
        update_field_value = db_agency[agency_key]
    #For Location
    if query_field_name == 'Work Location':
      location_key = query_field_value
      for loc_key,loc_value in db_location.iteritems() :
        if loc_key == location_key :
          query_field_value = loc_value
    elif update_field_name == 'Work Location':
      location_key = update_field_value
      if location_key in db_location:
        for loc_key,loc_value in db_location.iteritems() :
          if loc_key == location_key :
            update_field_value = loc_value
      else:
        db_location[location_key] = len(db_location)
        update_field_value = db_location[location_key]
    #For Min Salary requirement
    if query_field_name == 'Minimum Qual Requirements':
      requirement_key = query_field_value
      for req_key,req_value in db_requirement.iteritems() :
        if req_key == requirement_key :
          query_field_value = req_value
    elif update_field_name == 'Minimum Qual Requirements':
      requirement_key = update_field_value
      if requirement_key in db_requirement:
        for req_key,req_value in db_requirement.iteritems() :
          if req_key == requirement_key :
            update_field_value = req_value
      else:
        db_requirement[requirement_key] = len(db_requirement)
        update_field_value = db_requirement[requirement_key]

    #UPDATE THE VALUE, check if equal Job ID 
    for k,v in db.iteritems():
      if query_field_name == 'Job ID' and k == query_field_value:
        for key,value in db[k].iteritems():
          if db[k][update_field_name] == update_field_value:
            pass
          else:
            db[k][update_field_name]=update_field_value
            updatedRowCount+=1
      else:
        for key,value in db[k].iteritems():
          if key == query_field_name and value == query_field_value:
            if  db[k][update_field_name] == update_field_value:
              pass
            else: 
              db[k][update_field_name]=update_field_value
              updatedRowCount+=1
   
    # Prints number of updated rows in the database.
    print str(updatedRowCount)


#a Deletes all job offers that attend the field_name=field_value pair.
def delete_all(params):
  #print 'delete_all'
  query_field_name, query_field_value = params
  jobs_id_to_delete = []

  #CHECKING SUB-DATABASE and DELETE records in SUB DATABASE
  #For Salary Frequency
  if query_field_name == 'Salary Frequency':
    frequency_key = query_field_value
    for freq_key,freq_value in db_frequency.iteritems() :
      if freq_key == frequency_key :
        query_field_value = freq_value
    del db_frequency[frequency_key]
  #For Agency
  elif query_field_name == 'Agency':
    agency_key = query_field_value
    for agen_key,agen_value in db_agency.iteritems() :
      if agen_key == agency_key :
        query_field_value = agen_value
    del db_agency[agency_key]
  #For Location
  elif query_field_name == 'Work Location':
    location_key = query_field_value
    for loc_key,loc_value in db_location.iteritems() :
      if loc_key == location_key :
        query_field_value = loc_value
    del db_location[location_key]
  #For Min Salary requirement
  elif query_field_name == 'Minimum Qual Requirements':
    requirement_key = query_field_value
    for req_key,req_value in db_requirement.iteritems() :
      if req_key == requirement_key :
        query_field_value = req_value
    del db_requirement[requirement_key]

  #DELETE DATABASE RECORD, check if equal Job ID
  for k,v in db.iteritems():
    if query_field_name == 'Job ID' and k == query_field_value:
      jobs_id_to_delete.append(k)    
    else:
      for key,value in db[k].iteritems():
        if key == query_field_name and value == query_field_value:
          jobs_id_to_delete.append(k) 
 
  for i in jobs_id_to_delete:
    del db[i]


# Prints all job offers that match the query field_name=field_value, one per
# line, semicolon-separated, with fields in the order defined in the assignment.
def find(params):
  #print 'find'
  query_field_name, query_field_value = params
  jobs_id_to_find = []
  

  #CHECKING SUB-DATABASE and get the database id
  #For Salary Frequency
  if query_field_name == 'Salary Frequency':
    frequency_key = query_field_value
    for freq_key,freq_value in db_frequency.iteritems() :
      if freq_key == frequency_key :
        query_field_value = freq_value
  #For Agency
  elif query_field_name == 'Agency':
    agency_key = query_field_value
    for agen_key,agen_value in db_agency.iteritems() :
      if agen_key == agency_key :
        query_field_value = agen_value
  #For Location
  elif query_field_name == 'Work Location':
    location_key = query_field_value
    for loc_key,loc_value in db_location.iteritems() :
      if loc_key == location_key :
        query_field_value = loc_value
  #For Min Salary requirement
  elif query_field_name == 'Minimum Qual Requirements':
    requirement_key = query_field_value
    for req_key,req_value in db_requirement.iteritems() :
      if req_key == requirement_key :
        query_field_value = req_value

  #Get the Job ID which matches the query
  if (query_field_name == query_field_value): pass
  else:
    for k,v in db.iteritems():
      if query_field_name == 'Job ID' and k == query_field_value:
        jobs_id_to_find.append(k)    
      else:
        for key,value in db[k].iteritems():
          if key == query_field_name and value == query_field_value:
            jobs_id_to_find.append(k) 

  #Printing the selected records based on query
  for job_id in jobs_id_to_find :
    job_details = db[job_id]
    output = ''

    for title in names:
      #for salary frequency
      if title == 'Salary Frequency':
        frequency_value = job_details['Salary Frequency']       
        for freq_key,freq_value in db_frequency.iteritems() :
          if freq_value == frequency_value :
            output =  output+'|'+str(freq_key)
      #for salary agency
      elif title == 'Agency':
        agency_value = job_details['Agency']       
        for agen_key,agen_value in db_agency.iteritems() :
          if agen_value == agency_value :
            output =  output+'|'+str(agen_key)
      #for location
      elif title == 'Work Location':
        location_value = job_details['Work Location']       
        for loc_key,loc_value in db_location.iteritems() :
          if loc_value == location_value :
            output =  output+'|'+str(loc_key)
      #for requirement
      elif title == 'Minimum Qual Requirements':
        requirement_value = job_details['Minimum Qual Requirements']       
        for req_key,req_value in db_requirement.iteritems() :
          if req_value == requirement_value :
            output =  output+'|'+str(req_key)
      else:
        output =  output+'|'+str(job_details[title])

    print job_id+output


# Prints how many job offers match the query field_name=field_value.
def count(params):
  query_field_name, query_field_value = params
  counter = 0

  #CHECKING SUB-DATABASE and DELETE records in SUB DATABASE
  #For Salary Frequency
  if query_field_name == 'Salary Frequency':
    frequency_key = query_field_value
    for freq_key,freq_value in db_frequency.iteritems() :
      if freq_key == frequency_key :
        query_field_value = freq_value
  #For Agency
  elif query_field_name == 'Agency':
    agency_key = query_field_value
    for agen_key,agen_value in db_agency.iteritems() :
      if agen_key == agency_key :
        query_field_value = agen_value
  #For Location
  elif query_field_name == 'Work Location':
    location_key = query_field_value
    for loc_key,loc_value in db_location.iteritems() :
      if loc_key == location_key :
        query_field_value = loc_value
  #For Min Salary requirement
  elif query_field_name == 'Minimum Qual Requirements':
    requirement_key = query_field_value
    for req_key,req_value in db_requirement.iteritems() :
      if req_key == requirement_key :
        query_field_value = req_value

  #Count
  for k,v in db.iteritems():
    if query_field_name == 'Job ID' and k == query_field_value:
        counter += 1
    else:
      for key,value in db[k].iteritems():
        if key == query_field_name and value == query_field_value:
          counter += 1
  print str(counter) 
  



# Prints all job offers in the database, one per line, semicolon-separated, with
# fields in the order defined in the assignment.
def dump(params):
  #print 'dump'
  # TODO Complete with your code and remove print below.
  sorted_keys = sorted(db.keys())

  for job_id in sorted_keys :
    job_details = db[job_id]
    output = ''


    for title in names:
      #for salary frequency
      if title == 'Salary Frequency':
        frequency_value = job_details['Salary Frequency']       
        for freq_key,freq_value in db_frequency.iteritems() :
          if freq_value == frequency_value :
            output =  output+'|'+str(freq_key)
      #for salary agency
      elif title == 'Agency':
        agency_value = job_details['Agency']       
        for agen_key,agen_value in db_agency.iteritems() :
          if agen_value == agency_value :
            output =  output+'|'+str(agen_key)
      #for location
      elif title == 'Work Location':
        location_value = job_details['Work Location']       
        for loc_key,loc_value in db_location.iteritems() :
          if loc_value == location_value :
            output =  output+'|'+str(loc_key)
      #for requirement
      elif title == 'Minimum Qual Requirements':
        requirement_value = job_details['Minimum Qual Requirements']       
        for req_key,req_value in db_requirement.iteritems() :
          if req_value == requirement_value :
            output =  output+'|'+str(req_key)
      else:
        output =  output+'|'+str(job_details[title])

    print job_id+output


# Prints all job offers, one per line, semicolon-separated, but only the
# specified fields, in the order specified for the view.
def view(field_names):
  #print 'view'
  sorted_keys = sorted(db.keys())

  for job_id in sorted_keys :
    job_details = db[job_id]
    output = ''
    header = True 

    for title in field_names:
      #for JOB ID
      if title == 'Job ID':
        if header:
          output =  output+str(job_id)
          header = False
        else:
          output =  output+'|'+str(job_id)
      #for salary frequency
      elif title == 'Salary Frequency':
        frequency_value = job_details['Salary Frequency']       
        for freq_key,freq_value in db_frequency.iteritems() :
          if freq_value == frequency_value :
            if header:
              output =  output+str(freq_key)
              header = False
            else:
              output =  output+'|'+str(freq_key)
      #for salary agency
      elif title == 'Agency':
        agency_value = job_details['Agency']       
        for agen_key,agen_value in db_agency.iteritems() :
          if agen_value == agency_value :
            if header:
              output =  output+str(agen_key)
              header = False
            else:
              output =  output+'|'+str(agen_key)
      #for location
      elif title == 'Work Location':
        location_value = job_details['Work Location']       
        for loc_key,loc_value in db_location.iteritems() :
          if loc_value == location_value :
            if header:
              output =  output+str(loc_key)
              header = False
            else:
              output =  output+'|'+str(loc_key)
      #for requirement
      elif title == 'Minimum Qual Requirements':
        requirement_value = job_details['Minimum Qual Requirements']       
        for req_key,req_value in db_requirement.iteritems() :
          if req_value == requirement_value :
            if header:
              output =  output+str(req_key)
              header = False
            else:
              output =  output+'|'+str(req_key)
      else:
        if header:
          output =  output+str(freq_key)
          header = False
        else:
          output =  output+'|'+str(job_details[title])

    print output


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

  #Check if file exist
  if os.path.isfile('jobs.db'):pass
  else:open('jobs.db','a').close
  if os.path.isfile('frequency.db'):pass
  else:open('frequency.db','a').close
  if os.path.isfile('agency.db'):pass
  else:open('agency.db','a').close
  if os.path.isfile('location.db'):pass
  else:open('location.db','a').close
  if os.path.isfile('requirement.db'):pass
  else:open('requirement.db','a').close
 
  #LOAD the database
  #print 'load'
  fjobs = open('jobs.db')
  ffrequency = open('frequency.db')
  fagency = open('agency.db')
  flocation = open('location.db')
  frequirement = open('requirement.db')

  #for jobs database 
  for line in fjobs:
    tokens = line.split('|')
    job_id = tokens[0]
    db[job_id] = {}
    i = 0
    for value in tokens[1:]:
      db[job_id][names[i]] = value.strip()
      i += 1

  #for frequency database
  for line in ffrequency:
    tokens = line.split('|')
    frequency_id = tokens[0].strip('\n')
    frequency_value = tokens[1].strip('\n')
    db_frequency[frequency_id] = frequency_value 

  #for agency database
  for line in fagency:
    tokens = line.split('|')
    agency_id = tokens[0].strip('\n')
    agency_value = tokens[1].strip('\n')
    db_agency[agency_id] = agency_value 

  #for location database
  for line in flocation:
    tokens = line.split('|')
    location_id = tokens[0].strip('\n')
    location_value = tokens[1].strip('\n')
    db_location[location_id] = location_value 

  #for requirement database
  for line in frequirement:
    tokens = line.split('|')
    requirement_id = tokens[0].strip('\n')
    requirement_value = tokens[1].strip('\n')
    db_requirement[requirement_id] = requirement_value 

  #Defining variable 
  updatedRowCount = 0

  #Execute commands
  executeCommands(sys.argv[1])
 
  #SAVE the database
  #print 'save'
  fjobs = open('jobs.db','w')
  ffrequency = open('frequency.db','w')
  fagency = open('agency.db','w')
  flocation = open('location.db','w')
  frequirement = open('requirement.db','w')
  sorted_keys = sorted(db.keys())

  for jobs in db:
    output = ''
    for title in names :

      #for frequency
      if title == 'Salary Frequency':
        frequency_value = db[jobs]['Salary Frequency']
        for freq_key,freq_value in db_frequency.iteritems() :
          if freq_value == frequency_value :
            output =  output+'|'+str(freq_value)

      #for agency
      elif title == 'Agency':
        agency_value = db[jobs]['Agency']
        for agen_key,agen_value in db_agency.iteritems() :
          if agen_value == agency_value :
            output =  output+'|'+str(agen_value)

      #for location
      elif title == 'Work Location':
        location_value = db[jobs]['Work Location']
        for loc_key,loc_value in db_location.iteritems() :
          if loc_value == location_value :
            output =  output+'|'+str(loc_value)

      #for requirement
      elif title == 'Minimum Qual Requirements':
        requirement_value = db[jobs]['Minimum Qual Requirements']
        for req_key,req_value in db_requirement.iteritems() :
          if req_value == requirement_value :
            output =  output+'|'+str(req_value)
      else:
        output =  output+'|'+str(db[jobs][title])

    fjobs.write(jobs+output+'\n') 

  #print db

  #for frequency database
  for frequency in db_frequency:
    ffrequency.write(frequency+'|'+str(db_frequency[frequency])+'\n')

  #for agency database
  for agency in db_agency:
    fagency.write(agency+'|'+str(db_agency[agency])+'\n')

  #for location database
  for location in db_location:
    flocation.write(location+'|'+str(db_location[location])+'\n')

  #for requirement database
  for requirement in db_requirement:
    frequirement.write(requirement+'|'+str(db_requirement[requirement])+'\n')
