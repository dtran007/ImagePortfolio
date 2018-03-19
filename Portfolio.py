#Image Portfolio

#Rose-colored glasses ############################################################################
def roseColoredGlasses():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    pink_it = makeColor(r*0.85, g*0.45, b*0.45)
    setColor(p, pink_it)
  repaint(pic)
  writePictureTo(pic, '/home/wave/Desktop/Portfolio/roseColoredGlassesOutput.jpg')
  return(pic)

###################################################################################################  


 
#Negative #########################################################################################
def makeNegative():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    red = getRed(p)
    blue = getBlue(p)
    green = getGreen(p)
    negativeColor = makeColor(255-red, 255-green, 255-blue)
    setColor(p, negativeColor)
  repaint(pic)
  writePictureTo(pic, '/home/wave/Desktop/Portfolio/makeNegativeOutput.jpg')
  return(pic)


#################################################################################################

#Better black and white #########################################################################
def betterBnW():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    redP = getRed(p)
    blueP = getBlue(p)
    greenP = getGreen(p)
    averageP = redP*0.299 + greenP*0.587 + blueP*0.114
    makeGrey = makeColor(averageP, averageP, averageP)
    setColor(p, makeGrey)
  repaint(pic)
  writePictureTo(pic, '/home/wave/Desktop/Portfolio/betterBnWOutput.jpg')
  return(pic)

##################################################################################################


#Bottom-to-top mirror ##########################################################################
def bottomToTop():
  file = pickAFile()
  pic = makePicture(file)
  width = getWidth(pic)
  height = getHeight(pic)
  canvas = makeEmptyPicture(width, height)
  for x in range(0, width):
    for y in range(height/2, height):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(canvas, x, y), color)
      setColor(getPixel(canvas, x, height-y-1), color)
  show(canvas)
  writePictureTo(canvas, '/home/wave/Desktop/Portfolio/bottomToTop.jpg')
  return canvas   


###################################################################################################


#Shrink ###########################################################################################
def shrink():
  file = pickAFile()
  pic = makePicture(file)
  width = getWidth(pic)
  height = getHeight(pic)
  canvas = makeEmptyPicture(width/2, height/2) #half size
  for x in range(0, width/2):
    for y in range(0, height/2):
      pxCan = getPixel(canvas, x, y)
      #the canvas
      for i in range(x*2, x*2 + 2):
        for j in range(y*2, y*2 + 2):
          pxSrc = getPixel(pic, i, j)
          setColor(pxCan, getColor(pxSrc))      
  show(canvas)
  writePictureTo(canvas, '/home/wave/Desktop/Portfolio/shrink.jpg')
  return canvas

#Collage #####################################################################################
#Vertical Mirror
def verticalMirror(file):
  #file = pickAFile()
  #pic = makePicture(file)
  pic = file
  width = getWidth(pic)
  height = getHeight(pic)
  canvas = makeEmptyPicture(width, height)
  for x in range(0, width/2):
    for y in range(0, height):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(canvas, x, y), color)
      setColor(getPixel(canvas, width-x-1, y), color)
  #show(pic)
  #show(canvas)
  writePictureTo(canvas, '/home/wave/Desktop/CST205Lab5/DogeMirror.jpg')
  return canvas
  


def rotatePic(file):
  #file = pickAFile()
  #pic = makePicture(file)
  pic = file
  width = getWidth(pic)
  height = getHeight(pic)
  canvas = makeEmptyPicture(height, width) #swap values
  for y in range(0, height):
    for x in range(0, width):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(canvas, y, x), color) #swap x, y
  #show(pic)
  #show(canvas)
  return canvas


#Problem #1 Sepia 
def Sepia(file):
  #filename = pickAFile()
  #pic = makePicture(filename)
  #show(pic) #just showing original //comment out after
  pic = file
  pixels = getPixels(pic)
  for p in pixels:
    redP = getRed(p)
    blueP = getBlue(p)
    greenP = getGreen(p)
    averageP = (redP + blueP + greenP) / 3
    makeGrey = makeColor(averageP, averageP, averageP)
    setColor(p, makeGrey)
  xpixels = getPixels(pic) 
  for x in xpixels:
    xredP = getRed(x)
    xblueP = getBlue(x)
    xgreenP = getGreen(x)  
    if xredP < 63:
      xredP = xredP * 1.1
      blueP = xblueP * 1.1
    elif 62 < xredP < 192: 
      xredP = xredP * 1.15
      blueP = xblueP * 0.85
    elif xredP > 191:
      if xredP > 255:
        xredP = 255
      xredP = xredP * 1.08
      xblueP = xblueP * 0.93
      
    makeColour = makeColor(xredP, xgreenP, xblueP)
    setColor(x, makeColour)
  #repaint(pic)
  writePictureTo(pic, '/home/wave/Desktop/CST205Lab5/tokyoSepia.jpg')
  return(pic)



def Artify(file):
  #filename = pickAFile()
  pic = file
  #show(pic) #just showing original //comment out after
  
  pixels = getPixels(pic)
  for p in pixels:
    redP = getRed(p)
    blueP = getBlue(p)
    greenP = getGreen(p)
    
    if redP < 64:
      redP = 31
    elif 63 < redP < 128:
      redP = 95
    elif 127 < redP < 192:
      redP = 159
    elif 191 < blueP < 256:
      redP = 223
      
    if blueP < 64:
      blueP = 31
    elif 63 < redP < 128:
      blueP = 95
    elif 127 < redP < 192:
      blueP = 159
    elif 191 < blueP < 256:
      blueP = 223

    if greenP < 64:
      greenP = 31
    elif 63 < redP < 128:
      greenP = 95
    elif 127 < redP < 192:
      greenP = 159
    elif 191 < greenP < 256:
      greenP = 223
      
    newColour = makeColor(redP, greenP, blueP)
    setColor(p, newColour)
  repaint(pic)
  writePictureTo(pic, '/home/wave/Desktop/CST205Lab5/GroupphotoArtify.jpg')
  return(pic)


def pyCopy(source, target, targetX, targetY): #Removed pickAFile() bc source should be provided in functioncall
  #pic = makePicture(source)  #input course should be file directory path
  #above is commented out so that source is now a makepicture that way use functions that pipe into pyCopy
  pic = source
  pwidth = getWidth(pic)
  pheight = getHeight(pic)
  #This function does not do anything to canvas size, that warmup function did
  
  for x in range(0, pwidth):
    for y in range(0, pheight):
      colorSource = getColor(getPixel(pic, x, y)) #get color pixel of source
      targetPixel = getPixel(target, x+targetX, y+targetY) #target pixel
      setColor(targetPixel, colorSource)
      
  


#kept getting an Error:
#The error was: GC overhead limit exceeded
#A python OutofMemoryError happened while running your program, so it stopped. 
#I think my computer can't run the big process so had to break down into smaller function... 
#modify images in separate function then run makeCollage

#resolved error by using these below functions first before running makeCollage()

def makeDoge():
  pic = makePicture('/home/wave/Desktop/CST205Lab5/Doge.jpg')
  verticalMirror(pic)
  
def makeGroupArtify():
  pic = makePicture('/home/wave/Desktop/CST205Lab5/Groupphoto.jpg')
  Artify(pic)
  
def maketokyoSepia():
  pic = makePicture('/home/wave/Desktop/CST205Lab5/tokyo.jpg')
  Sepia(pic)



def makeCollage():
  #create canvas that is 8.5 x 11
  cwidth = 2550
  cheight = 3300
  canvas = makeEmptyPicture(cwidth, cheight)
  
  pic1 = makePicture('/home/wave/Desktop/CST205Lab5/autumn.jpg') #1920/1080
  pyCopy(pic1, canvas, 0, 0)
  
  #used rotation modification
  #taking rotatePic function as parameter worked
  pic5 = makePicture('/home/wave/Desktop/CST205Lab5/clover.jpg') #
  pyCopy(rotatePic(pic5), canvas, 0, 1081)
  
  #used rotation modification
  #taking rotatePic function worked
  pic6 = makePicture('/home/wave/Desktop/CST205Lab5/tigerOriginal.jpg')
  pyCopy(rotatePic(pic6), canvas, 1350, 0)
  
  pic3 = makePicture('/home/wave/Desktop/CST205Lab5/lake.jpg') #1920/1080
  pyCopy(pic3, canvas, 630, 2220)
  
  pic4 = makePicture('/home/wave/Desktop/CST205Lab5/cherryblossom.jpg') #1680/1260
  pyCopy(pic4, canvas, 870, 960)
  
  #used sephia
  #ran out of memory so called separate function above to create mod image first
  pic2 = makePicture('/home/wave/Desktop/CST205Lab5/GroupphotoArtify.jpg') #1024/768
  pyCopy(pic2, canvas, 0, 2532)
  
  #Vertical mirror modification
  #also had to use separate function first
  pic7 = makePicture('/home/wave/Desktop/CST205Lab5/DogeMirror.jpg')
  pyCopy(pic7, canvas, 500, 1000)
  
  #Sephia modification to image
  #also had to use separate function first
  pic8 = makePicture('/home/wave/Desktop/CST205Lab5/tokyoSepia.jpg')
  pyCopy(pic8, canvas, 1000, 1800)
  
  #show(canvas)
  writePictureTo(canvas, '/home/wave/Desktop/CST205Lab5/Lab5Collage.jpg') 
  return(canvas)

#####################################################################################################


#Red-eye Reduction ############################################################################
def getRegions(): 
#setting red region
  return [[358,526],[379,548],[592,526],[618,548]]
  
def getDistanceFromBase(pixel, baseColor):
  col = getColor(pixel)
  return distance(baseColor, col)

def redEye():
   file = pickAFile()
   pic = makePicture(file)
   #making the red color
   baseColor =  makeColor(218, 69, 96)
   regions = getRegions() 
   pixelsArray = []

   for y in range (regions[0][1],regions[1][1]):
     for x in range (regions[0][0],regions[1][0]):
       p=getPixelAt(pic,x,y)
       cred = getDistanceFromBase(p,baseColor)
       if cred <80:
         pixelsArray.append(p)
     for x in range (regions[2][0],regions[3][0]):
         p=getPixelAt(pic,x,y)
         cred = getDistanceFromBase(p,baseColor)
         if cred <80:
           pixelsArray.append(p)
   #repaint(pic)
   for pixel in pixelsArray:
     newColor = makeColor(0, getGreen( pixel ), getBlue( pixel )) 
     setColor( pixel, newColor)
   repaint(pic)
   writePictureTo(pic, '/home/wave/Desktop/Portfolio/RedEyeOutput.jpg')
   return(pic)

####################################################################################

#Color Art-i-fy #####################################################################
def Artify():
  filename = pickAFile()
  pic = makePicture(filename)
  #show(pic) #just showing original //comment out after
  pixels = getPixels(pic)
  for p in pixels:
    redP = getRed(p)
    blueP = getBlue(p)
    greenP = getGreen(p)
    #Posertization
    #Each color will be changed within specific range
    
    #Red Pixel
    if redP < 64:
      redP = 31
    elif 63 < redP < 128:
      redP = 95
    elif 127 < redP < 192:
      redP = 159
    elif 191 < redP < 256:
      redP = 223
    
    #Blue Pixel
    if blueP < 64:
      blueP = 31
    elif 63 < blueP < 128:
      blueP = 95
    elif 127 < blueP < 192:
      blueP = 159
    elif 191 < blueP < 256:
      blueP = 223
    #Green Pixel
    if greenP < 64:
      greenP = 31
    elif 63 < greenP < 128:
      greenP = 95
    elif 127 < greenP < 192:
      greenP = 159
    elif 191 < greenP < 256:
      greenP = 223
      
    newColour = makeColor(redP, greenP, blueP)
    setColor(p, newColour)
  repaint(pic)
  writePictureTo(pic, '/home/wave/Desktop/Portfolio/ArtifyOutput.jpg')
  return(pic)
  
####################################################################################

#Green screen ######################################################################
def chromaKey():
  #choose background img
  fileBack = pickAFile()
  picBack = makePicture(fileBack)
  #choose greenscreen img
  fileGreen = pickAFile()
  picGreen = makePicture(fileGreen)
  #get pixels in green screen img
  pixels = getPixels(picGreen)
  #check for same img dimensions
  if getWidth(picGreen) != getWidth(picBack):
    print("Unequal Widths")   
  elif getHeight(picGreen) != getHeight(picBack):
    print("Unequal Heights")
  else:
    for p in pixels:
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      #looking for green pixels in greenscreen
      if (r<90 and g>140 and b<85):
        x=getX(p)
        y=getY(p)
        P=getPixelAt(picBack,x,y)
        #replace greenscreen pixel with background pixels
        setColor(p,getColor(P))
      elif (r<120 and g>30 and b<120 and (abs(r-b)<51) and ((r+b/2)<(g-20))):
        newGreen = float(r+b+g)/3 #toned down green
        x=getX(p)
        y=getY(p)
        P=getPixelAt(picBack,x,y)#Get background pixel color        
        R = getRed(P)
        G = getGreen(P)
        B = getBlue(P)
        proportion = float(g)/90 - float(5)/9 #blending proportion
        R = int(float(R)*proportion + r*(1-proportion))#blending colors
        G = int(float(G)*proportion + newGreen*(1-proportion))
        B = int(float(B)*proportion + b*(1-proportion)) 
        c = makeColor(R,G,B)
        setColor(p,c)
    repaint(picGreen)
    writePictureTo(picGreen, '/home/wave/Desktop/Portfolio/chromaKeyOutput.jpg')
    return(picGreen)   

###################################################################################

#Home made Thanksgiving #############################################################
def getDimantions(pic):
  return getWidth(pic),getHeight(pic)

def errorMSG(pic,txt):
    w,h = getDimantions(pic)
    c = makeColor(255, 0, 0)
    s = makeStyle(sansSerif, bold, 30)
    addTextWithStyle(pic, (w//2), h//2, txt, s, c)
    return pic


def txtMSG(pic,txt_1,txt_2):
    w,h = getDimantions(pic)
    c = makeColor(0, 255, 0)
    s = makeStyle(sansSerif, bold, 30)
    addTextWithStyle(pic, (w//2)-150, h//2, txt_1, s, c)
    addTextWithStyle(pic, (w//2)-100, (h//2)+30, txt_2, s, c)
    return pic
    
def getDistanceFromBase(pixel, baseColor):
  col = getColor(pixel)
  return distance(baseColor, col)

def chromakey (source, backGround, coordX, coordY): 
  sourceW,sourceH = getDimantions(source)
  bgW,bgH = getDimantions(backGround)
  if (sourceW+coordX)>=bgW or (sourceH+coordY)>bgH :
    return errorMSG(source,"YELL NO")
  for x in range (0, bgW):
   for y in range (0, bgH):
    if x>=coordX and x<(sourceW+coordX) and y>=coordY and y<(sourceH+coordY):
     picPixel=getPixelAt(backGround,x,y)
     pixelX=x-coordX
     pixelY=y-coordY
     pixel = getPixelAt(source,pixelX,pixelY)
     pixelR = getRed(pixel)
     pixelG = getGreen(pixel)
     pixelB = getBlue(pixel)
     if (pixelR<80 and pixelG>120 and pixelB<75):
        px=""
     elif (pixelR<120 and pixelG>30 and pixelB<120 and (abs(pixelR-pixelB)<51) and ((pixelR+pixelB/2)<(pixelG-20))):
       newGreen = float(pixelR+pixelG+pixelB)/3 #toned down green
       pX=getX(picPixel)
       pY=getY(picPixel)
       picPixel=getPixelAt(backGround,pX,pY)#Get background pixle color        
       picR = getRed(picPixel)
       picG = getGreen(picPixel)
       picB = getBlue(picPixel)
       proportion = float(pixelG)/220 - float(5)/9 #blending proportion
       pixelR = int(float(picR)*proportion + pixelR*(1-proportion))#blending colors
       pixelG = int(float(picG)*proportion + newGreen*(1-proportion))
       pixelB = int(float(picB)*proportion + pixelB*(1-proportion)) 
       colorPixel = makeColor(pixelR,pixelB,pixelG)
       setColor(picPixel,colorPixel)
     else:
       colorPixel = getColor(pixel)
       setColor(picPixel,colorPixel)
  return backGround
  
def Run():
  pic = makePicture('/home/wave/Desktop/Portfolio/johnny_walker_logo_bwv.jpg')
  bg = makePicture('/home/wave/Desktop/Portfolio/JWG.jpg')
  bg = chromakey (pic,bg,298,19)
  pic = makePicture('/home/wave/Desktop/Portfolio/SPD.jpg')
  Card = chromakey (pic,bg,500,320)
  Card=txtMSG(Card,"Make sure you keep walking","this St. Patrick`s Day")
  writePictureTo(Card,'/home/wave/Desktop/Portfolio/spdCard.jpg')
  show(Card)
  
############################################################################################################
  
#Advanced Image Processing Technique  ######################################################################
def advance():
  file = pickAFile()
  pic = makePicture(file)
  #make pic into black and white image
  pixels = getPixels(pic)
  for p in pixels:
    redP = getRed(p)
    blueP = getBlue(p)
    greenP = getGreen(p)
    averageP = redP*0.299 + greenP*0.587 + blueP*0.114
    makeGrey = makeColor(averageP, averageP, averageP)
    setColor(p, makeGrey)


  width = getWidth(pic)
  height = getHeight(pic)
   
  for x in range(0, width-1):
    for y in range(0, height-1):
      currentPixel = getPixel(pic, x, y)
      belowPixel = getPixel(pic, x, y+1)
      rightPixel = getPixel(pic, x+1, y)
      
      #luminescence 
      currentPixelLum = (getRed(currentPixel) + getGreen(currentPixel) + getBlue(currentPixel))/3
      belowPixelLum = (getRed(belowPixel) + getGreen(belowPixel) + getBlue(belowPixel))/3
      rightPixelLum = (getRed(rightPixel) + getGreen(rightPixel) + getBlue(rightPixel))/3
  
      #from trying various differenceValues, increasing number resulted in less filled in black pixels and vice versa
      differenceValue = 5
      if( abs(currentPixelLum - belowPixelLum) > differenceValue and abs(currentPixelLum - rightPixelLum) > differenceValue):
        setColor(currentPixel, black)

      if( abs(currentPixelLum - belowPixelLum) <= differenceValue and abs(currentPixelLum - rightPixelLum) <= differenceValue):
        setColor(currentPixel, white) 
          
  show(pic)
  writePictureTo(pic, '/home/wave/Desktop/Portfolio/advanceOutput.jpg')
  return pic

##################################################################################################
