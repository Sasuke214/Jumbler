import math
import tkinter
import random

class JumbleTheFreakingCode:
         def __init__(self):
                  self.OriginalList=[]
                  self.JumbledList=[]
                  self.JumbleAnswer=[]
                  self.jumbleNo=0
                  try:
                           self.fp=open("JumbleIDbase.txt","r+")
                  except:
                           self.fp=open("JumbleIDbase.txt","w+")

                  try:
                           self.OutputFile=open("JumbleODbase.txt","r+")
                  except:
                           self.OutputFile=open("JumbleODbase.txt","w+")
                  try:
                           self.AnswerFile=open("JumbleAnsDbase.txt","r+")
                  except:
                           self.AnswerFile=open("JumbleAnsDbase.txt","w+")                           
                  
         def ReadAll(self):
                  self.DataFromDbase=self.fp.read()
         def PrepareToJumble(self,listtojumble):
                  questionsList=listtojumble.split('\n')

                  lengthofprogram=0
                  FullPreparedList=[]
                  for p in questionsList:
                           if(p.lstrip(' ')!=''):
                                    FullPreparedList.append(p)
                                    lengthofprogram+=1
                  self.OriginalList.append(FullPreparedList)
                  self.LetsJumble(FullPreparedList)
                  #print(lengthofprogram)

         def LetsJumble(self,FullPreparedList):
                  jumbledlist=[str]*len(FullPreparedList)
                  usedline=[]
                  currline=0
                  self.jumbleNo+=1
                  self.AnswerFile.write(str(self.jumbleNo)+'\n')
                  self.JumbleAnswer.append(str(self.jumbleNo)+'\n')
                  
                  for line in FullPreparedList:
                                    line_no=random.randint(0,len(FullPreparedList)-1)
                                    while line_no in usedline:
                                             line_no=random.randint(0,len(FullPreparedList)-1)
                                    usedline.append(line_no)
                                    jumbledlist.pop(line_no)

                                    currline+=1
                                    jumbleanswerstring=str(currline)+"   "+str(line_no+1)
                                    self.JumbleAnswer.append(jumbleanswerstring)
                                    self.AnswerFile.write(jumbleanswerstring+'\n')
                                    
                                    jumbledlist.insert(line_no,line)
                  #for c
##                  for i in range(0,len(jumbledlist)):
##                           jumbledlist[i]=jumbledlist[i].lstrip(' ')
                  self.AnswerFile.write('\n\n\n')
                  self.JumbleAnswer.append('\n\n\n')
                  self.JumbledList.append(jumbledlist)
                  
         def SeperateByQuestions(self):
                           ListOfQuestions=self.DataFromDbase.split('\n\n\n*\n\n')
                           for question in ListOfQuestions:
                                    self.PrepareToJumble(question)

                           
         def PrintData(self):
                  print(self.OriginalList)
                  print(self.JumbledList)
                  print(self.JumbleAnswer)
         def Finalized(self):
               for each in self.JumbledList:
                        line_no=1
                        for line in each:
                                 self.OutputFile.write(str(line_no)+'. '+line+'\n')
                                 line_no+=1
                        self.OutputFile.write('\n\n\n')
               self.OutputFile.close()
               self.AnswerFile.close()
               self.fp.close()



JTFC=JumbleTheFreakingCode()
JTFC.ReadAll()
JTFC.SeperateByQuestions()
JTFC.Finalized()

