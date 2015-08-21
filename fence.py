#!/usr/bin/python
import os
import sys

def main(argv):

    # sirka plotu
    fenceWidth = 2440;
    # odsazeni od kraje
    fenceOffset = 42;
    # celkove odsazeni (dva okraje)
    fenceOffsets = fenceOffset * 2;
    # sirka late
    fenceBarWidth = 80;
    # vychozi sirka mezery
    fenceSpace = fenceBarWidth // 2;
    # sirka plotu bez celkoveho odsazeni
    fenceWidthReal = fenceWidth - fenceOffsets;
    # celkova sirka s mezerou
    fenceBarTotalWidth = fenceBarWidth + fenceSpace

    fenceBarDiv = 1
    fenceWidthTemp = 0;
    while fenceBarDiv != 0:
        fenceSpace = fenceSpace + 1;
        fenceBarCounter = fenceWidthReal // fenceBarTotalWidth;
        fenceBarDiv = fenceWidthReal % fenceBarTotalWidth;
        fenceBarTotalWidth = fenceBarWidth + fenceSpace;
        fenceWidthTemp = ((fenceBarWidth+fenceSpace)*fenceBarCounter);
        if fenceWidthTemp == fenceWidthReal:
            break;

    print ""
    print "Sirka plotu: %s mm" % (fenceWidth);
    print "Sirka bez okraju: %s mm" % (fenceWidthReal);
    print "Pocet lati o sirce %s mm: %s" % (fenceBarWidth, fenceBarCounter);
    print "Velikost mezery: %s mm" % (fenceSpace)
    print "%s = %s" % (fenceWidthReal, fenceWidthTemp)
    print ""

if __name__ == "__main__":
    main(sys.argv)
