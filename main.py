import json
import openpyxl
import time



def main():
    previous=[]
    while(True): 
      print("start")
      book=openpyxl.open("Book1.xlsx",read_only=True)
      sheet=book.worksheets
      
      international=sheet[0]
      slots=jsonmaker(international)
      if slots is not previous:
        with open('international.json','w') as file:
          json.dump(slots,file, indent=2, ensure_ascii=True)
        previous=slots
      time.sleep(5)
    
    
""" 
    NEVERMIND THESE LINES
    domestic=sheet[1]
    slots=jsonmaker(domestic)
    with open('domestic.json','w') as file:
      json.dump(slots,file, indent=2, ensure_ascii=False)
"""
    
    
    

def jsonmaker(sheet):
  tags=["ID","destination","time","price","days"]
  slots=[]
  for row in range(1,sheet.max_row+1):
    busobj={}
    for column in range (0,5):
      busobj[tags[column]]=str(sheet[row][column].value)
    slots.append(busobj)
  res={}
  res['Monday']=slots
  res['Tuesday']=slots
  return res
    
if __name__== '__main__':
    main()