import pygame 
import sys
import button
import os
import scores
# start pygame
pygame.init()
# locate folder
IMAGE_FOLDER1 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra"
IMAGE_FOLDER2 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/bbutt"
IMAGE_FOLDER3 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/gesch"
IMAGE_FOLDER4 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/formeln"
IMAGE_FOLDER5 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/gefa"
IMAGE_FOLDER6 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/spanleicht"
IMAGE_FOLDER7 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/spanmitt"
IMAGE_FOLDER8 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/spanschwer"
IMAGE_FOLDER9 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/widerleicht"
IMAGE_FOLDER11 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/widermitt"
IMAGE_FOLDER12 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/widerschwer"
IMAGE_FOLDER13 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/stromleicht"
IMAGE_FOLDER14 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/strommitt"
IMAGE_FOLDER15 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/stromschwer"
IMAGE_FOLDER16 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/gemischleicht"
IMAGE_FOLDER17 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/gemischmitt"
IMAGE_FOLDER18 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/gemischschwer"
IMAGE_FOLDER19 = "C:/Users/attam/Desktop/ISME/Maturaarbeit/eleapp/ggra/spielen"
#set screen size
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1074
screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))  # Oder pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# window title 
# add logo 
pygame.display.set_caption("Elektrizitäts Lernprogramm")
# timer = pygame.time.Clock()
# implement delta time and framerate
# image load
try:
# bg
    bg_image = pygame.image.load(os.path.join(IMAGE_FOLDER1,'bg.png')).convert_alpha()  
# menu buttons
    start_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'start.png')).convert_alpha()
# learn practice play
    lern_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'lernen.png')).convert_alpha()
    ueb_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'ueben.png')).convert_alpha()
    spi_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'spielen.png')).convert_alpha()
# history 
    ges_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'geschicht.png')).convert_alpha()
    gesch1_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'geschele.png')).convert_alpha()
    elegesch_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'elegesch.jpg')).convert_alpha()
# calculations 
    form_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'formeln.png')).convert_alpha()
# dangers
    gefa_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'gefa.png')).convert_alpha()
# span wider strom gemisch
    span_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'Spannung.png')).convert_alpha()
    wider_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'wider.png')).convert_alpha()
    strom_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'strom.png')).convert_alpha()
    gemisch_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'gemisch.png')).convert_alpha()
# tutorial easy medium hard
    erkl_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'erklärung.png')).convert_alpha()
    lei_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'leicht.png')).convert_alpha()
    mit_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'mittel.png')).convert_alpha()
    schwe_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'schwe.png')).convert_alpha()
# interface
    weit_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'weiter.png')).convert_alpha()
    zurü_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'zurü.png')).convert_alpha()
    exit_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'exit.png')).convert_alpha()
    menu_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'menu.png')).convert_alpha()
    richtig_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'richtig.png')).convert_alpha()
    falsch_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'falsch.png')).convert_alpha()
# level üeben
#span
# easy
    #SPL1_img = pygame.image.load(os.path.join(IMAGE_FOLDER6,'SPL1.png')).convert_alpha()
    #SPL2_img = pygame.image.load(os.path.join(IMAGE_FOLDER6,'SPL2.png')).convert_alpha()
    #SPL3_img = pygame.image.load(os.path.join(IMAGE_FOLDER6,'SPL3.png')).convert_alpha()
    #SPL4_img = pygame.image.load(os.path.join(IMAGE_FOLDER6,'SPL4.png')).convert_alpha()
    #SPL5_img = pygame.image.load(os.path.join(IMAGE_FOLDER6,'SPL5.png')).convert_alpha()
    #SPL6_img = pygame.image.load(os.path.join(IMAGE_FOLDER6,'SPL6.png')).convert_alpha()
    #SPL7_img = pygame.image.load(os.path.join(IMAGE_FOLDER6,'SPL7.png')).convert_alpha()
    #SPL8_img = pygame.image.load(os.path.join(IMAGE_FOLDER6,'SPL8.png')).convert_alpha()
    #SPL9_img = pygame.image.load(os.path.join(IMAGE_FOLDER6,'SPL9.png')).convert_alpha()
    #SPL10_img = pygame.image.load(os.path.join(IMAGE_FOLDER6,'SPL10.png')).convert_alpha()
# medium
    #SPM1_img = pygame.image.load(os.path.join(IMAGE_FOLDER7,'SPM1.png')).convert_alpha()
    #SPM2_img = pygame.image.load(os.path.join(IMAGE_FOLDER7,'SPM2.png')).convert_alpha()
    #SPM3_img = pygame.image.load(os.path.join(IMAGE_FOLDER7,'SPM3.png')).convert_alpha()
    #SPM4_img = pygame.image.load(os.path.join(IMAGE_FOLDER7,'SPM4.png')).convert_alpha()
    #SPM5_img = pygame.image.load(os.path.join(IMAGE_FOLDER7,'SPM5.png')).convert_alpha()
    #SPM6_img = pygame.image.load(os.path.join(IMAGE_FOLDER7,'SPM6.png')).convert_alpha()
    #SPM7_img = pygame.image.load(os.path.join(IMAGE_FOLDER7,'SPM7.png')).convert_alpha()
    #SPM8_img = pygame.image.load(os.path.join(IMAGE_FOLDER7,'SPM8.png')).convert_alpha()
    #SPM9_img = pygame.image.load(os.path.join(IMAGE_FOLDER7,'SPM9.png')).convert_alpha()
    #SPM10_img = pygame.image.load(os.path.join(IMAGE_FOLDER7,'SPM10.png')).convert_alpha()
# hard
    #SPS1_img = pygame.image.load(os.path.join(IMAGE_FOLDER8,'SPS1.png')).convert_alpha()
    #SPS2_img = pygame.image.load(os.path.join(IMAGE_FOLDER8,'SPS2.png')).convert_alpha()
    #SPS3_img = pygame.image.load(os.path.join(IMAGE_FOLDER8,'SPS3.png')).convert_alpha()
    #SPS4_img = pygame.image.load(os.path.join(IMAGE_FOLDER8,'SPS4.png')).convert_alpha()
    #SPS5_img = pygame.image.load(os.path.join(IMAGE_FOLDER8,'SPS5.png')).convert_alpha()
    #SPS6_img = pygame.image.load(os.path.join(IMAGE_FOLDER8,'SPS6.png')).convert_alpha()
    #SPS7_img = pygame.image.load(os.path.join(IMAGE_FOLDER8,'SPS7.png')).convert_alpha()
    #SPS8_img = pygame.image.load(os.path.join(IMAGE_FOLDER8,'SPS8.png')).convert_alpha()
    #SPS9_img = pygame.image.load(os.path.join(IMAGE_FOLDER8,'SPS9.png')).convert_alpha()
    #SPS10_img = pygame.image.load(os.path.join(IMAGE_FOLDER8,'SPS10.png')).convert_alpha()
# wider
# easy WE zu WL
    WE1_img = pygame.image.load(os.path.join(IMAGE_FOLDER9,'WE1.png')).convert_alpha()
    WE2_img = pygame.image.load(os.path.join(IMAGE_FOLDER9,'WE2.png')).convert_alpha()
    WE3_img = pygame.image.load(os.path.join(IMAGE_FOLDER9,'WE3.png')).convert_alpha()
    WE4_img = pygame.image.load(os.path.join(IMAGE_FOLDER9,'WE4.png')).convert_alpha()
    WE5_img = pygame.image.load(os.path.join(IMAGE_FOLDER9,'WE5.png')).convert_alpha()
    WE6_img = pygame.image.load(os.path.join(IMAGE_FOLDER9,'WE6.png')).convert_alpha()
    WE7_img = pygame.image.load(os.path.join(IMAGE_FOLDER9,'WE7.png')).convert_alpha()
    WE8_img = pygame.image.load(os.path.join(IMAGE_FOLDER9,'WE8.png')).convert_alpha()
    WE9_img = pygame.image.load(os.path.join(IMAGE_FOLDER9,'WE9.png')).convert_alpha()
    WE10_img = pygame.image.load(os.path.join(IMAGE_FOLDER9,'WE10.png')).convert_alpha()
# medium
    WM1_img = pygame.image.load(os.path.join(IMAGE_FOLDER11,'WM1.png')).convert_alpha()
    WM2_img = pygame.image.load(os.path.join(IMAGE_FOLDER11,'WM2.png')).convert_alpha()
    WM3_img = pygame.image.load(os.path.join(IMAGE_FOLDER11,'WM3.png')).convert_alpha()
    WM4_img = pygame.image.load(os.path.join(IMAGE_FOLDER11,'WM4.png')).convert_alpha()
    WM5_img = pygame.image.load(os.path.join(IMAGE_FOLDER11,'WM5.png')).convert_alpha()
    WM6_img = pygame.image.load(os.path.join(IMAGE_FOLDER11,'WM6.png')).convert_alpha()
    WM7_img = pygame.image.load(os.path.join(IMAGE_FOLDER11,'WM7.png')).convert_alpha()
    WM8_img = pygame.image.load(os.path.join(IMAGE_FOLDER11,'WM8.png')).convert_alpha()
    WM9_img = pygame.image.load(os.path.join(IMAGE_FOLDER11,'WM9.png')).convert_alpha()
    WM10_img = pygame.image.load(os.path.join(IMAGE_FOLDER11,'WM10.png')).convert_alpha()
# hard
    WS1_img = pygame.image.load(os.path.join(IMAGE_FOLDER12,'WS1.png')).convert_alpha()
    WS2_img = pygame.image.load(os.path.join(IMAGE_FOLDER12,'WS2.png')).convert_alpha()
    WS3_img = pygame.image.load(os.path.join(IMAGE_FOLDER12,'WS3.png')).convert_alpha()
    WS4_img = pygame.image.load(os.path.join(IMAGE_FOLDER12,'WS4.png')).convert_alpha()
    WS5_img = pygame.image.load(os.path.join(IMAGE_FOLDER12,'WS5.png')).convert_alpha()
    WS6_img = pygame.image.load(os.path.join(IMAGE_FOLDER12,'WS6.png')).convert_alpha()
    WS7_img = pygame.image.load(os.path.join(IMAGE_FOLDER12,'WS7.png')).convert_alpha()
    WS8_img = pygame.image.load(os.path.join(IMAGE_FOLDER12,'WS8.png')).convert_alpha()
    WS9_img = pygame.image.load(os.path.join(IMAGE_FOLDER12,'WS9.png')).convert_alpha()
    WS10_img = pygame.image.load(os.path.join(IMAGE_FOLDER12,'WS10.png')).convert_alpha()
# strom
# easy
    #STL1_img = pygame.image.load(os.path.join(IMAGE_FOLDER13,'STL1.png')).convert_alpha()
    #STL2_img = pygame.image.load(os.path.join(IMAGE_FOLDER13,'STL2.png')).convert_alpha()
    #STL3_img = pygame.image.load(os.path.join(IMAGE_FOLDER13,'STL3.png')).convert_alpha()
    #STL4_img = pygame.image.load(os.path.join(IMAGE_FOLDER13,'STL4.png')).convert_alpha()
    #STL5_img = pygame.image.load(os.path.join(IMAGE_FOLDER13,'STL5.png')).convert_alpha()
    #STL6_img = pygame.image.load(os.path.join(IMAGE_FOLDER13,'STL6.png')).convert_alpha()
    #STL7_img = pygame.image.load(os.path.join(IMAGE_FOLDER13,'STL7.png')).convert_alpha()
    #STL8_img = pygame.image.load(os.path.join(IMAGE_FOLDER13,'STL8.png')).convert_alpha()
    #STL9_img = pygame.image.load(os.path.join(IMAGE_FOLDER13,'STL9.png')).convert_alpha()
    #STL10_img = pygame.image.load(os.path.join(IMAGE_FOLDER13,'STL10.png')).convert_alpha()
# medium
    #STM1_img = pygame.image.load(os.path.join(IMAGE_FOLDER14,'STM1.png')).convert_alpha()
    #STM2_img = pygame.image.load(os.path.join(IMAGE_FOLDER14,'STM2.png')).convert_alpha()
    #STM3_img = pygame.image.load(os.path.join(IMAGE_FOLDER14,'STM3.png')).convert_alpha()
    #STM4_img = pygame.image.load(os.path.join(IMAGE_FOLDER14,'STM4.png')).convert_alpha()
    #STM5_img = pygame.image.load(os.path.join(IMAGE_FOLDER14,'STM5.png')).convert_alpha()
    #STM6_img = pygame.image.load(os.path.join(IMAGE_FOLDER14,'STM6.png')).convert_alpha()
    #STM7_img = pygame.image.load(os.path.join(IMAGE_FOLDER14,'STM7.png')).convert_alpha()
    #STM8_img = pygame.image.load(os.path.join(IMAGE_FOLDER14,'STM8.png')).convert_alpha()
    #STM9_img = pygame.image.load(os.path.join(IMAGE_FOLDER14,'STM9.png')).convert_alpha()
    #STM10_img = pygame.image.load(os.path.join(IMAGE_FOLDER14,'STM10.png')).convert_alpha()
# hard
    #STS1_img = pygame.image.load(os.path.join(IMAGE_FOLDER15,'STS1.png')).convert_alpha()
    #STS2_img = pygame.image.load(os.path.join(IMAGE_FOLDER15,'STS2.png')).convert_alpha()
    #STS3_img = pygame.image.load(os.path.join(IMAGE_FOLDER15,'STS3.png')).convert_alpha()
    #STS4_img = pygame.image.load(os.path.join(IMAGE_FOLDER15,'STS4.png')).convert_alpha()
    #STS5_img = pygame.image.load(os.path.join(IMAGE_FOLDER15,'STS5.png')).convert_alpha()
    #STS6_img = pygame.image.load(os.path.join(IMAGE_FOLDER15,'STS6.png')).convert_alpha()
    #STS7_img = pygame.image.load(os.path.join(IMAGE_FOLDER15,'STS7.png')).convert_alpha()
    #STS8_img = pygame.image.load(os.path.join(IMAGE_FOLDER15,'STS8.png')).convert_alpha()
    #STS9_img = pygame.image.load(os.path.join(IMAGE_FOLDER15,'STS9.png')).convert_alpha()
    #STS10_img = pygame.image.load(os.path.join(IMAGE_FOLDER15,'STS10.png')).convert_alpha()
# gemisch
# easy
    #GL1_img = pygame.image.load(os.path.join(IMAGE_FOLDER16,'GL1.png')).convert_alpha()
    #GL2_img = pygame.image.load(os.path.join(IMAGE_FOLDER16,'GL2.png')).convert_alpha()
    #GL3_img = pygame.image.load(os.path.join(IMAGE_FOLDER16,'GL3.png')).convert_alpha()
    #GL4_img = pygame.image.load(os.path.join(IMAGE_FOLDER16,'GL4.png')).convert_alpha()
    #GL5_img = pygame.image.load(os.path.join(IMAGE_FOLDER16,'GL5.png')).convert_alpha()
    #GL6_img = pygame.image.load(os.path.join(IMAGE_FOLDER16,'GL6.png')).convert_alpha()
    #GL7_img = pygame.image.load(os.path.join(IMAGE_FOLDER16,'GL7.png')).convert_alpha()
    #GL8_img = pygame.image.load(os.path.join(IMAGE_FOLDER16,'GL8.png')).convert_alpha()
    #GL9_img = pygame.image.load(os.path.join(IMAGE_FOLDER16,'GL9.png')).convert_alpha()
    #GL10_img = pygame.image.load(os.path.join(IMAGE_FOLDER16,'GL10.png')).convert_alpha()
# medium
    #GM1_img = pygame.image.load(os.path.join(IMAGE_FOLDER17,'GM1.png')).convert_alpha()
    #GM2_img = pygame.image.load(os.path.join(IMAGE_FOLDER17,'GM2.png')).convert_alpha()
    #GM3_img = pygame.image.load(os.path.join(IMAGE_FOLDER17,'GM3.png')).convert_alpha()
    #GM4_img = pygame.image.load(os.path.join(IMAGE_FOLDER17,'GM4.png')).convert_alpha()
    #GM5_img = pygame.image.load(os.path.join(IMAGE_FOLDER17,'GM5.png')).convert_alpha()
    #GM6_img = pygame.image.load(os.path.join(IMAGE_FOLDER17,'GM6.png')).convert_alpha()
    #GM7_img = pygame.image.load(os.path.join(IMAGE_FOLDER17,'GM7.png')).convert_alpha()
    #GM8_img = pygame.image.load(os.path.join(IMAGE_FOLDER17,'GM8.png')).convert_alpha()
    #GM9_img = pygame.image.load(os.path.join(IMAGE_FOLDER17,'GM9.png')).convert_alpha()
    #GM10_img = pygame.image.load(os.path.join(IMAGE_FOLDER17,'GM10.png')).convert_alpha()
# hard
    #GS1_img = pygame.image.load(os.path.join(IMAGE_FOLDER18,'GS1.png')).convert_alpha()
    #GS2_img = pygame.image.load(os.path.join(IMAGE_FOLDER18,'GS2.png')).convert_alpha()
    #GS3_img = pygame.image.load(os.path.join(IMAGE_FOLDER18,'GS3.png')).convert_alpha()
    #GS4_img = pygame.image.load(os.path.join(IMAGE_FOLDER18,'GS4.png')).convert_alpha()
    #GS5_img = pygame.image.load(os.path.join(IMAGE_FOLDER18,'GS5.png')).convert_alpha()
    #GS6_img = pygame.image.load(os.path.join(IMAGE_FOLDER18,'GS6.png')).convert_alpha()
    #GS7_img = pygame.image.load(os.path.join(IMAGE_FOLDER18,'GS7.png')).convert_alpha()
    #GS8_img = pygame.image.load(os.path.join(IMAGE_FOLDER18,'GS8.png')).convert_alpha()
    #GS9_img = pygame.image.load(os.path.join(IMAGE_FOLDER18,'GS9.png')).convert_alpha()
    #GS10_img = pygame.image.load(os.path.join(IMAGE_FOLDER18,'GS10.png')).convert_alpha()
# solutions wrong
    l220_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'l220.png')).convert_alpha()
    l100200_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'l100200.png')).convert_alpha()
    lschwer_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'lschwer.png')).convert_alpha()
# easy right
    zwei_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'2ohm.png')).convert_alpha()
    vier_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'4.png')).convert_alpha()
    sex_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'6.png')).convert_alpha()
    acht_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'8.png')).convert_alpha()
    zeh_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'10.png')).convert_alpha()
    zwö_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'12.png')).convert_alpha()
    vierz_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'14.png')).convert_alpha()
    sexz_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'16.png')).convert_alpha()
    achtz_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'18.png')).convert_alpha()
    zwan_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'20.png')).convert_alpha()
# medium right
    hun_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'100.png')).convert_alpha()
    hunz_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'110.png')).convert_alpha()
    hunzwa_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'120.png')).convert_alpha()
    hundre_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'130.png')).convert_alpha()
    hunvie_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'140.png')).convert_alpha()
    hunfün_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'150.png')).convert_alpha()
    hunsex_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'160.png')).convert_alpha()
    hunsib_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'170.png')).convert_alpha()
    hunacht_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'180.png')).convert_alpha()
    hunneu_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'190.png')).convert_alpha()
    zweihun_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'200.png')).convert_alpha()
 # hard
    sibsib_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'77.png')).convert_alpha()
    neusib_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'97.png')).convert_alpha()
    hunzwadrei_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'123.png')).convert_alpha()
    hunzwavie_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'124.png')).convert_alpha()
    hunzwafü_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'125.png')).convert_alpha()
    hundreivie_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'134.png')).convert_alpha()
    hunvievie_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'144.png')).convert_alpha()
    hunfüneu_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'159.png')).convert_alpha()
    hunsibsib_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'177.png')).convert_alpha()
    zweihunein_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'201.png')).convert_alpha()
# failsave image
except pygame.error as e:
    print(f"Fehler beim Laden des Bildes: {e}")
    sys.exit()
# buttons
# background as button to scale
bg_button = button.Button(-50,-30,bg_image,1.05)
# menu
start_button = button.Button(700,400,start_img,1)
# interface
exit_button = button.Button(118,855,exit_img,0.9)
zurü_button = button.Button(1470,100,zurü_img,1)
weit_button  = button.Button(1629,100,weit_img,1)
menu_button  = button.Button(700, 450,menu_img,1)
# menu lern
lern_button = button.Button(700, 250,lern_img,1)
ueb_button  = button.Button(700, 450,ueb_img,1)
spi_button  = button.Button(700, 650,spi_img,1)
# menu geschformgefa
ges_button = button.Button(700, 250,ges_img,1)
form_button = button.Button(700, 450,form_img,1)
gefabutton = button.Button(700, 650,gefa_img,1)
# menu spawid
span_button = button.Button(700, 150,span_img,1)
wider_button = button.Button(700, 350,wider_img,1)
strom_button = button.Button(700, 550,strom_img,1)
gemisch_button = button.Button(700,750,gemisch_img,1)
# menu spannung
erklspan_button = button.Button(700, 150,erkl_img,1)
leispan_button = button.Button(700, 350,lei_img,1)
mitspan_button = button.Button(700, 550,mit_img,1)
schwespan_button = button.Button(700, 750,schwe_img,1)
# menu widerstand
erklwider_button = button.Button(700, 150,erkl_img,1)
leiwider_button = button.Button(700, 350,lei_img,1)
mitwider_button = button.Button(700, 550,mit_img,1)
schwewider_button = button.Button(700, 750,schwe_img,1)
# menu stromstärke
erklstrom_button = button.Button(700, 150,erkl_img,1)
leistrom_button = button.Button(700, 350,lei_img,1)
mitstrom_button = button.Button(700, 550,mit_img,1)
schwestrom_button = button.Button(700, 750,schwe_img,1)
# menu gemischt
erklgemisch_button = button.Button(700, 150,erkl_img,1)
leigemisch_button = button.Button(700, 350,lei_img,1)
mitgemisch_button = button.Button(700, 550,mit_img,1)
schwegemisch_button = button.Button(700, 750,schwe_img,1)
# solutions 2-20
l220_button = button.Button(1495,500,l220_img,1.1)
zwei_button = button.Button(1500, 585,zwei_img,1.08)
vier_button = button.Button(1500, 663,vier_img,1.08)
sex_button = button.Button(1500, 400,sex_img,1.08)
acht_button = button.Button(1501, 824,acht_img,1)
zeh_button = button.Button(1500, 901,zeh_img,1.08)
zwö_button = button.Button(1642, 584,zwö_img,1.08)
vierz_button = button.Button(1642, 686,vierz_img,1.08)
sexz_button = button.Button(1642, 400,sexz_img,1.08)
achtz_button = button.Button(1640,822,achtz_img,1.06)
zwan_button = button.Button(1642, 400,zwan_img,1.08)
# solutions 100-200
l100200_button = button.Button(1495, 500,l100200_img,1.1)
hun_button = button.Button(1500, 507,hun_img,1.08)
hunz_button = button.Button(1500, 584,hunz_img,1.08)
hunzwa_button = button.Button(1500, 664,hunzwa_img,1.06)
hundre_button = button.Button(1500, 400,hundre_img,1.08)
hunvie_button = button.Button(1500, 823,hunvie_img,1.06)
hunfün_button = button.Button(1500, 901,hunfün_img,1.08)
hunsex_button = button.Button(1640, 584,hunsex_img,1.08)
hunsib_button = button.Button(1642, 400,hunsib_img,1.08)
hunacht_button = button.Button(1642, 400,hunacht_img,1.08)
hunneu_button = button.Button(1642, 400,hunneu_img,1.08)
zweihun_button = button.Button(1642, 400,zweihun_img,1.08)
# solutions span hard
lschwer_button = button.Button(1495, 505,lschwer_img,1.1)
sibsib_button = button.Button(1500, 828,sibsib_img,1.08)
neusib_button = button.Button(1500, 908,neusib_img,1.08)
hunzwadrei_button = button.Button(1500, 515,hunzwadrei_img,1.06)
hunzwavie_button = button.Button(1640, 747,hunzwavie_img,1.08)
hunzwafü_button = button.Button(1640, 908,hunzwafü_img,1.06)
hundreivie_button = button.Button(1500, 748,hundreivie_img,1.08)
hunvievie_button = button.Button(1640, 828,hunvievie_img,1.08)
hunfüneu_button = button.Button(1640, 513,hunfüneu_img,1.08)
hunsibsib_button = button.Button(1640, 669,hunsibsib_img,1.08)
zweihunein_button = button.Button(1499, 591,zweihunein_img,1.08)
# solutions wider hard
# solutions strom hard
# solutions gemisch hard
# load or wright score 
Scores = scores.Scores()
# start parameters
clicked = False
running = True
menu_state ="start"
#gameloop
while running:
    screen.fill((0, 0, 0))
    bg_button.draw(screen)
# menu navigation
# main zu lern 
    if menu_state == "start":
            if start_button.draw(screen) and clicked == False:
                menu_state = "main"
                clicked = True
# main zu lern ueb spi
    if menu_state == "main":
            if lern_button.draw(screen) and clicked == False:
                menu_state = "lern"
                clicked = True
            if ueb_button.draw(screen) and clicked == False:
                menu_state = "spanwider"
                clicked = True
            if spi_button.draw(screen) and clicked == False:
                menu_state = "spielen"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
# lern zu geschichte formeln gefahren
    if menu_state == "lern":
            if ges_button.draw(screen) and clicked == False:
                menu_state = "geschichte"
                clicked = True
            if form_button.draw(screen) and clicked == False:
                menu_state = "formeln"
                clicked = True
            if gefabutton.draw(screen) and clicked == False:
                menu_state = "gefahren"
                clicked = True
            if zurü_button.draw(screen):
                menu_state = "main"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False   
# zu lernseite
    if menu_state == "geschichte":
            screen.blit(gesch1_img,(100,100))
            if zurü_button.draw(screen):
                menu_state = "lern" 
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "formeln":
            if zurü_button.draw(screen):
                menu_state = "lern" 
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "gefahren":
            if zurü_button.draw(screen):
                menu_state = "lern" 
            if exit_button.draw(screen)and clicked == False:
                running = False
# menu spannun widerstand stromstärke gemischt    
    if menu_state == "spanwider":
            if span_button.draw(screen) and clicked == False:
                menu_state = "spannung"
                clicked = True
            if wider_button.draw(screen) and clicked == False:
                menu_state = "widerstand"
                clicked = True
            if strom_button.draw(screen) and clicked == False:
                menu_state = "stromstärke"
                clicked = True
            if gemisch_button.draw(screen) and clicked == False:
                menu_state = "gemischt"
                clicked = True
            if zurü_button.draw(screen):
                menu_state = "main" 
            if exit_button.draw(screen)and clicked == False:
                running = False
#menu spannung zu level
    if menu_state == "spannung":
            if erklspan_button.draw(screen) and clicked == False:
                menu_state = "erklspan"
                clicked = True
            if leispan_button.draw(screen) and clicked == False:
                menu_state = "leichtspan"
                clicked = True
            if mitspan_button.draw(screen) and clicked == False:
                menu_state = "mittelspan"
                clicked = True
            if schwespan_button.draw(screen) and clicked == False:
                menu_state = "schwerspan"
                clicked = True
            if zurü_button.draw(screen):
                menu_state = "spanwider"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False  
    if menu_state == "widerstand":
            if erklwider_button.draw(screen) and clicked == False:
                menu_state = "erklwider"
                clicked = True
            if leiwider_button.draw(screen) and clicked == False:
                menu_state = "leichtwider"
                clicked = True
            if mitwider_button.draw(screen) and clicked == False:
                menu_state = "mittelwider"
                clicked = True
            if schwewider_button.draw(screen) and clicked == False:
                menu_state = "schwerwider"
                clicked = True
            if zurü_button.draw(screen):
                menu_state = "spanwider"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "stromstärke":
            if erklstrom_button.draw(screen) and clicked == False:
                menu_state = "erklstrom"
                clicked = True
            if leistrom_button.draw(screen) and clicked == False:
                menu_state = "leichtstrom"
                clicked = True
            if mitstrom_button.draw(screen) and clicked == False:
                menu_state = "mittelstrom"
                clicked = True
            if schwestrom_button.draw(screen) and clicked == False:
                menu_state = "schwerstrom"
                clicked = True
            if zurü_button.draw(screen):
                menu_state = "spanwider"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False   
    if menu_state == "gemischt":
            if erklgemisch_button.draw(screen) and clicked == False:
                menu_state = "erklgemisch"
                clicked = True
            if leigemisch_button.draw(screen) and clicked == False:
                menu_state = "leichtgemisch"
                clicked = True
            if mitgemisch_button.draw(screen) and clicked == False:
                menu_state = "mittelgemisch"
                clicked = True
            if schwegemisch_button.draw(screen) and clicked == False:
                menu_state = "schwergemisch"
                clicked = True
            if zurü_button.draw(screen):
                menu_state = "spanwider"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "erklspan":
            if zurü_button.draw(screen):
                menu_state = "spannung"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "leichtspan":
            if zurü_button.draw(screen):
                menu_state = "spannung"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "mittelspan":
            if zurü_button.draw(screen):
                menu_state = "spannung"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "schwerspan":
            if zurü_button.draw(screen):
                menu_state = "spannung"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "gemischtspan":
            if zurü_button.draw(screen):
                menu_state = "spannung"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "erklwiderleicht":
            if zurü_button.draw(screen):
                menu_state = "widerstand"
                clicked = True
            if exit_button.draw(screen)and clicked == False:
                running = False
    if menu_state == "leichtwider":
            screen.blit(WE1_img,(10,10))
            if  zwö_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            elif l220_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            elif weit_button.draw(screen):
                menu_state = "WE2"
            elif zurü_button.draw(screen):
                menu_state = "widerstand"
                clicked = True
            elif exit_button.draw(screen):
                running = False                
    if menu_state == "WE2":            
            screen.blit(WE2_img,(10,10))
            if  zwei_button.draw(screen) and clicked == False:
                screen.blit(richtig_img,(700,450))
                Scores.add_wider()
                pygame.display.update()
                pygame.time.wait(2000) 
            elif l220_button.draw(screen) and clicked == False:
                screen.blit(falsch_img,(700,449))
                Scores.add_widerwrong()
                pygame.display.update()
                pygame.time.wait(2000) 
            if weit_button.draw(screen):
                menu_state = "WE3"
            if zurü_button.draw(screen):
                menu_state = "leichtwider"
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
            elif l220_button.draw(screen) and clicked == False:
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
            elif l220_button.draw(screen) and clicked == False:
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
            elif l220_button.draw(screen) and clicked == False:
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
            elif l220_button.draw(screen) and clicked == False:
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
            elif l220_button.draw(screen) and clicked == False:
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
            elif l220_button.draw(screen) and clicked == False:
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
            elif l220_button.draw(screen) and clicked == False:
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
            elif l220_button.draw(screen) and clicked == False:
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
            elif l100200_button.draw(screen) and clicked == False:
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
            elif l100200_button.draw(screen) and clicked == False:
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
            elif l100200_button.draw(screen) and clicked == False:
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
            elif l100200_button.draw(screen) and clicked == False:
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
            elif l100200_button.draw(screen) and clicked == False:
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
            elif l100200_button.draw(screen) and clicked == False:
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
            elif l100200_button.draw(screen) and clicked == False:
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
            elif l100200_button.draw(screen) and clicked == False:
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
            elif l100200_button.draw(screen) and clicked == False:
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
            elif l100200_button.draw(screen) and clicked == False:
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
            elif lschwer_button.draw(screen) and clicked == False:
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
            elif lschwer_button.draw(screen) and clicked == False:
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
            elif lschwer_button.draw(screen) and clicked == False:
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
            elif lschwer_button.draw(screen) and clicked == False:
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
            elif lschwer_button.draw(screen) and clicked == False:
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
            elif lschwer_button.draw(screen) and clicked == False:
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
            elif lschwer_button.draw(screen) and clicked == False:
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
            elif lschwer_button.draw(screen) and clicked == False:
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
            elif lschwer_button.draw(screen) and clicked == False:
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
            elif lschwer_button.draw(screen) and clicked == False:
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
# update all images
    pygame.display.update()
# eventloop
# mousup check
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
             clicked = False
# close window x
        if event.type == pygame.QUIT:
            running = False
# close window esc           
        elif event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_ESCAPE:  # ESC zum Beenden
                running = False
pygame.quit()
sys.exit()
                
                




    