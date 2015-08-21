#!/usr/bin/python
import os
import sys

def main(argv):

    # sirka plotu
    fenceWidth = 2450;
    # odsazeni od kraje
    fenceOffsetLeft = 30;
    fenceOffsetRight = 30;
    # celkove odsazeni (dva okraje)
    fenceOffsets = fenceOffsetLeft + fenceOffsetRight;
    # sirka plotu bez celkoveho odsazeni
    fenceWidthReal = fenceWidth - fenceOffsets;
    # sirka late
    fenceBarWidth = 78;
    # vychozi sirka mezery
    fenceBarSpace = 30;
    # celkova sirka s mezerou
    fenceBarTotalWidth = fenceBarWidth + fenceBarSpace;
    fenceBarSpaceTemp = 1;

    while True:
        fenceBarSpaceTemp = 0;
        fenceBarSpace = fenceBarSpace + 1;
        for i in range(1,26):
            fenceBarSpaceTemp = (fenceBarWidth * i) + (fenceBarSpace * (i-1));
            if( fenceBarSpaceTemp == fenceWidthReal ):
                print "Sirce plotu %smm s okrajema %smm a %smm odpovida %s lati o sirce %smm s mezerou %smm." % (fenceWidth, fenceOffsetLeft, fenceOffsetRight, i, fenceBarWidth, fenceBarSpace);
        if fenceBarSpace > fenceBarWidth:
            break;

if __name__ == "__main__":
    main(sys.argv)
