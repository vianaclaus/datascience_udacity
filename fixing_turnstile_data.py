import csv

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
   
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:
    
    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''
    
    def clean(string):
        while ' ' in string and '\r' in string and '\n' in string:
            string = string.replace(' ', '')
            string = string.replace('\r', '')
            string = string.replace('\n', '')
        return string
    
    for filename in filenames:
        
        with open(filename, "r") as f:
            lines = f.readlines()
            lines = [clean(line) for line in lines]
            
        #print(lines)
        
        parsed_lines = []
        for line in lines:
            line = line.split(',')
            prefix = ','.join(line[:3]) + ','
            line = line[3:]
            
            row = []
            #print(line)
            for index, item in enumerate(line):
                row += [item]
                if (index + 1) % 5 == 0:
                    parsed_lines += [prefix + ','.join(row)]
                    row = []
            
        #print(parsed_lines)
        
        new_file = 'updated_' + filename
        with open(new_file, 'wt') as f:
            for parsed_line in parsed_lines:
                f.write(parsed_line + '\n')
            
        my_file = open(new_file, 'r')
        print(my_file.read())
        my_file.close()
        
        
        
                            
                            
                            
                            
                            
                            
                            
                            
                            
            