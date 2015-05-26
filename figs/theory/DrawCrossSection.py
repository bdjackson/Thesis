#!/usr/bin/env python

import sys
import os.path
import optparse
import time
import array

import ROOT
import rootlogon

f = file('xsec_stop.txt')

mass_list = []
xsec_list = []
xunc_list = []

for l in f.readlines():
    l = l.rstrip('\n')
    print l
    splits = l.split()
    print splits
    mass_list.append(float(splits[0]))
    xsec_list.append(float(splits[1]))
    xunc_list.append(xsec_list[-1]*float(splits[2])/100.)

g = ROOT.TGraphErrors( len(mass_list)
                     , array.array('d', mass_list)
                     , array.array('d', xsec_list)
                     , array.array('d', [0]*len(mass_list))
                     , array.array('d', xunc_list)
                     )
g.SetLineColor(ROOT.kBlue+2)
g.SetFillColor(ROOT.kBlue-4)

g.SetLineWidth(3)
g.SetFillStyle(3002)

c = ROOT.TCanvas('c1')
c.SetLogy()

g.Draw("AP")

g.GetHistogram().SetMaximum(max(xsec_list)*100)
g.GetHistogram().SetMinimum(min(xsec_list)/100)
g.GetHistogram().GetXaxis().SetTitle('m(#tilde{t}) [GeV]')
g.GetHistogram().GetYaxis().SetTitle('#sigma(p p #rightarrow #tilde{t} #tilde{t}*) [pb]')

g.Draw("A4")
g.Draw("LX")

# c.Print("xsec.eps")
# c.Print("xsec.png")
c.Print("xsec.pdf")
