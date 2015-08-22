#!/usr/bin/python
import os;
import sys;
import random, string;
from PIL import Image, ImageDraw, ImageFont;

def main(argv):

    # sirka plotu
    fenceWidth = 1925;
    # odsazeni od kraje
    fenceOffsetLeft = 37;
    fenceOffsetRight = 32;
    # celkove odsazeni (dva okraje)
    fenceOffsets = fenceOffsetLeft + fenceOffsetRight;
    # sirka plotu bez celkoveho odsazeni
    fenceWidthReal = fenceWidth - fenceOffsets;
    # sirka late
    fenceBarWidth = 80;
    # vychozi sirka mezery
    fenceBarSpace = 30;
    # celkova sirka s mezerou
    fenceBarTotalWidth = fenceBarWidth + fenceBarSpace;
    fenceBarSpaceTemp = 1;

    # -------------------------------------------------------------------------

    def salt():
       return ''.join(random.choice(string.lowercase) for i in range(3))

    def createPicture(pFenceBarSpace, pCounter, pTextResult):
        imageWidth = fenceWidth;
        imageHeight = 400;
        imageHeightHalf = imageHeight // 2;
        imageBg = (255, 255, 255, 255);

        im = Image.new(
            'RGBA',
            (imageWidth, imageHeight),
            imageBg
        );

        font = ImageFont.truetype("mono.ttf", 16)
        font2 = ImageFont.truetype("mono.ttf", 32)

        draw = ImageDraw.Draw(im)
        draw.line((0,imageHeight//2, imageWidth,imageHeight//2), fill="black", width=3)

        # levy offset plotu
        draw.rectangle(
            (
                (0, imageHeightHalf-20),
                (fenceOffsetLeft, imageHeightHalf+20)
            ),
            fill="silver"
        );
        draw.text((5, imageHeightHalf-40),str(fenceOffsetLeft),(0,0,0),font=font)

        # pravy offset plotu
        draw.rectangle(
            (
                (imageWidth-fenceOffsetRight, imageHeightHalf-20),
                (imageWidth, imageHeightHalf+20)
            ),
            fill="silver"
        );
        draw.text((imageWidth-fenceOffsetRight+5, imageHeightHalf-40),str(fenceOffsetRight),(0,0,0),font=font)

        # vykresleni lati
        for i in range(0, pCounter):
            barOffset = fenceOffsetLeft + (fenceBarWidth * i) + (pFenceBarSpace * i);
            draw.rectangle(
                (
                    (barOffset, imageHeightHalf-100),
                    (barOffset + fenceBarWidth, imageHeightHalf+100)
                ),
                fill=(0,0,0),
                outline = "black"
            );
            # rozmer late
            draw.text((barOffset+5, imageHeightHalf-120),str(fenceBarWidth),(0,0,0),font=font)
            # cislo late
            draw.text((barOffset+20, imageHeightHalf-16),str(i+1),(255,255,255),font=font2)
            if( i != (pCounter-1) ):
                # rozmer mezery
                draw.text((barOffset+fenceBarWidth+5, imageHeightHalf-20),str(pFenceBarSpace),(0,0,0),font=font)

        # textovy vysledek
        draw.text((10, 10),str(pTextResult),(0,0,0),font=font2)

        fileName = "output/fence-%s.png" % salt();
        im.save(fileName);

    while True:
        fenceBarSpaceTemp = 0;
        fenceBarSpace = fenceBarSpace + 1;
        for i in range(1,26):
            fenceBarSpaceTemp = (fenceBarWidth * i) + (fenceBarSpace * (i-1));
            if( fenceBarSpaceTemp == fenceWidthReal ):
                textResult = "Sirce plotu %smm s okrajema %smm a %smm odpovida %s lati o sirce %smm s mezerou %smm." % (fenceWidth, fenceOffsetLeft, fenceOffsetRight, i, fenceBarWidth, fenceBarSpace);
                print textResult;
                createPicture(fenceBarSpace, i, textResult);
        if fenceBarSpace > fenceBarWidth:
            break;

if __name__ == "__main__":
    main(sys.argv)
