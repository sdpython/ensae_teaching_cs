"""panorama avec images"""
import pygame
import os
import time
from PIL import Image
import random

def attendre_touche () :
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP : return "clic"
        elif event.type == pygame.KEYDOWN : 
            if event.key == 275 : return "right"
            elif event.key == 276 : return "left"
            elif event.key == 273 : return "up"
            elif event.key == 274 : return "down"
            elif event.key == 27 : return "quit"
            elif event.key == 32 : return "pause"
            else :
                pass
                #print "key ", event.key
        else :
            #print event
            pass
    return ""
       

def get_image_list (dir = ".") :
    li = os.listdir (dir)
    res = []
    for l in li :
        s = l.lower ()
        if "jpg" in s or "png" in s or "jpeg" in s :
            res.append (l)
    res.sort ()
    return res
    
def image_resize (im, size, pil = True) :
    s = im.get_size ()
    rapx = float (size [0]) / s [0]
    rapy = float (size [1]) / s [1]
    
    rap = min (rapx, rapy)
    rap = min (rap, 2.0)
    
    size2 = ( int (s [0] * rap), int (s [1] * rap) )
    
    if not pil :
        res = pygame.transform.scale (im, size2)
    else :
        # scale from pygame is not good, use PIL's one
        s = pygame.image.tostring (im, "RGBX")
        temp = Image.fromstring ("RGBX", im.get_size (), s)
        tu = (0,0, im.get_size () [0]-1, im.get_size () [1] - 1)
        temp = temp.transform (size2, Image.EXTENT,  tu, Image.BICUBIC)
        mode = temp.mode
        size = temp.size
        data = temp.tostring()
        res = pygame.image.fromstring (data, size, mode)    
    return res
    
def load_image (file) :
    try :
        im = pygame.image.load (file)
    except Exception, e :
        print "unable to load image ", file, " error ", e
        return None
    return im
    
def display (sur, im) :
    im = image_resize (im, sur.get_size ())
    sur.fill ( (0,0,0) )
    
    x = (sur.get_size () [0] - im.get_size () [0]) / 2
    y = (sur.get_size () [1] - im.get_size () [1]) / 2
    
    sur.blit (im, (x,y))
    
def loop (sur, li, d = 500, rnd = True, transition = True) :
    
    already = { }
    for i in range (0, len (li)) : already [i] = - len (li) 
    
    print "number of images ", len (li)
    lo = 0
    i = 0
    while i < len (li) or rnd :
        
        lo += 1
        if rnd : 
            i = random.randint (0, len (li)-1)
            while lo - already [i]  < len (li) / 2 :
                i = random.randint (0, len (li)-1)
        im = li [i]
        already [i] = lo
        
        
        ti = pygame.time.get_ticks ()
        
        s = load_image (im)
        if s == None : continue
            
        display (sur, s)
        
        if not transition :
            pygame.display.flip ()
        else :
            ts = sur.get_size ()
            for i in xrange (0, ts [0], 20) :
                r = pygame.Rect (i, 0, i+100, ts [1])
                pygame.display.update (r)
                pygame.time.delay (10)
        
        
        ti = ti - pygame.time.get_ticks ()
        
        ti = max (0, d - ti)
        pygame.time.delay (ti)
        
        if pygame.event.peek () :
            t = attendre_touche ()
            if t == "quit" : return 
            elif t == "left" : i -= 1
            elif t == "right" : i += 1
            elif t == "up" : i += 10
            elif t == "down" : i += 10
            elif t == "pause" :
                while attendre_touche () != "pause" :
                    pass
        i += 1
        i = max (i, 0)
        
    print "stop at ", i
            
    
if __name__ == "__main__" :
    li = get_image_list ()
    
    pygame.init ()
    pygame.display.set_mode ((1280,800), pygame.FULLSCREEN)
    #pygame.display.set_mode ((1280,800)) #, pygame.FULLSCREEN)
    s = pygame.display.get_surface ()
    
    loop (s, li)

    pygame.time.delay (1000)