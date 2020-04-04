# hep_make_bib_v2
Making bibs for latex/tex based on the new version of [INSPIRE-HEP](https://inspirehep.net/) and [selenium](https://www.selenium.dev/)/[pyppeteer](https://github.com/miyakogi/pyppeteer)/[pyppeteer2](https://github.com/pyppeteer/pyppeteer2).

# Introduction
Due to the [old INSPIRE](https://old.inspirehep.net) will be phased out by June 2020, the first version of [hep_make_bib](https://github.com/ElonSteveWang/hep_make_bib) have to upgrade to adapt new INSPIRE-HEP. 

The new version of INSPIRE-HEP adopts js dynamic loading technology, but the first edition hep_make_bib can't work properly in this situation. Given a lot of consideration, the new version of hep_make_bib (namely [hep_make_bib_v2](https://github.com/ElonSteveWang/hep_make_bib_v2)) inner inserted in two methods, selenium and pyppeteer, to solve this problem. 

# Environment
For selenium, this python script inner inserted three webdrivers: Chrome, Firefox and Safari, the default webdriver is for Firefox. Before you can use it, you need to configure the relevant driver which download address is indicated in this script. 

For pyppeteer,an unofficial Python port of puppeteer JavaScript (headless) chrome/chromium browser automation library. Your computer will be automatically download chromium browser when you first use it. 

If you want change another webdriver, please you swicth it in script via annotated and un-annotated related codes.

Default model is headless.

# Instruction
It's used the same way as [hep_make_bib](https://github.com/ElonSteveWang/hep_make_bib). Here is an example of how to use it.

```
# cd /some/place 
# python3 make_bib.py
Please input your keyword...
Fast neutrino+PRD+2020
Your are searching:  Fast neutrino+PRD+2020
You got  4  result(s) in the index - 1  page. Total:  4 results .


Index.  0 , ---------->title:  Fast Neutrino Flavor Instability in the Neutron-star Convection Layer of Three-dimensional Supernova Models


%\cite{Glas:2019kbx}
\bibitem{Glas:2019kbx}
R.~Glas, H.~-.~Janka, F.~Capozzi, M.~Sen and B.~Dasgupta~,
{\it{Fast Neutrino Flavor Instability in the Neutron-star Convection Layer of Three-dimensional Supernova Models}},{\color{blue}\href{https:/doi.org/10.1103/PhysRevD.101.063001}{~ Phys.Rev.D\textbf{ 101} (2020) 6, 063001}\href{https://arxiv.org/abs/1912.00274}{~[arVix: 1912.00274 [astro-ph.HE]]}[\href{https://inspirehep.net//literature/1768014}{\scriptsize IN\normalsize SPIRE}]}


Index.  1 , ---------->title:  Fast Neutrino Flavor Conversion Modes in Multidimensional Core-collapse Supernova Models: the Role of the Asymmetric Neutrino Distributions


%\cite{Abbar:2019pfb}
\bibitem{Abbar:2019pfb}
S.~Abbar, H.~Duan, K.~Sumiyoshi, T.~Takiwaki and M.~C.~Volpe~,
{\it{Fast Neutrino Flavor Conversion Modes in Multidimensional Core-collapse Supernova Models: the Role of the Asymmetric Neutrino Distributions}},{\color{blue}\href{https:/doi.org/10.1103/PhysRevD.101.043016}{~ Phys.Rev.D\textbf{ 101} (2020) 4, 043016}\href{https://arxiv.org/abs/1911.01983}{~[arVix: 1911.01983 [astro-ph.HE]]}[\href{https://inspirehep.net//literature/1763159}{\scriptsize IN\normalsize SPIRE}]}


Index.  2 , ---------->title:  Fast collective neutrino oscillations inside the neutrino sphere in core-collapse supernovae


%\cite{Azari:2019zgt}
\bibitem{Azari:2019zgt}
M.~D.~Azari, S.~Yamada, T.~Morinaga, H.~Nagakura and S.~Furusawa~,
{\it{Fast collective neutrino oscillations inside the neutrino sphere in core-collapse supernovae}},{\color{blue}\href{https:/doi.org/10.1103/PhysRevD.101.023018}{~ Phys.Rev.D\textbf{ 101} (2020) 2, 023018}\href{https://arxiv.org/abs/1910.06176}{~[arVix: 1910.06176 [astro-ph.HE]]}[\href{https://inspirehep.net//literature/1758800}{\scriptsize IN\normalsize SPIRE}]}


Index.  3 , ---------->title:  Distinguishing Dirac and Majorana neutrinos by their decays via Nambu-Goldstone bosons in the gravitational-anomaly model of neutrino masses


%\cite{Funcke:2019zkg}
\bibitem{Funcke:2019zkg}
L.~Funcke, G.~Raffelt and E.~Vitagliano~,
{\it{Distinguishing Dirac and Majorana neutrinos by their decays via Nambu-Goldstone bosons in the gravitational-anomaly model of neutrino masses}},{\color{blue}\href{https:/doi.org/10.1103/PhysRevD.101.015025}{~ Phys.Rev.D\textbf{ 101} (2020) 1, 015025}\href{https://arxiv.org/abs/1905.01264}{~[arVix: 1905.01264 [hep-ph]]}[\href{https://inspirehep.net//literature/1733131}{\scriptsize IN\normalsize SPIRE}]}
```

For now, you can copy the corresponding bib into your document. As you may have noticed, the usage of the key words is exactly the same as the inspire-hep. Don't explain much, please see the picture below.![example](https://github.com/ElonSteveWang/hep_make_bib/blob/master/example.png) Three hyperlinks are inserted in the highlighted blue text to the corresponding online journal, arxiv and inspire-hep home pages of the article, respectively.


# Common problems
* Users in mainland China may experience very slow production speed, presumably the driver used in this program is not well configured. 
* If there are some special symbol in the title of the article, the generated bib need to be manually modified by themselves.
* The generated bib maybe abnormal for some special cases. However, unfortunately, I do not intend to fix the bugs of this version in the future. Because I also already upgrade it to [hep_make_bib_v3](https://github.com/ElonSteveWang/hep_make_bib_v3).(:smile::smile::smile::smile:)



# License
[hep_make_bib_v2](https://github.com/ElonSteveWang/hep_make_bib_v2) is available under the terms of the [GNU General Public License, version 2](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

This project can also be used on other websites with a few changes. If someone based on this work for the second development, please indicate the source, thank you!
