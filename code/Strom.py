# Strom

import pygame
import Eleapp
import scores
import button
#-------------------------------------------------------------------------------------------------------------                
#-------------------------------------------------------------------------------------------------------------
# widererkl                
    if menu_state == "erklw":
            screen.blit(Erkl_img,(10,10))
            if zurü_button.draw(screen):
                menu_state = "widerstand"
                clicked = True
            if weit_button.draw(screen):
                menu_state = "erklwiderser"
            if exit_button.draw(screen)and clicked == False:
                running = False                
    if menu_state == "erklwiderser":
            screen.blit(Erklwser_img,(10,10))
            if zurü_button.draw(screen):
                menu_state = "erklw"
                clicked = True
            if weit_button.draw(screen):
                menu_state = "erklwiderpara"
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "erklwiderpara":
            screen.blit(Erklwpara_img,(10,10))
            if zurü_button.draw(screen):
                menu_state = "erklwiderser"
                clicked = True
            if weit_button.draw(screen):
                menu_state = "erklwidergruppe"
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "erklwidergruppe":
            screen.blit(Erklwgruppe_img,(10,10))
            if zurü_button.draw(screen):
                menu_state = "erklwiderpara"
                clicked = True
            if weit_button.draw(screen):
                menu_state = "widerstand"
            if exit_button.draw(screen)and clicked == False:
                running = False
            if exit_button.draw(screen)and clicked == False:
                running = False
    #----------------------------------------------------
# widerleicht

    if menu_state == "widerleicht":
            screen.blit(WE1_img,(10,10))
            if  zwö_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l220_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WE2"
            if zurü_button.draw(screen):
                menu_state = "widerstand"
                clicked = True
            if exit_button.draw(screen):
                running = False
            if rech_button.draw(screen):
                pass        
    if menu_state == "WE2":            
            screen.blit(WE2_img,(10,10))
            if  zwei_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l220_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WE3"
            if zurü_button.draw(screen):
                menu_state = "widerleicht"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "WE3":            
            screen.blit(WE3_img,(10,10))
            if  acht_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l220_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WE4"
            if zurü_button.draw(screen):
                menu_state = "WE2"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False            
    if menu_state == "WE4":
            screen.blit(WE4_img,(10,10))
            if  zwei_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l220_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WE5"
            if zurü_button.draw(screen):
                menu_state = "WE3"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WE5":
            screen.blit(WE5_img,(10,10))
            if  vier_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l220_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WE6"
            if zurü_button.draw(screen):
                menu_state = "WE4"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WE6":        
            screen.blit(WE6_img,(10,10))
            if  zwö_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l220_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WE7"
            if zurü_button.draw(screen):
                menu_state = "WE5"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WE7":            
            screen.blit(WE7_img,(10,10))
            if  vier_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l220_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WE8"
            if zurü_button.draw(screen):
                menu_state = "WE6"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WE8":            
            screen.blit(WE8_img,(10,10))
            if  zwö_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l220_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WE9"
            if zurü_button.draw(screen):
                menu_state = "WE7"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False      
    if menu_state == "WE9":        
            screen.blit(WE9_img,(10,10))
            if  achtz_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l220_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WE10"
            if zurü_button.draw(screen):
                menu_state = "WE8"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WE10":            
            screen.blit(WE10_img,(10,10))
            if  zeh_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l220_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "resultatl"
            if zurü_button.draw(screen):
                menu_state = "WE9"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False    
    if menu_state == "resultatl": 
            if zurü_button.draw(screen):                   
                menu_state = "WE10"                
                clicked = True
            if menu_button.draw(screen):                   
                menu_state = "widerstand"                
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
#----------------------------------------------------
# widermitt
    if menu_state == "erklwidermitt":
            if zurü_button.draw(screen):
                menu_state = "widerstand"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "mittelwider":
            if zurü_button.draw(screen):
                menu_state = "widerstand"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "mittelwider":
            screen.blit(WM1_img,(10,10))
            if  hun_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l100200_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WM2"
            if zurü_button.draw(screen):
                menu_state = "widerstand"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "WM2":            
            screen.blit(WM2_img,(10,10))
            if  hunfün_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l100200_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WM3"
            if zurü_button.draw(screen):
                menu_state = "mittelwider"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "WM3":            
            screen.blit(WM3_img,(10,10))
            if  hun_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l100200_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WM4"
            if zurü_button.draw(screen):
                menu_state = "WM2"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False            
    if menu_state == "WM4":
            screen.blit(WM4_img,(10,10))
            if  hun_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l100200_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WM5"
            if zurü_button.draw(screen):
                menu_state = "WM3"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WM5":
            screen.blit(WM5_img,(10,10))
            if  hunvie_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l100200_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WM6"
            if zurü_button.draw(screen):
                menu_state = "WM4"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WM6":        
            screen.blit(WM6_img,(10,10))
            if  hun_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l100200_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WM7"
            if zurü_button.draw(screen):
                menu_state = "WM5"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WM7":            
            screen.blit(WM7_img,(10,10))
            if  hunsex_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l100200_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WM8"
            if zurü_button.draw(screen):
                menu_state = "WM6"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WM8":            
            screen.blit(WM8_img,(10,10))
            if  hunz_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l100200_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WM9"
            if zurü_button.draw(screen):
                menu_state = "WM7"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False      
    if menu_state == "WM9":        
            screen.blit(WM9_img,(10,10))
            if  hun_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l100200_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WM10"
            if zurü_button.draw(screen):
                menu_state = "WM8"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WM10":            
            screen.blit(WM10_img,(10,10))
            if  hun_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if l100200_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "resultatm"
            if zurü_button.draw(screen):
                menu_state = "WM9"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False    
    if menu_state == "resultatm": 
            if zurü_button.draw(screen):                   
                menu_state = "WM10"                
                clicked = True
            if menu_button.draw(screen):                   
                menu_state = "widerstand"                
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
#----------------------------------------------------
# widerschwer

    if menu_state == "erklwiderschwer":
            if zurü_button.draw(screen):
                menu_state = "widerstand"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "schwerwider":
            if zurü_button.draw(screen):
                menu_state = "widerstand"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "schwerwider":
            screen.blit(WS1_img,(10,10))
            if  hunsibsib_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if lschwer_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WS2"
            if zurü_button.draw(screen):
                menu_state = "widerstand"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "WS2":            
            screen.blit(WS2_img,(10,10))
            if  hunzwavie_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if lschwer_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WS3"
            if zurü_button.draw(screen):
                menu_state = "schwerwider"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "WS3":            
            screen.blit(WS3_img,(10,10))
            if  hunzwafü_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if lschwer_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WS4"
            if zurü_button.draw(screen):
                menu_state = "WS2"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False            
    if menu_state == "WS4":
            screen.blit(WS4_img,(10,10))
            if  sibsib_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if lschwer_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WS5"
            if zurü_button.draw(screen):
                menu_state = "WS3"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WS5":
            screen.blit(WS5_img,(10,10))
            if  hundreivie_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if lschwer_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WS6"
            if zurü_button.draw(screen):
                menu_state = "WS4"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WS6":        
            screen.blit(WS6_img,(10,10))
            if  hunvievie_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if lschwer_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WS7"
            if zurü_button.draw(screen):
                menu_state = "WS5"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WS7":            
            screen.blit(WS7_img,(10,10))
            if  neusib_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if lschwer_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WS8"
            if zurü_button.draw(screen):
                menu_state = "WS6"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WS8":            
            screen.blit(WS8_img,(10,10))
            if  zweihunein_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if lschwer_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WS9"
            if zurü_button.draw(screen):
                menu_state = "WS7"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False      
    if menu_state == "WS9":        
            screen.blit(WS9_img,(10,10))
            if  hunzwadrei_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if lschwer_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WS10"
            if zurü_button.draw(screen):
                menu_state = "WS8"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "WS10":            
            screen.blit(WS10_img,(10,10))
            if  hunfüneu_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            if lschwer_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "resultats"
            if zurü_button.draw(screen):
                menu_state = "WS9"
                clicked = True                
            if exit_button.draw(screen)and clicked == False:
                running = False    
    if menu_state == "resultats": 
            screen.blit(gesch1_img,(50,50))
            if zurü_button.draw(screen):                   
                menu_state = "WS10"                
                clicked = True
            if menu_button.draw(screen):                   
                menu_state = "widerstand"                
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
#----------------------------------------------------
# widergemisch
    if menu_state == "erklwidergemisch":
            if zurü_button.draw(screen):
                menu_state = "widerstand"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "gemischtwider":
            if zurü_button.draw(screen):
                menu_state = "widerstand"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    # gemischt levels
    if menu_state == "resultatg": 
            screen.blit(gesch1_img,(50,50))
            if zurü_button.draw(screen):                   
                menu_state = "WG10"                
                clicked = True
            if menu_button.draw(screen):                   
                menu_state = "widerstand"                
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False    
    if menu_state == "erklstrom":
            if zurü_button.draw(screen):
                menu_state = "stromstärke"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "leichtstrom":
            if zurü_button.draw(screen):
                menu_state = "stromstärke"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "mittelstrom":
            if zurü_button.draw(screen):
                menu_state = "stromstärke"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "schwerstrom":
            if zurü_button.draw(screen):
                menu_state = "stromstärke"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "gemischtstrom":
            if zurü_button.draw(screen):
                menu_state = "stromstärke"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "erklgemisch":
            if zurü_button.draw(screen):
                menu_state = "gemischt"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "leichtgemisch":
            if zurü_button.draw(screen):
                menu_state = "gemischt"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "mittelgemisch":
            if zurü_button.draw(screen):
                menu_state = "gemischt"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "schwergemisch":
            if zurü_button.draw(screen):
                menu_state = "gemischt"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "gemischtgemisch":
            if zurü_button.draw(screen):
                menu_state = "gemischt"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "spielen": 
            if zurü_button.draw(screen):
                menu_state = "main"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
