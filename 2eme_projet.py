from typing import overload
import cv2
import numpy as np
import time




cap=cv2.VideoCapture(0)
cap.set(3,1440)
cap.set(4,720)
print('Width :' + str(cap.get(3)))
print('Height:' + str(cap.get(4)))



face_cascade = cv2.CascadeClassifier('D:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')

test_distance=1
num=""

i=0
cmpt=0
c=0
test_call=0
interface=0
#############POLICE NUMS ####################################
font = cv2.FONT_HERSHEY_TRIPLEX
fontScale = 2.5
color = (0, 0, 0)
thickness = 3



test=0
######################programme####################
while True:

   _, img=cap.read()
   


   

   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   faces = face_cascade.detectMultiScale(gray, 1.1, 4)



   if((test_distance==1)&(cmpt<8)&(interface==0)):
      
      # ************************ keyboard buttons **************************
     color_rect=(0,0,0)
     cv2.rectangle(img,(10,0),(90,100),color_rect,10) # button 1
     cv2.rectangle(img,(130,0),(210,100),color_rect,10) # button 2
     cv2 .rectangle(img,(250,0),(330,100),color_rect,10) # button 3
     cv2.rectangle(img,(370,0),(450,100),color_rect,10) # button 4
     cv2.rectangle(img,(490,0),(570,100),color_rect,10) # button 5 
     cv2.rectangle(img,(10,370),(90,470),color_rect,10) # button 6
     cv2.rectangle(img,(130,370),(210,470),color_rect,10) # button 7
     cv2.rectangle(img,(250,370),(330,470),color_rect,10) # button 8
     cv2.rectangle(img,(370,370),(450,470),color_rect,10) # button 9
     cv2.rectangle(img,(490,370),(570,470),color_rect,10) # button 0

        



      
   
      
   
      # 1 
     text = cv2.putText(img, '1', (25,70), font, fontScale,color, thickness, cv2.LINE_AA, False)
     # 2
     text = cv2.putText(img, '2', (145,70), font, fontScale,color, thickness, cv2.LINE_AA, False)
     #3
     text = cv2.putText(img, '3', (265,70), font, fontScale,color, thickness, cv2.LINE_AA, False)
     #4
     text = cv2.putText(img, '4', (380,70), font, fontScale,color, thickness, cv2.LINE_AA, False)
     # 5
     text = cv2.putText(img, '5',(505,70), font, fontScale,color, thickness, cv2.LINE_AA, False)
     # 6
     text = cv2.putText(img, '6', (25,440), font, fontScale,color, thickness, cv2.LINE_AA, False)
     # 7 
     text = cv2.putText(img, '7', (145,440), font, fontScale,color, thickness, cv2.LINE_AA, False)
     # 8
     text = cv2.putText(img, '8', (265,440), font, fontScale,color, thickness, cv2.LINE_AA, False)    
     # 9
     text = cv2.putText(img, '9', (380,440), font, fontScale,color, thickness, cv2.LINE_AA, False)
      # 0
     text = cv2.putText(img, '0', (505,440), font, fontScale,color, thickness, cv2.LINE_AA, False)
   


  
 #dessiner les  rectangles du visage

   for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3) 
        cv2.putText(img,'visage',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(250,250,250),1)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        absc_cer1 = w / 2    


        cv2.circle(img,(x+(w//2),y-20),5,(255,0,255),18) # cercle au dessus
        cv2.circle(img,(x+w//2,h+y+20),5,(255,0,255),18) # cercle au dessous
        cv2.circle(img,(x+w+20,y+h//2),5,(255,0,255),18) # cercle a droite 
        cv2.circle(img,(x-20,y+h//2),5,(255,0,255),18) # cercle a gauche
       
        choix_dessus_x=x+(w//2)    
        choix_dessus_y=y-20 
   

        choix_dessous_x=x+w//2   
        choix_dessous_y=h+y+20 

        choix_droite_x=x+w+20
        choix_droite_y=y+h//2

        choix_gauche_x=x-20
        choix_gauche_y=y+h//2

        #print('x face =' ,x)
        #print('y face =' ,y)
        #print('w face =' ,w)
        #print('h face =' ,h)

        distance=w
        print('distance est  =' ,w)
        
        
     
        cv2.line(img,(x,y),(w+x,y),(0,0,255),4)

        seg_1= cv2.line(img,(x+w//2,y) , (x+(w//2),y-20), (0, 255 , 0),10)
        seg_2 = cv2.line(img,(x+w//2,h+y) , (x+w//2,h+y+20), (0, 255 , 0),10)
        seg_3 = cv2.line(img,(x+w,y+h//2) , (x+w+20,y+h//2), (0, 255 , 0),10)
        seg_4 = cv2.line(img,(x,y+h//2) , (x-20,y+h//2), (0, 255 , 0),10)

        


        if (distance>=190):
         text = cv2.putText(img, 'please keep 0.7 m distance at least  ', (20,300),1,cv2.FONT_HERSHEY_DUPLEX,(0,0,255),1, cv2.LINE_AA, False)
         test_distance=0
         break
        else :test_distance=1



        if(test_distance==1)&(cmpt<8):####verification

              color_rect_se=(255,0,0)
              color_num_se=(255,0,0)
              

              

              numero = cv2.putText(img, num, (100,315), 1, fontScale,(0,0,0), 1, cv2.LINE_AA, False)


              cv2.rectangle(img,(100,270),(500,320),(0,0,0),2) #rectangle du numero compose

              




             # button 1 selectionne  
              if(choix_dessus_x>10)&(choix_dessus_x<90)&(choix_dessus_y>0)&(choix_dessus_y<100):
                cv2.rectangle(img,(10,0),(90,100),color_rect_se,10)
                text = cv2.putText(img, '1', (25,70), font, fontScale,color_num_se, thickness, cv2.LINE_AA, False)
                

                i=i+1
                cv2.rectangle(img,(10,0),(90,100),(255,0,0),i+10)
                if (i>=20):
                 num=num+'1'
                 numero = cv2.putText(img, num, (100,315), 1, fontScale,(0,0,0), 1, cv2.LINE_AA, False)
                 i=0
                 cmpt=cmpt+1
                break   



              # button 2 selectionne 
              if(choix_dessus_x>130)&(choix_dessus_x<210)&(choix_dessus_y>0)&(choix_dessus_y<100):
                cv2.rectangle(img,(130,0),(210,100),color_rect_se,10) 
                text = cv2.putText(img, '2', (145,70), font, fontScale,color_num_se, thickness, cv2.LINE_AA, False)


                i=i+1
                cv2.rectangle(img,(130,0),(210,100),(255,0,0),i+10)

                if (i>=20):
                 num=num+'2'
                 numero = cv2.putText(img, num, (100,315), 1, fontScale,(0,0,0), 1, cv2.LINE_AA, False)
                 i=0
                 cmpt=cmpt+1

                break 


              # button 3 selectionne
              if(choix_dessus_x>250)&(choix_dessus_x<330)&(choix_dessus_y>0)&(choix_dessus_y<100):
                cv2 .rectangle(img,(250,0),(330,100),color_rect_se,10) 
                text = cv2.putText(img, '3', (265,70), font, fontScale,color_num_se, thickness, cv2.LINE_AA, False)

                i=i+1
                cv2.rectangle(img,(250,0),(330,100),(255,0,0),i+10)

                if (i>=20):
                  num=num+'3'
                  numero = cv2.putText(img, num, (100,315), 1, fontScale,(0,0,0), 1, cv2.LINE_AA, False)
                  i=0
                  cmpt=cmpt+1

                break 

               



              # button 4 selectionne
              if(choix_dessus_x>370)&(choix_dessus_x<450)&(choix_dessus_y>0)&(choix_dessus_y<100):
                cv2.rectangle(img,(370,0),(450,100),color_rect_se,10)  
                text = cv2.putText(img, '4', (380,70), font, fontScale,color_num_se, thickness, cv2.LINE_AA, False)


                i=i+1
                cv2.rectangle(img,(370,0),(450,100),(255,0,0),i+10)

                if (i>=20):
                 num=num+'4'
                 numero = cv2.putText(img, num, (100,315), 1, fontScale,(0,0,0), 1, cv2.LINE_AA, False)
                 i=0
                 cmpt=cmpt+1

                break 





             # button 5 selectionne
              if(choix_dessus_x>490)&(choix_dessus_x<570)&(choix_dessus_y>0)&(choix_dessus_y<100):
                cv2.rectangle(img,(490,0),(570,100),color_rect_se,10)  
                text = cv2.putText(img, '5',(505,70), font, fontScale,color_num_se, thickness, cv2.LINE_AA, False)



                i=i+1
                cv2.rectangle(img,(490,0),(570,100),(255,0,0),i+10)

                if (i>=20):
                 num=num+'5'
                 numero = cv2.putText(img, num, (100,315), 1, fontScale,(0,0,0), 1, cv2.LINE_AA, False)
                 i=0
                 cmpt=cmpt+1

                break 





             # button 6 selectionne
              if(choix_dessous_x>10)&(choix_dessous_x<90)&(choix_dessous_y>370)&(choix_dessous_y<470):
                cv2.rectangle(img,(10,370),(90,470),color_rect_se,10)   
                text = cv2.putText(img, '6', (25,440), font, fontScale,color_num_se, thickness, cv2.LINE_AA, False)

                i=i+1
                cv2.rectangle(img,(10,370),(90,470),(255,0,0),i+10)

                if (i>=20):
                 num=num+'6'
                 numero = cv2.putText(img, num, (100,315), 1, fontScale,(0,0,0), 1, cv2.LINE_AA, False)
                 i=0
                 cmpt=cmpt+1


                break




             # button 7 selectionne
              if(choix_dessous_x>130)&(choix_dessous_x<210)&(choix_dessous_y>370)&(choix_dessous_y<470):

                cv2.rectangle(img,(130,370),(210,470),color_rect_se,10) 
                text = cv2.putText(img, '7', (145,440), font, fontScale,color_num_se, thickness, cv2.LINE_AA, False)



                i=i+1
                cv2.rectangle(img,(130,370),(210,470),(255,0,0),i+10)

                if (i>=20):
                 num=num+'7'
                 numero = cv2.putText(img, num, (100,315), 1, fontScale,(0,0,0), 1, cv2.LINE_AA, False)
                 i=0
                 cmpt=cmpt+1

                break 
 
         

             # button 8 selectionne
              if(choix_dessous_x>250)&(choix_dessous_x<330)&(choix_dessous_y>370)&(choix_dessous_y<470):
                cv2.rectangle(img,(250,370),(330,470),color_rect_se,10)
                text = cv2.putText(img, '8', (265,440), font, fontScale,color_num_se, thickness, cv2.LINE_AA, False)



                i=i+1
                cv2.rectangle(img,(250,370),(330,470),(255,0,0),i+10)

                if (i>=20):
                 num=num+'8'
                 numero = cv2.putText(img, num, (100,315), 1, fontScale,(0,0,0), 1, cv2.LINE_AA, False)
                 i=0
                 cmpt=cmpt+1

                break 


             # button 9 selectionne 
              if(choix_dessous_x>370)&(choix_dessous_x<450)&(choix_dessous_y>370)&(choix_dessous_y<470):
                cv2.rectangle(img,(370,370),(450,470),color_rect_se,10) 
                text = cv2.putText(img, '9', (380,440), font, fontScale,color_num_se, thickness, cv2.LINE_AA, False)




                i=i+1
                cv2.rectangle(img,(370,370),(450,470),(255,0,0),i+10)

                if (i>=20):
                 num=num+'9'
                 numero = cv2.putText(img, num, (100,315), 1, fontScale,(0,0,0), 1, cv2.LINE_AA, False)
                 i=0
                 cmpt=cmpt+1

                break 
               


               
              # button 0 selectionne 
              if(choix_dessous_x>490)&(choix_dessous_x<570)&(choix_dessous_y>370)&(choix_dessous_y<470):
                cv2.rectangle(img,(490,370),(570,470),color_rect_se,10) 
                text = cv2.putText(img, '0', (505,440), font, fontScale,color_num_se, thickness, cv2.LINE_AA, False)



                i=i+1
                cv2.rectangle(img,(490,370),(570,470),(255,0,0),i+10)

                if (i>=20):
                 num=num+'0 '
                 numero = cv2.putText(img, num, (100,315), 1, fontScale,(0,0,0), 1, cv2.LINE_AA, False)
                 i=0
                 cmpt=cmpt+1

                break 
              
        if(cmpt>=8):interface=1


        if (test_distance==1)&(interface==1):
           cv2.rectangle(img,(50,50),(170,170),(0, 255 , 0),10) 
           cv2.rectangle(img,(470,50),(590,170),(0, 0 , 255),10)



           ligne_verte = cv2.line(img,(60,100) , (90,130), (0, 255 , 0), 8)
           ligne_verte = cv2.line(img,(90,130) , (160,80), (0, 255 , 0), 8)

  
           ligne_rouge = cv2.line(img,(505,90) , (555,130), (0, 0, 255), 10)
           ligne_rouge = cv2.line(img,(505,130) , (555,90), (0, 0 , 255), 10)





            #choix confirmé pour l'appel
           if (choix_gauche_x>50)&(choix_gauche_x<170)&(choix_gauche_y>50)&(choix_gauche_y<170):
             cv2.rectangle(img,(50,50),(170,170),(0, 255 , 0),16)
             ligne_verte = cv2.line(img,(60,100) , (90,130), (0, 255 , 0),12)
             ligne_verte = cv2.line(img,(90,130) , (160,80), (0, 255 , 0),12)
           

             c=c+1
             cv2.rectangle(img,(50,50),(170,170),(0, 255 , 0),16+c)
           

             if (c>=20):
               c=0
               test_call=1

             if (test_call==1): 
               text = cv2.putText(img, 'number comfirmed', (120,400), 1, fontScale,color, thickness, cv2.LINE_AA, False)




           #choix annulé pour l'appel
           elif  (choix_droite_x>470)&(choix_droite_x<590)&(choix_droite_y>50)&(choix_droite_y<170):
             cv2.rectangle(img,(470,50),(590,170),(0, 0 , 255),16)
             ligne_rouge = cv2.line(img,(505,90) , (555,130), (0, 0, 255), 12)
             ligne_rouge = cv2.line(img,(505,130) , (555,90), (0, 0 , 255), 12)
 
             c=c+1
             cv2.rectangle(img,(470,50),(590,170),(0, 0 , 255),16+c)
           

             if (c>=20):
               c=0
               test_call=2


             if (test_call==2): 
               interface=0
               cmpt=0
               num=''
               
               


           


 







   


################################## AFFICHAGE#####################
   cv2.imshow('face detector',img)


   if cv2.waitKey(1)==ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()