
def thumbnail(filename, size='104x104', x2=False):
    # defining the size
    x, y = [int(x) for x in size.split('x')]
    # defining the filename and the miniature filename
    filehead, filetail = os.path.split(filename)
    basename, format = os.path.splitext(filetail)
    miniature = basename + '_' + size + format
    if x2:
        miniature = basename + '_' + size + '@2x' + format
    miniature_filename = os.path.join(filehead, miniature)

    if os.path.exists(miniature_filename) and \
            os.path.getmtime(filename) > os.path.getmtime(miniature_filename):
        os.unlink(miniature_filename)
        # if the image wasn't already resized, resize it
    if not os.path.exists(miniature_filename):
        image = Image.open(filename)
        image.thumbnail([x, y], Image.ANTIALIAS)
        try:
            image.save(miniature_filename, image.format, quality=90, optimize=1)
        except:
            image.save(miniature_filename, image.format, quality=90)

    return miniature_filename
 
