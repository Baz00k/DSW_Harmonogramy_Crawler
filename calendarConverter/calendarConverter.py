import pandas as pd

def convertToGoogleCalendarCSV(inputFile, outputFile):
    # load data from csv file
    df = pd.read_csv(inputFile)
    # create 'Description' column from form of class and comments
    df['Description'] = df['Form Of Class'] + ', Komentarze: ' + df['Comments']
    
    # convert to google calendar format by dropping unnecessary columns and renaming the rest
    df = df.drop(columns=['Day Of Week', 'Number Of Hours', 'Form Of Class', 'Group', 'Lecturer', 'Form Of Passing', 'Mode Of Studies', 'Comments'])
    
    # add 'Private' column
    df['Private'] = 'True'
    
    # add 'All Day Event' column
    df['All Day Event'] = 'False'
    
    # save to csv file
    df.to_csv(f'data/calendar/{outputFile}', index=False)