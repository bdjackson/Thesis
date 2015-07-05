from collections import OrderedDict

regions = OrderedDict([('CR_TOP_v2','top CR'), ('CR_Z_v2','Z CR'),
                       ('VR_TOP_1_v2','top VR 1'), ('VR_TOP_2_v2','top VR 2'),
                       ('VR_TOP_3_v2','top VR 3'), ('VR_Z_v2','Z VR')])
# , 'CR_Z':'Z CR', 'VR_TOP_1':'top VR 1',
#            'VR_TOP_2':'top VR 2', 'VR_TOP_2':'top VR 2', 'VR_Z':'Z VR'}
histograms = OrderedDict([('mbl_0', 'Leading \\Mbl'),
                          # ('mbl_1', 'Sub-leading \\Mbl'),
                          ('ht_signal', '\\Ht'),
                          ('mbl_asym', '\\MblAsym'),
                          ('met_sig_signal', '\\MetSig'),
                          ('mll', '$m_{\\ell\\ell}$'),
                          ('mll_detailed', '$m_{\\ell\\ell}$'),
                          ('lep_pt_detailed_0', 'Leading lepton $p_\mathrm{T}$'),
                          ('lep_pt_detailed_1', 'Sub-leading lepton $p_\mathrm{T}$'),
                          # (#lep_eta_0', 'Leading lepton $\eta$'),
                          # ('lep_eta_1', 'Sub-leading lepton $\eta$'),
                          ('b_jet_pt_detailed_0', 'Leading b jet $p_\mathrm{T}$'),
                          ('b_jet_pt_detailed_1', 'Sub-leading b jet $p_\mathrm{T}$'),
                          # ('b_jet_eta_0', 'Leading b jet $\eta$'),
                          # ('b_jet_eta_1', 'Sub-leading b jet $\eta$'),
                          # ('mbb', '$m_{bb}$'),
                          # ('ptll', '$p_\mathrm{T}^{\\ell\\ell}$'),
                          # ('ptbb', '$p_\mathrm{T}^{bb}$'),
                          ])

# ------------------------------------------------------------------------------
def writeFirstPart(f):
    f.write('''
% ------------------------------------------------------------------------------
\\newcommand{\\RegionTitle}{XXX}
\\newcommand{\\Region}{XXX}
\\newcommand{\\PlotTitle}{XXX}
\\newcommand{\\PlotName}{XXX}
\\newcommand{\\LinLog}{lin}


''')




# ------------------------------------------------------------------------------
def writeRegionTitleSlide(f, region_name):
    f.write('% ------------------------------------------------------------------------------\n')
    f.write('\\frame\n')
    f.write('{\n')
    f.write('\\begin{center}\n')
    f.write('\\Huge %s\n' % regions[region_name])
    f.write('\\end{center}\n')
    f.write('}\n\n\n')


# ------------------------------------------------------------------------------
def writeFourFigureSlide(f, hist_name, region_name, lin_log = 'lin'):
    f.write('% ------------------------------------------------------------------------------\n')
    f.write('\\renewcommand{\\RegionTitle}{%s}\n' % regions[region_name])
    f.write('\\renewcommand{\\Region}{%s}\n' % region_name)
    f.write('\\renewcommand{\\PlotTitle}{%s}\n' % histograms[hist_name])
    f.write('\\renewcommand{\\PlotName}{%s}\n' % hist_name)
    f.write('\\renewcommand{\\LinLog}{%s}\n' % lin_log)
    f.write('''\\frame
{
  \\frametitle{\\PlotTitle\\,in \\RegionTitle}
''')
    # discussion(f, hist_name, region_name)
    f.write('''
  \\begin{columns}
    \\column{0.32\\textwidth}
    \\begin{block}{All flavor channels}
      \\begin{tikzpicture}
        \\node[anchor=south west, inner sep=0] (image) at (0,0) {
          \\includegraphics[height=0.28\\textheight]{figures/BMINUSL_\\Region/flavor_all__\\PlotName__BMINUSL_\\Region__\\LinLog.pdf}};
          % \\begin{scope}[x={(image.south east)}, y={(image.north west)}]
          %   \\draw[red, ultra thick, rounded corners] (0.25, 0.08) rectangle (0.45, 0.26);

          %   % \\draw[help lines,xstep=.1,ystep=.1] (0,0) grid (1,1);
          %   % \\foreach \\x in {0,1,...,9} { \\node [anchor=north] at (\\x/10,0) {0.\\x}; }
          %   % \\foreach \\y in {0,1,...,9} { \\node [anchor=east] at (0,\\y/10) {0.\\y}; }

          % \\end{scope}
      \\end{tikzpicture}
    \\end{block}
    \\begin{block}{$ee$}
      \\begin{tikzpicture}
        \\node[anchor=south west, inner sep=0] (image) at (0,0) {
          \\includegraphics[height=0.28\\textheight]{figures/BMINUSL_\\Region/flavor_ee__\\PlotName__BMINUSL_\\Region__\\LinLog.pdf}};
          % \\begin{scope}[x={(image.south east)}, y={(image.north west)}]
          %   \\draw[red, ultra thick, rounded corners] (0.25, 0.08) rectangle (0.45, 0.26);

          %   % \\draw[help lines,xstep=.1,ystep=.1] (0,0) grid (1,1);
          %   % \\foreach \\x in {0,1,...,9} { \\node [anchor=north] at (\\x/10,0) {0.\\x}; }
          %   % \\foreach \\y in {0,1,...,9} { \\node [anchor=east] at (0,\\y/10) {0.\\y}; }

          % \\end{scope}
      \\end{tikzpicture}
    \\end{block}

    \\column{0.32\\textwidth}
    \\begin{block}{$e\\mu$}
      \\begin{tikzpicture}
        \\node[anchor=south west, inner sep=0] (image) at (0,0) {
          \\includegraphics[height=0.28\\textheight]{figures/BMINUSL_\\Region/flavor_em__\\PlotName__BMINUSL_\\Region__\\LinLog.pdf}};
          % \\begin{scope}[x={(image.south east)}, y={(image.north west)}]
          %   \\draw[red, ultra thick, rounded corners] (0.25, 0.08) rectangle (0.45, 0.26);

          %   % \\draw[help lines,xstep=.1,ystep=.1] (0,0) grid (1,1);
          %   % \\foreach \\x in {0,1,...,9} { \\node [anchor=north] at (\\x/10,0) {0.\\x}; }
          %   % \\foreach \\y in {0,1,...,9} { \\node [anchor=east] at (0,\\y/10) {0.\\y}; }

          % \\end{scope}
      \\end{tikzpicture}
    \\end{block}
    \\begin{block}{$\\mu\\mu$}
      \\begin{tikzpicture}
        \\node[anchor=south west, inner sep=0] (image) at (0,0) {
          \\includegraphics[height=0.28\\textheight]{figures/BMINUSL_\\Region/flavor_mm__\\PlotName__BMINUSL_\\Region__\\LinLog.pdf}};
          % \\begin{scope}[x={(image.south east)}, y={(image.north west)}]
          %   \\draw[red, ultra thick, rounded corners] (0.25, 0.08) rectangle (0.45, 0.26);

          %   % \\draw[help lines,xstep=.1,ystep=.1] (0,0) grid (1,1);
          %   % \\foreach \\x in {0,1,...,9} { \\node [anchor=north] at (\\x/10,0) {0.\\x}; }
          %   % \\foreach \\y in {0,1,...,9} { \\node [anchor=east] at (0,\\y/10) {0.\\y}; }

          % \\end{scope}
      \\end{tikzpicture}
    \\end{block}

  \\end{columns}
}


''')


# ------------------------------------------------------------------------------
def writeThreeFigureSlide(f, hist_name, region_name, lin_log = 'lin'):
    f.write('% ------------------------------------------------------------------------------\n')
    f.write('\\renewcommand{\\RegionTitle}{%s}\n' % regions[region_name])
    f.write('\\renewcommand{\\Region}{%s}\n' % region_name)
    f.write('\\renewcommand{\\PlotTitle}{%s}\n' % histograms[hist_name])
    f.write('\\renewcommand{\\PlotName}{%s}\n' % hist_name)
    f.write('\\renewcommand{\\LinLog}{%s}\n' % lin_log)
    f.write('''\\frame
{
  \\frametitle{\\PlotTitle\\,in \\RegionTitle}
''')
    discussion(f, hist_name, region_name)
    f.write('''
  \\begin{columns}
    \\column{0.32\\textwidth}
    \\begin{block}{All flavor channels}
      \\begin{tikzpicture}
        \\node[anchor=south west, inner sep=0] (image) at (0,0) {
          \\includegraphics[height=0.28\\textheight]{figures/BMINUSL_\\Region/flavor_all__\\PlotName__BMINUSL_\\Region__\\LinLog.pdf}};
          % \\begin{scope}[x={(image.south east)}, y={(image.north west)}]
          %   \\draw[red, ultra thick, rounded corners] (0.25, 0.08) rectangle (0.45, 0.26);

          %   % \\draw[help lines,xstep=.1,ystep=.1] (0,0) grid (1,1);
          %   % \\foreach \\x in {0,1,...,9} { \\node [anchor=north] at (\\x/10,0) {0.\\x}; }
          %   % \\foreach \\y in {0,1,...,9} { \\node [anchor=east] at (0,\\y/10) {0.\\y}; }

          % \\end{scope}
      \\end{tikzpicture}
    \\end{block}

    \\column{0.32\\textwidth}
    \\begin{block}{$ee$}
      \\begin{tikzpicture}
        \\node[anchor=south west, inner sep=0] (image) at (0,0) {
          \\includegraphics[height=0.28\\textheight]{figures/BMINUSL_\\Region/flavor_ee__\\PlotName__BMINUSL_\\Region__\\LinLog.pdf}};
          % \\begin{scope}[x={(image.south east)}, y={(image.north west)}]
          %   \\draw[red, ultra thick, rounded corners] (0.25, 0.08) rectangle (0.45, 0.26);

          %   % \\draw[help lines,xstep=.1,ystep=.1] (0,0) grid (1,1);
          %   % \\foreach \\x in {0,1,...,9} { \\node [anchor=north] at (\\x/10,0) {0.\\x}; }
          %   % \\foreach \\y in {0,1,...,9} { \\node [anchor=east] at (0,\\y/10) {0.\\y}; }

          % \\end{scope}
      \\end{tikzpicture}
    \\end{block}

    \\column{0.32\\textwidth}
    \\begin{block}{$\\mu\\mu$}
      \\begin{tikzpicture}
        \\node[anchor=south west, inner sep=0] (image) at (0,0) {
          \\includegraphics[height=0.28\\textheight]{figures/BMINUSL_\\Region/flavor_mm__\\PlotName__BMINUSL_\\Region__\\LinLog.pdf}};
          % \\begin{scope}[x={(image.south east)}, y={(image.north west)}]
          %   \\draw[red, ultra thick, rounded corners] (0.25, 0.08) rectangle (0.45, 0.26);

          %   % \\draw[help lines,xstep=.1,ystep=.1] (0,0) grid (1,1);
          %   % \\foreach \\x in {0,1,...,9} { \\node [anchor=north] at (\\x/10,0) {0.\\x}; }
          %   % \\foreach \\y in {0,1,...,9} { \\node [anchor=east] at (0,\\y/10) {0.\\y}; }

          % \\end{scope}
      \\end{tikzpicture}
    \\end{block}

  \\end{columns}
}


''')


# ------------------------------------------------------------------------------
def discussion(f, hist_name, region_name):
    f.write('\\begin{itemize}\n')
    # if region_name == 'CR_TOP':
    #     if hist_name == 'mbl_0':
    #         f.write('\\item Reasonable agreement apart from $ee$ flavor channel \\Simley{0.5}\n')
    #     elif hist_name == 'mbl_1':
    #         f.write('''\\item As with the leading pair, the sub-leading \Mbl distribution has
    #                 reasonable agreement apart from $ee$ flavor channel \Simley{0.5}\n''')
    #     elif hist_name == 'ht_signal':
    #         f.write('\\item Good agreement apart from single bin in $ee$ with low stats \\Simley{0.5}\n')
    #     elif hist_name == 'met_sig_signal':
    #         f.write('\\item Good agreement in core of distribution \\Simley{0.5}\n')
    #     elif hist_name == 'lep_pt_detailed_0':
    #         f.write('\\item Reasonable agreement \\Simley{0}\n')
    #     elif hist_name == 'lep_pt_detailed_1':
    #         f.write('\\item Reasonable agreement \\Simley{0}\n')
    #     elif hist_name == 'lep_eta_0':
    #         f.write('\\item Apart from strange features in $ee$ channel, good agreement \\Simley{0}\n')
    #     elif hist_name == 'lep_eta_1':
    #         f.write('\\item Reasonable agreement \\Simley{0}\n')
    #     elif hist_name == 'mll':
    #         f.write('\\item Good agreement apart from bin nearest the $Z$ mass \\Simley{1}\n')
    #     else:
    #         f.write('\\item Good agreement \\Simley{1}\n')

    # elif region_name == 'CR_Z':
    #     if hist_name == 'mbl_0':
    #         f.write('''\\item Apart from the overall disagreement in the normalization, the shape
    #                 appears to be modeled pretty well \\Simley{0.5}\n''')
    #     elif hist_name == 'mbl_1':
    #         f.write('''\\item Apart from the overall disagreement in the normalization, the shape
    #         appears to be modeled pretty well \\Simley{0.5}\n''')
    #     elif hist_name == 'lep_pt_detailed_0':
    #         f.write('\\item Agreement is worse for low $p_\\mathrm{T}$ leptons \\Simley{0}\n')
    #     elif hist_name == 'lep_pt_detailed_1':
    #         f.write('\\item Agreement is slightly worse for low $p_\\mathrm{T}$ leptons \\Simley{0}\n')
    #     elif hist_name == 'lep_eta_1':
    #         f.write('\\item Shape reasonalby well described apart from a few bins \\Simley{0.5}\n')
    #     elif hist_name == 'mbb':
    #         f.write('\\item Core of distribution seems worse than tail, but could be statistical fluctuations \\Simley{-0.5}\n')
    #     elif hist_name == 'ptll':
    #         f.write('\\item Low $p_\\mathrm{T}$ events have larger disagreement \\Simley{-0.5}\n')
    #         f.write('\\item Especially in $ee$\n')
    #     elif hist_name == 'ptbb':
    #         f.write('\\item Shape of $\\mu\\mu$ is reasonalby well modeled \\Simley{0.5}\n')
    #         f.write('\\item Shape of $ee$ looks OK apart from a couple of bins near the peak \\Simley{0.0}\n')
    #     else:
    #         f.write('\\item Shape well described \\Simley{0.5}\n')

    # elif region_name == 'VR_TOP_1':
    #     if hist_name == 'mbl_0':
    #         f.write('''\\item Good agreement apart from low mass $ee$ events \\Simley{0.5}\n''')
    #     elif hist_name == 'mbl_1':
    #         f.write('''\\item Good agreement apart from low mass $ee$ events \\Simley{0.5}\n''')
    #     elif hist_name == 'ht_signal':
    #         f.write('\\item Good agreement apart from low $h_\\mathrm{T}$ $ee$ events \\Simley{0.5}\n')
    #     elif hist_name == 'b_jet_pt_detailed_0':
    #         f.write('\\item Reasonable agreement in $e\\mu$ and $\\mu\\mu$ channels \\Simley{0.5}\n')
    #         f.write('\\item Underpredict in core of disctribution in $ee$ channel \\Simley{-0.5}\n')
    #     elif hist_name == 'b_jet_pt_detailed_1':
    #         f.write('\\item Reasonable agreement in $e\\mu$ and $\\mu\\mu$ channels \\Simley{0.5}\n')
    #         f.write('\\item Underpredict for low $p_\\mathrm{T}$ electrons in $ee$ channel \\Simley{-0.5}\n')
    #     elif hist_name == 'b_jet_eta_0':
    #         f.write('\\item Similar feature as seen in top CR \\Simley{0}\n')
    #         f.write('\\item Otherwise, good agreement \\Simley{0.5}\n')
    #     elif hist_name == 'mll':
    #         f.write('\\item Reasonable agreement in $e\\mu$ and $\\mu\\mu$ channels \\Simley{0.5}\n')
    #         f.write('\\item Underpredict in $ee$ channel \\Simley{-0.5}\n')
    #     elif hist_name == 'mbb':
    #         f.write('\\item Reasonable agreement in $e\\mu$ and $\\mu\\mu$ channels \\Simley{0.5}\n')
    #         f.write('\\item Underpredict for low mass events in $ee$ channel \\Simley{-0.5}\n')
    #     else:
    #         f.write('\\item Reasonable agreement \\Simley{0.5}\n')

    # elif region_name == 'VR_TOP_2':
    #     if hist_name == 'mbl_0':
    #         f.write('''\\item Good agreement \\Simley{0.5}\n''')
    #     elif hist_name == 'mbl_1':
    #         f.write('''\\item Good agreement outside low statistics bins \\Simley{0.5}\n''')
    #     elif hist_name == 'b_jet_pt_detailed_1':
    #         f.write('\\item Funny feature in $e\\mu$ channel near 60 GeV\\Simley{0}\n')
    #         f.write('\\item Doesn\'t seem to show up elsewhere\n')
    #     else:
    #         f.write('''\\item Reasonable agreement \\Simley{0.5}\n''')

    # elif region_name == 'VR_TOP_3':
    #     if hist_name == 'mbl_0':
    #         f.write('''\\item Most of the disagreement here seems to show up at low mass \\Simley{0.0}\n''')
    #         f.write('''\\item The statistics are probably too low in this region to conclude much \\Simley{-0.5}\n''')
    #     elif hist_name == 'mbl_1':
    #         f.write('\\item Hard to say anythin with low statistics \\Simley{-0.5}\n')
    #     elif 'lep_eta' in hist_name or 'b_jet_pt' in hist_name:
    #         f.write('\\item Hard to say anything with this binning \\Simley{-0.5}\n')
    #     else:
    #         f.write('\\item Despite the low statistics, this actually looks reasonable \\Simley{0.5}\n')

    # elif region_name == 'VR_Z':
    #     if hist_name == 'mbl_0':
    #         f.write('''\\item Reasonable agreement despite less than great statistics \\Simley{0.5}\n''')
    #         f.write('''\\item Need to rebin the plots in this region\n''')
    #     # elif hist_name == 'mbl_1':
    #     #     f.write('''\\item Reasonable agreement \\Simley{0.5}\n''')
    #     # elif hist_name == 'ht_signal':
    #     #     f.write('\\item ... \\Simley{0.0}\n')
    #     # elif hist_name == 'met_sig_signal':
    #     #     f.write('\\item ... \\Simley{0.0}\n')
    #     elif hist_name == 'lep_pt_detailed_0':
    #         f.write('''\\item Reasonable agreement despite less than great statistics \\Simley{0.5}\n''')
    #     # elif hist_name == 'lep_pt_detailed_1':
    #     #     f.write('\\item ... \\Simley{0}\n')
    #     # elif hist_name == 'lep_eta_0':
    #     #     f.write('\\item ... \\Simley{0}\n')
    #     # elif hist_name == 'lep_eta_1':
    #     #     f.write('\\item ... \\Simley{0}\n')
    #     elif hist_name == 'b_jet_pt_detailed_0':
    #         f.write('\\item Cannot conclude anything from this plot \\Simley{0}\n')
    #     # elif hist_name == 'b_jet_pt_detailed_1':
    #     #     f.write('\\item ... \\Simley{0}\n')
    #     # elif hist_name == 'b_jet_eta_0':
    #     #     f.write('\\item ... \\Simley{0}\n')
    #     # elif hist_name == 'b_jet_eta_1':
    #     #     f.write('\\item ... \\Simley{0}\n')
    #     # elif hist_name == 'mll':
    #     #     f.write('\\item ... \\Simley{0}\n')
    #     # elif hist_name == 'mbb':
    #     #     f.write('\\item ... \\Simley{0}\n')
    #     # elif hist_name == 'ptll':
    #     #     f.write('\\item ... \\Simley{0}\n')
    #     # elif hist_name == 'ptbb':
    #     #     f.write('\\item ... \\Simley{0}\n')
    #     else:
    #         f.write('''\\item Reasonable agreement \\Simley{0.5}\n''')

    # else:
    #     f.write('\\item ...\n')

    f.write('\\item ...\n')
    f.write('\\end{itemize}\n')


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    f = file('backup.tex', 'w')
    writeFirstPart(f)

    for region in regions:
        writeRegionTitleSlide(f, region)
        for hist in histograms:
            if 'Z' not in region and hist == 'mll_detailed': continue
            if 'Z' in region and hist == 'mll': continue

            if 'Z' not in region:
                writeFourFigureSlide(f, hist, region)
            else:
                writeThreeFigureSlide(f, hist, region)

    f.close()
