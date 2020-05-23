from PIL import Image 


path = input("please provide path to image") or 'child.jpg'
img = Image.open(path).convert("RGB")

width,height = img.size

pixels = img.load()


def red(r,g,b):
    newr = r
    newg = 0
    newb = 0
    return (newr,newg,newb)
def darkpink(r,g,b):
    newr = g
    newg = b
    newb = r
    return (newr,newg,newb)
def skyblue(r,g,b):
    newr = b
    newg = g
    newb = r
    return (newr,newg,newb)
def lemonyellow(r,g,b):
    newr = g
    newg = r
    newb = b
    return (newr,newg,newb)
def maroon(r,g,b):
    newr = r//2
    newg = 0
    newb = 0
    return (newr,newg,newb)
def grey(r,g,b):
    newr = (r+g+b)//3
    newg = (r+g+b)//3
    newb = (r+g+b)//3
    return (newr,newg,newb)
def lightgrey(r,g,b):
    newr = (r+g+b)//2
    newg = (r+g+b)//2
    newb = (r+g+b)//2
    return (newr,newg,newb)
def yellow(r,g,b):
    newr = r
    newg = g
    newb = 0
    return (newr,newg,newb)
def deep_pink(r,g,b):
    newr = r
    newg = int(g//12.75)
    newb = int(b//1.734)
    return (newr,newg,newb)
def chocolate(r,g,b):
    newr = int(r//1.21)
    newg = int(g//2.42)
    newb = int(b//8.5)
    return (newr,newg,newb)
def negative(r,g,b):
    newr = 255-r
    newg = 255-r
    newb = 255-r
    return (newr,newg,newb)
def B_W(r,g,b):
    avg = r+g+b//3
    if avg > 128:
        avg = 0
    else:
        avg = 255
    newr = avg
    newg = avg
    newb = avg
    return (newr,newg,newb)
def navy_blue(r,g,b):
    newr = 0
    newg = 0
    newb = b//2
    return (newr,newg,newb)
def sepia(r,g,b):
    newr = int((r * .393) + (g *.769) + (b * .189))
    newg = int((r * .349) + (g *.686) + (b * .168))
    newb = int((r * .272) + (g *.534) + (b * .131))
    return (newr,newg,newb)
choice = '''
enter you choice
1:red
2:darkpink
3:skybule
4:lemonyellow
5:grey
6:sepia
7:lightgrey
8:maroon
9:yellow
10:deep_pink
11:chocolate
12:navy_blue
13:negative
14:B_W
'''    
print(choice)
no = int(input())

for py in range(height):
    for px in range(width):
      r,g,b = img.getpixel((px,py))
      if no == 1:
          pixels[px,py] = red(r,g,b)
      elif no == 2:
          pixels[px,py] = darkpink(r,g,b)
      elif no == 3:
          pixels[px,py] = skyblue(r,g,b)
      elif no == 4:
          pixels[px,py] = lemonyellow(r,g,b)
      elif no == 5:
          pixels[px,py] = grey(r,g,b)
      elif no == 6:
          pixels[px,py] = sepia(r,g,b)
      elif no == 7:
          pixels[px,py] = lightgrey(r,g,b)
      elif no == 8:
          pixels[px,py] = maroon(r,g,b)
      elif no == 9:
          pixels[px,py] = yellow(r,g,b)
      elif no == 10:
          pixels[px,py] = deep_pink(r,g,b)
      elif no == 11:
          pixels[px,py] = chocolate(r,g,b)
      elif no == 12:
          pixels[px,py] = navy_blue(r,g,b)
      elif no == 13:
          pixels[px,py] = negative(r,g,b)
      elif no == 14:
          pixels[px,py] = B_W(r,g,b)
      else:
          pixels[px,py] = (r,g,b)



img.show()
img.save("newfilterimg.jpg")
