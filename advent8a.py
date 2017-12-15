import re
import sys

indata = """"| d dec 683 if qn == 0         |
| d dec -220 if h == 0         |
| rak dec -875 if rak > -9     |
| isy dec 250 if wf == 0       |
| cie dec 20 if rak > 870      |
| isy inc 93 if wf >= -5       |
| o dec 739 if bok < 8         |
| rak inc -605 if mxg <= 9     |
| rak inc 668 if rfw > -8      |
| rfw dec 214 if h > -7        |
| j dec 649 if wf != 4         |
| bok dec -712 if cie >= -22   |
| s dec 151 if rxb == 0        |
| bok dec -656 if d <= -463    |
| pf dec -435 if brr != -10    |
| pf dec 115 if rxb < 6        |
| uxr dec -574 if brr == -3    |
| h inc -34 if s == -151       |
| rxb inc -919 if rak == 938   |
| s inc 627 if o <= -748       |
| rxb dec -456 if rfw != -214  |
| rak dec -687 if x <= 8       |
| d dec 292 if bok >= 1363     |
| mxg inc 665 if o == -739     |
| brr dec 531 if bok == 1368   |
| isy dec -890 if x != 7       |
| o inc -649 if bok > 1361     |
| erb dec 656 if j != -648     |
| vso inc -882 if wf <= -2     |
| rxb inc 978 if brr >= -539   |
| pf dec -176 if wf <= 8       |
| rxb dec -647 if hsn == 0     |
| vso inc -2 if isy <= 725     |
| brr dec -661 if x != 4       |
| uxr dec 913 if x <= 9        |
| hsn inc -784 if rxb <= 706   |
| pf dec -795 if hsn <= -782   |
| pf dec 421 if rfw >= -217    |
| o inc -88 if s < -147        |
| rak inc 991 if hsn == -784   |
| brr dec -27 if bok != 1372   |
| uxr dec 705 if x >= -2       |
| tss inc 130 if h != -35      |
| vso inc -800 if wf != 8      |
| tss inc 301 if pf != 866     |
| ie inc -311 if cie == -20    |
| mxg inc -20 if vso >= -808   |
| cie dec -142 if bok == 1368  |
| rfw dec -141 if rxb != 706   |
| isy dec -826 if j > -656     |
| cie inc 252 if pf >= 870     |
| hsn dec 972 if bs < 2        |
| hsn inc -576 if rfw >= -219  |
| bok dec 439 if h >= -40      |
| cie dec 614 if h == -34      |
| cie dec 890 if cie == -240   |
| wf inc -251 if pf <= 875     |
| isy inc -507 if o == -1476   |
| bok dec 619 if bok < 928     |
| rxb inc 361 if rfw == -224   |
| rfw dec -654 if s < -141     |
| mxg dec -488 if isy >= 1047  |
| pf dec 721 if mxg >= 1135    |
| h inc -4 if rxb == 706       |
| hsn dec -966 if rfw >= 431   |
| isy dec -422 if h < -44      |
| rfw inc -379 if qn == 0      |
| pf inc -78 if cie >= -1136   |
| o inc 902 if isy > 1042      |
| erb dec -529 if brr <= 160   |
| x dec 280 if o <= -572       |
| isy dec -266 if d < -751     |
| j dec -260 if isy != 1313    |
| rak dec 330 if qn != 9       |
| tss inc -113 if ie <= -311   |
| isy dec -186 if erb > -135   |
| o dec 839 if pf <= 800       |
| x inc -906 if uxr > -1622    |
| hsn dec 353 if vso > -808    |
| cie dec -734 if bs > -9      |
| rak dec -690 if rfw == 61    |
| tss inc 355 if rfw == 54     |
| isy dec 507 if erb != -127   |
| uxr dec -901 if hsn >= -1726 |
| tss inc 787 if cie == -396   |
| j inc -851 if d < -753       |
| d dec -929 if pf < 790       |
| h inc -328 if mxg <= 1140    |
| j dec -381 if erb != -122    |
| o dec 810 if rxb <= 696      |
| brr dec 207 if x == -1186    |
| rak dec -697 if erb < -135   |
| ie dec 96 if vso <= -798     |
| vso inc 739 if rak < 2968    |
| o inc 890 if mxg == 1133     |
| wf dec 453 if pf <= 785      |
| rxb inc -950 if bok > 923    |
| brr inc 160 if isy != 1504   |
| isy inc 767 if rak < 2967    |
| bok dec 297 if bs != 2       |
| qn dec -686 if erb == -127   |
| uxr dec -835 if h >= -370    |
| rxb dec -315 if pf < 799     |
| h inc -97 if j != -864       |
| bs inc -380 if erb < -117    |
| rfw dec -444 if tss <= 1108  |
| brr inc 951 if wf <= -251    |
| erb dec -665 if h != -465    |
| qn inc -350 if isy != 1504   |
| h inc 603 if bs < -373       |
| vso inc -545 if uxr != 111   |
| o inc 110 if brr > 894       |
| s dec -924 if rfw <= 509     |
| hsn dec -114 if rfw != 507   |
| tss dec -441 if erb != 529   |
| d inc -791 if bok > 630      |
| rxb dec 576 if pf >= 800     |
| x dec 797 if j >= -859       |
| cie inc 828 if rfw <= 507    |
| s inc 945 if mxg != 1127     |
| mxg inc 122 if qn <= 685     |
| rak inc 778 if pf <= 786     |
| tss inc -795 if pf < 794     |
| vso dec -412 if d >= -1553   |
| vso inc 371 if bs != -385    |
| wf inc 443 if uxr != 109     |
| wf dec 366 if rak == 2976    |
| tss inc 608 if vso >= -571   |
| x inc 316 if qn != 694       |
| o inc -570 if mxg > 1136     |
| qn inc 346 if bok < 636      |
| erb dec 947 if erb != 529    |
| uxr dec -673 if h != 147     |
| pf inc -252 if d == -1546    |
| ie dec -157 if o < -406      |
| vso inc -46 if rfw > 499     |
| qn dec -915 if vso <= -617   |
| bok dec 288 if rak < 2983    |
| o inc -842 if uxr == 783     |
| rfw dec 867 if mxg > 1136    |
| s dec -639 if uxr == 791     |
| uxr dec 825 if erb < -406    |
| rxb inc 414 if j >= -866     |
| d dec 695 if vso > -612      |
| mxg dec 119 if uxr == -34    |
| tss inc -168 if bs > -379    |
| tss inc 379 if mxg <= 1017   |
| mxg dec 629 if ie != -250    |
| rak inc 803 if d != -2245    |
| pf dec -393 if rxb > 488     |
| ie dec 574 if tss <= 1740    |
| bok dec 498 if brr <= 907    |
| rxb inc -999 if x < -1663    |
| h inc -716 if s != 2359      |
| vso inc -635 if cie > 430    |
| tss inc 712 if mxg > 1009    |
| x dec 303 if mxg == 1016     |
| x dec -426 if rfw <= 510     |
| rxb dec -99 if wf <= -174    |
| ie dec 955 if x == -1241     |
| ie inc -6 if qn < 1036       |
| o inc 231 if pf != 541       |
| d inc -967 if bok < -147     |
| bs dec -86 if qn <= 1037     |
| rak dec 255 if x != -1240    |
| rfw dec 143 if d >= -3204    |
| qn dec 175 if hsn > -1614    |
| j inc -550 if isy == 1504    |
| cie dec -553 if d != -3209   |
| wf dec 353 if hsn == -1605   |
| vso dec -563 if d <= -3205   |
| o inc 593 if wf == -535      |
| vso dec -519 if vso != -677  |
| rfw inc 122 if s >= 2357     |
| wf inc -889 if vso <= -166   |
| ie dec -73 if rak >= 3531    |
| pf dec 79 if d <= -3201      |
| hsn dec 164 if cie > 982     |
| rak dec 237 if rxb != -419   |
| qn dec -585 if tss > 2442    |
| rfw dec -186 if rfw >= 623   |
| uxr dec 520 if rfw < 822     |
| x dec 447 if x > -1251       |
| vso inc -796 if pf < 464     |
| tss dec 34 if rxb == -415    |
| x inc 603 if cie != 994      |
| uxr dec -234 if h <= -577    |
| rak inc 381 if h < -571      |
| j inc 692 if pf >= 455       |
| pf inc -279 if pf != 461     |
| bs inc -401 if h == -576     |
| o inc -629 if mxg != 1018    |
| hsn dec -619 if x < -1086    |
| bok dec -91 if qn >= 1433    |
| bs dec 660 if isy < 1495     |
| x dec -908 if vso != -960    |
| rak inc -16 if x >= -185     |
| mxg dec -367 if mxg == 1010  |
| bs inc 487 if o > -802       |
| mxg inc -608 if o == -811    |
| brr inc -730 if d < -3198    |
| mxg dec -872 if qn != 1438   |
| bs inc 467 if cie >= 983     |
| isy inc 504 if cie < 981     |
| rxb inc 356 if isy >= 1501   |
| pf inc 427 if mxg < 1279     |
| brr inc 967 if isy < 1510    |
| rxb dec 561 if j > -720      |
| hsn dec -175 if d != -3218   |
| wf dec 700 if hsn >= -1602   |
| h inc 637 if brr >= 1137     |
| uxr inc 964 if wf >= -1232   |
| rxb inc -739 if uxr > 401    |
| erb dec -494 if qn == 1450   |
| rxb inc -226 if qn != 1436   |
| brr inc 131 if bs <= -220    |
| rak inc -899 if mxg == 1274  |
| tss dec -737 if bs != -238   |
| j dec 700 if wf == -1220     |
| j dec -823 if rak > 3654     |
| j inc 466 if d > -3211       |
| ie dec -521 if o == -811     |
| d inc -898 if qn > 1440      |
| isy dec 197 if rfw <= 815    |
| erb dec -911 if vso > -952   |
| j inc -835 if cie >= 983     |
| erb dec -315 if uxr != 416   |
| brr inc -673 if erb <= -99   |
| erb inc -72 if vso <= -949   |
| vso inc 165 if mxg <= 1285   |
| qn dec -870 if vso >= -799   |
| pf dec -574 if j == -1086    |
| pf inc -858 if erb > -173    |
| erb inc -243 if cie >= 985   |
| rxb inc -927 if x == -177    |
| rxb inc -260 if vso < -792   |
| tss inc 62 if rak > 3647     |
| tss dec -675 if vso <= -792  |
| qn inc 807 if rfw <= 810     |
| bok inc -360 if d > -4101    |
| s dec 56 if brr != 1260      |
| wf inc 855 if j == -1096     |
| j inc 698 if s <= 2304       |
| isy dec -459 if hsn <= -1591 |
| s dec -577 if bok > -71      |
| wf dec -469 if j != -397     |
| pf dec 127 if tss != 3897    |
| o inc 442 if rak >= 3651     |
| d dec 941 if j <= -383       |
| brr dec 809 if rak <= 3652   |
| o inc 161 if rfw != 820      |
| h dec 284 if uxr <= 418      |
| j inc -805 if pf < 475       |
| uxr inc 731 if uxr > 409     |
| isy dec -589 if isy <= 1772  |
| s inc 358 if h <= -221       |
| wf inc 680 if rxb == -2519   |
| brr dec 919 if ie != -1270   |
| tss dec -77 if h > -226      |
| qn dec 953 if hsn == -1594   |
| s inc -553 if rfw == 813     |
| isy dec 389 if qn < 1367     |
| qn dec 676 if vso != -782    |
| mxg dec 328 if uxr > 1135    |
| wf dec 788 if hsn < -1599    |
| uxr inc -361 if brr == -459  |
| isy dec -775 if rxb > -2504  |
| uxr inc 680 if vso < -788    |
| tss dec 368 if tss <= 3967   |
| pf inc -494 if qn <= 681     |
| tss inc 84 if bok == -63     |
| rfw dec -146 if rfw >= 804   |
| erb dec -175 if pf >= 484    |
| pf dec -655 if hsn <= -1590  |
| j dec 273 if pf != 1133      |
| rak inc -305 if wf > -764    |
| o inc -234 if rxb != -2503   |
| rfw dec -499 if uxr < 1470   |
| bs inc -102 if qn < 687      |
| j dec 698 if o > -435        |
| cie inc -460 if cie > 977    |
| wf inc 134 if rfw <= 1463    |
| uxr dec -390 if h == -223    |
| uxr dec -834 if bok >= -64   |
| ie inc 538 if s == 2688      |
| cie inc 504 if o > -445      |
| bok inc 102 if ie < -1255    |
| pf dec -65 if erb != -408    |
| vso dec -317 if vso >= -791  |
| x dec -139 if brr >= -459    |
| s inc 772 if bok < 34        |
| bs dec 736 if j <= -664      |
| j dec -352 if vso != -794    |
| s dec -656 if cie == 1029    |
| rfw inc -919 if x <= -44     |
| o inc 101 if vso < -793      |
| bok dec 37 if bok == 39      |
| hsn dec 413 if erb > -414    |
| d inc 686 if rak != 3337     |
| d dec -164 if j < -300       |
| brr dec 968 if bok >= 1      |
| rxb dec 177 if cie != 1029   |
| j inc 200 if o >= -448       |
| brr inc -665 if vso <= -792  |
| vso inc 581 if rak != 3345   |
| vso inc 491 if wf != -621    |
| rxb inc 611 if rxb >= -2513  |
| bok inc -77 if x != -39      |
| cie dec 354 if qn <= 691     |
| ie dec -328 if uxr != 2693   |
| qn inc 629 if cie <= 679     |
| mxg dec -941 if x > -46      |
| tss inc -153 if x >= -46     |
| o inc -459 if h == -222      |
| ie inc -744 if s >= 3333     |
| tss inc 62 if brr != -2086   |
| tss inc -27 if bs == -330    |
| vso dec -435 if rak != 3341  |
| isy dec -751 if x != -38     |
| hsn inc 700 if mxg != 1898   |
| hsn inc -383 if wf == -624   |
| rfw dec -697 if rfw >= 1458  |
| brr inc -446 if ie > -1682   |
| d dec 43 if rfw < 2152       |
| pf dec -798 if rxb == -1909  |
| vso inc -517 if x != -38     |
| rxb dec -595 if rxb < -1892  |
| s dec -820 if mxg <= 1884    |
| o dec -502 if uxr >= 2686    |
| wf inc -541 if rak < 3340    |
| d inc 285 if tss != 3572     |
| vso dec -901 if brr != -2543 |
| uxr dec 402 if rxb != -1306  |
| erb dec -927 if erb > -416   |
| tss dec -62 if rxb != -1312  |
| o inc -194 if qn >= 1319     |
| hsn inc 734 if isy <= 1972   |
| tss dec 553 if qn > 1308     |
| d inc -33 if vso == 1616     |
| bok dec 775 if tss <= 3080   |
| hsn dec 119 if cie >= 669    |
| x inc -50 if j <= -106       |
| erb dec -422 if qn >= 1309   |
| bs dec -573 if rxb <= -1303  |
| uxr dec 431 if uxr <= 2692   |
| rxb inc 174 if uxr <= 2255   |
| tss inc -613 if wf >= -627   |
| brr inc 166 if d != -3936    |
| rak inc -947 if brr <= -2365 |
| bs dec -504 if qn == 1312    |
| cie inc 259 if wf > -630     |
| hsn inc -290 if hsn == -1075 |
| isy dec -778 if mxg <= 1899  |
| rxb inc -146 if x >= -90     |
| bs inc -812 if cie > 929     |
| cie dec -71 if d <= -3943    |
| vso dec 235 if d >= -3935    |
| qn inc 192 if rak >= 2391    |
| rfw inc 403 if erb == 940    |
| rak inc -881 if rxb >= -1285 |
| x dec 30 if rak > 1510       |
| s inc 541 if rxb < -1268     |
| hsn inc -622 if tss != 2453  |
| rak inc -778 if erb <= 946   |
| hsn dec 300 if wf <= -628    |
| hsn inc -72 if ie != -1688   |
| erb inc -145 if erb > 936    |
| x inc -99 if o < -440        |
| vso inc 866 if bok > -842    |
| vso dec -308 if uxr <= 2256  |
| rfw dec 487 if uxr != 2260   |
| rfw dec -21 if mxg > 1881    |
| h inc 866 if rxb <= -1273    |
| erb dec 234 if d >= -3951    |
| erb dec -658 if qn == 1504   |
| o dec 771 if rfw == 2092     |
| h inc -843 if brr < -2377    |
| ie inc -528 if bok >= -851   |
| qn dec 187 if rfw == 2086    |
| isy inc -308 if d <= -3946   |
| rfw inc -163 if vso < 1930   |
| isy inc 815 if h == 643      |
| mxg dec 606 if h < 642       |
| mxg dec 165 if vso > 1923    |
| rfw dec -530 if uxr <= 2253  |
| ie inc 129 if mxg == 1726    |
| uxr dec -505 if h != 638     |
| bok inc -535 if bok >= -851  |
| o dec 941 if j != -104       |
| rak dec -133 if rfw >= 2460  |
| bs inc -461 if mxg >= 1727   |
| j dec -938 if brr != -2368   |
| erb inc 737 if x >= -207     |
| tss dec -280 if hsn < -2051  |
| s dec 651 if bs == -65       |
| rak inc -979 if vso < 1934   |
| pf dec -487 if hsn != -2060  |
| qn inc 384 if j != 830       |
| j inc -389 if o < -2147      |
| hsn dec 14 if s > 3224       |
| rxb dec -710 if uxr <= 2766  |
| hsn inc 278 if s != 3229     |
| tss inc 376 if brr < -2370   |
| d inc 306 if j != 435        |
| wf inc -561 if tss > 3122    |
| h dec -154 if bs >= -65      |
| x inc 396 if hsn != -2073    |
| mxg dec -806 if cie < 1013   |
| hsn dec 941 if hsn <= -2078  |
| erb inc 18 if pf > 1677      |
| x inc 63 if rak > -244       |
| rfw inc 883 if tss == 3124   |
| s inc -615 if erb < 1241     |
| s inc -696 if vso < 1933     |
| qn dec 120 if pf <= 1678     |
| rxb dec -680 if rxb <= -563  |
| wf inc -880 if ie > -2087    |
| tss dec 422 if d <= -3641    |
| d dec 270 if cie > 1004      |
| h dec 993 if tss > 3114      |
| isy dec 490 if o != -2144    |
| bok dec -649 if h > -200     |
| bs dec -505 if o != -2164    |
| hsn inc -863 if rfw == 2459  |
| bok inc -307 if bs <= 442    |
| x dec 961 if rxb > 104       |
| pf inc -606 if brr >= -2376  |
| mxg dec 409 if qn >= 1880    |
| rxb inc -962 if ie == -2079  |
| bs dec 847 if hsn >= -2944   |
| hsn inc 543 if erb == 1237   |
| d dec -752 if ie != -2086    |
| h inc 90 if rak != -228      |
| j dec 620 if cie < 1003      |
| o inc 827 if o != -2156      |
| erb inc -601 if bs >= -408   |
| mxg inc -616 if o >= -1335   |
| h dec -583 if rfw < 2468     |
| rfw inc -727 if erb <= 643   |
| s dec 178 if rak < -237      |
| rfw inc -781 if x >= -1122   |
| hsn inc 503 if brr < -2365   |
| h dec 738 if hsn != -1888    |
| vso inc 10 if rfw != 961     |
| tss dec 455 if j != 430      |
| pf dec -654 if bok >= -1047  |
| mxg dec -953 if hsn == -1890 |
| rfw inc -859 if cie <= 1008  |
| rxb inc -957 if x >= -1112   |
| erb inc 775 if isy >= 3061   |
| rfw inc -574 if rxb == -850  |
| erb inc 304 if s <= 1746     |
| bok dec 703 if bs <= -413    |
| d dec 788 if bs <= -404      |
| uxr inc -714 if bok > -1035  |
| bs dec -244 if h <= -264     |
| h dec -530 if vso == 1934    |
| s inc -792 if bs != -407     |
| j inc 384 if rfw >= -484     |
| rfw dec -694 if cie <= 1013  |
| hsn inc -53 if uxr != 2762   |
| rxb dec 83 if j != 834       |
| rxb inc 849 if o >= -1329    |
| o dec -244 if j < 816        |
| x inc 812 if rxb <= -78      |
| pf dec -950 if brr == -2372  |
| x inc -169 if hsn == -1943   |
| mxg inc -673 if vso != 1929  |
| tss dec -932 if pf == 2682   |
| o dec 976 if pf <= 2685      |
| mxg inc -90 if mxg >= 1783   |
| pf inc -466 if pf <= 2690    |
| rxb dec -592 if uxr < 2760   |
| s dec 904 if pf <= 2216      |
| o inc -958 if qn != 1888     |
| d inc 317 if ie != -2077     |
| d inc 732 if wf > -1511      |
| tss dec -200 if tss <= 3584  |
| mxg inc -894 if mxg >= 1692  |
| uxr dec -883 if rak > -248   |
| d dec 576 if x >= -481       |
| mxg inc -418 if d <= -3478   |
| rxb dec -435 if tss == 3594  |
| rxb dec -200 if uxr != 3646  |
| j dec 70 if d != -3473       |
| cie inc 524 if d > -3469     |
| tss dec 988 if rak <= -233   |
| bok inc 567 if pf < 2226     |
| tss inc -486 if isy > 3064   |
| erb inc -952 if brr < -2380  |
| uxr inc 723 if rfw <= 214    |
| x dec -510 if ie != -2078    |
| d inc 395 if rfw <= 212      |
| erb inc 592 if isy > 3075    |
| ie inc -61 if d >= -3080     |
| rak inc 400 if qn >= 1898    |
| erb dec 449 if cie > 997     |
| ie inc -918 if pf > 2215     |
| s dec -711 if rfw <= 220     |
| rxb dec 519 if wf != -1504   |
| ie dec -59 if rxb < 1145     |
| erb dec 425 if tss == 2120   |
| cie inc -306 if isy <= 3069  |
| x dec 635 if o >= -2296      |
| wf dec 815 if tss == 2120    |
| d dec -366 if pf >= 2210     |
| cie inc -787 if o < -2302    |
| erb dec -305 if brr != -2374 |
| rfw dec -915 if pf > 2216    |
| bs inc -516 if hsn >= -1947  |
| rxb inc 845 if tss != 2120   |
| erb dec -201 if qn == 1888   |
| h inc 297 if tss < 2129      |
| h dec -860 if s > 1541       |
| isy dec -59 if hsn > -1949   |
| mxg inc -266 if wf > -2316   |
| vso dec -578 if d != -2703   |
| qn dec 420 if o <= -2299     |
| ie dec 307 if wf == -2319    |
| pf dec -948 if bs >= -929    |
| j dec 927 if h == 1416       |
| vso dec 879 if d > -2717     |
| j dec -543 if uxr != 4374    |
| d dec -20 if o != -2308      |
| brr inc 606 if erb > 1340    |
| hsn dec 547 if rak != -244   |
| cie dec -865 if uxr < 4366   |
| bs inc -408 if o <= -2294    |
| wf inc 938 if rfw < 207      |
| pf inc 633 if j != 1289      |
| rak dec -871 if d <= -2687   |
| hsn inc 311 if tss < 2125    |
| wf dec -231 if qn <= 1477    |
| mxg dec 617 if rxb < 1137    |
| hsn inc 20 if ie > -3315     |
| uxr inc -810 if hsn < -2154  |
| d dec -738 if mxg > 798      |
| o inc 513 if d < -1960       |
| s dec 953 if mxg <= 812      |
| s inc 664 if cie < 775       |
| h dec 18 if bok >= -480      |
| erb dec 43 if rak > 631      |
| vso inc 662 if rak > 632     |
| mxg inc -938 if wf >= -2083  |
| brr inc -359 if rxb > 1136   |
| s dec -402 if rxb < 1144     |
| h dec 59 if x < 48           |
| mxg inc 842 if bs == -1331   |
| ie inc -748 if vso >= 2298   |
| mxg inc -176 if erb > 1301   |
| s inc -345 if bs == -1335    |
| cie inc 52 if brr < -2125    |
| j inc -243 if wf > -2095     |
| d dec 992 if qn != 1468      |
| h inc 302 if tss == 2120     |
| rfw dec 431 if hsn >= -2168  |
| hsn inc -930 if wf > -2098   |
| x dec -477 if cie != 767     |
| erb dec 922 if pf <= 3797    |
| j dec 838 if cie <= 782      |
| mxg inc -96 if bs < -1324    |
| cie dec 707 if hsn > -3099   |
| mxg inc 258 if h < 1655      |
| hsn dec -441 if qn >= 1461   |
| j dec 518 if tss >= 2115     |
| tss dec -760 if ie == -3306  |
| ie dec 21 if d != -1948      |
| j dec -990 if s > 997        |
| bs inc -889 if bok >= -482   |
| s dec 732 if hsn == -2646    |
| pf dec -401 if hsn <= -2639  |
| rak inc 211 if isy != 3128   |
| brr inc -868 if uxr == 3554  |
| vso dec 811 if uxr <= 3563   |
| pf dec 232 if rxb >= 1137    |
| bok inc -193 if vso < 1490   |
| d dec 817 if qn == 1468      |
| rak inc 282 if bs < -2216    |
| o inc 74 if pf < 3972        |
| isy dec -602 if rxb <= 1148  |
| pf inc -6 if cie <= 69       |
| uxr inc 835 if rfw >= -228   |
| tss inc 790 if bok <= -661   |
| rak dec -719 if bok <= -662  |
| cie inc 978 if j > -298      |
| d dec 475 if brr > -2994     |
| rxb dec -348 if pf >= 3976   |
| o dec 62 if j < -301         |
| brr dec 486 if bok > -675    |
| isy dec -256 if hsn == -2648 |
| rxb dec -536 if tss < 3671   |
| ie dec 91 if vso < 1490      |
| h inc 53 if h >= 1644        |
| qn inc 621 if d > -3247      |
| hsn dec -433 if x <= 523     |
| x dec 703 if tss >= 3673     |
| x inc -557 if isy >= 3978    |
| bs inc -180 if h < 1709      |
| pf inc -25 if hsn <= -2207   |
| bs dec 761 if o > -2294      |
| uxr dec 989 if brr > -3482   |
| erb dec 385 if h > 1703      |
| hsn dec 339 if bok < -664    |
| isy inc -176 if s > 989      |
| hsn inc 405 if isy == 3810   |
| pf dec -849 if uxr < 3402    |
| bok inc 274 if rak > 1631    |
| j inc 433 if tss >= 3668     |
| ie dec 385 if o <= -2290     |
| rak inc 529 if tss >= 3670   |
| isy dec -467 if o < -2285    |
| erb inc 765 if erb >= 7      |
| vso dec -935 if wf >= -2084  |
| tss inc 21 if brr != -3487   |
| s dec 631 if erb > 5         |
| hsn inc 709 if h < 1709      |
| isy inc 754 if tss != 3691   |
| rak dec -730 if rfw <= -216  |
| erb inc 33 if bs <= -3156    |
| hsn inc 972 if rxb <= 1681   |
| d inc 902 if mxg <= 1634     |
| cie inc -544 if d == -2343   |
| wf dec -706 if bs <= -3160   |
| j dec 564 if isy < 4282      |
| ie inc -832 if o > -2298     |
| rfw inc 737 if pf >= 4795    |
| o inc 558 if o <= -2285      |
| erb dec 749 if bs > -3163    |
| pf dec -93 if h > 1700       |
| o dec 85 if isy > 4271       |
| brr inc -713 if x <= -45     |
| x dec 659 if d < -2344       |
| tss dec -316 if mxg < 1638   |
| pf inc -542 if bok < -388    |
| tss dec 572 if h <= 1708     |
| s inc -19 if cie != -464     |
| j dec -262 if hsn <= -463    |
| rfw dec -775 if rxb > 1677   |
| s inc 564 if ie > -4639      |
| o inc -484 if brr == -3479   |
| uxr dec -651 if hsn <= -463  |
| wf dec 866 if qn == 2094     |
| ie inc 635 if pf < 4339      |
| cie inc 248 if pf == 4341    |
| rxb dec 233 if o > -2299     |
| bok inc 914 if cie != -232   |
| hsn dec -748 if x == -47     |
| cie dec 322 if uxr <= 4046   |
| mxg inc 79 if brr <= -3477   |
| tss dec 939 if x == -42      |
| pf dec 773 if s < 1551       |
| bok inc -145 if mxg >= 1712  |
| uxr inc -237 if tss > 2494   |
| d dec 187 if mxg >= 1705     |
| ie inc -280 if o > -2305     |
| rak inc -757 if isy > 4273   |
| s dec -922 if isy != 4278    |
| pf dec 868 if qn <= 2089     |
| pf dec 838 if j >= -174      |
| ie inc 293 if rfw > 554      |
| bok dec -846 if o >= -2303   |
| o dec -869 if qn == 2089     |
| rak inc 960 if cie <= -224   |
| vso dec -192 if o != -1443   |
| o dec -477 if rxb != 1675    |
| bs dec 256 if uxr > 3813     |
| brr dec 224 if bok > 1360    |
| qn dec -294 if erb <= -726   |
| h dec 790 if ie >= -4628     |
| erb inc -964 if rak != 3104  |
| rfw dec 417 if s >= 2462     |
| wf inc -396 if pf == 1862    |
| wf dec 765 if s > 2457       |
| bs inc -213 if mxg < 1711    |
| rfw dec 18 if o > -963       |
| isy dec 99 if uxr != 3808    |
| uxr dec -548 if mxg > 1707   |
| hsn dec 404 if brr == -3703  |
| cie dec -420 if x <= -49     |
| erb dec -623 if rxb < 1682   |
| h dec 519 if rxb > 1682      |
| o dec -58 if rak < 3106      |
| vso inc 459 if rxb == 1679   |
| hsn dec 843 if rfw < 126     |
| mxg inc 820 if pf < 1864     |
| hsn inc 60 if ie >= -4629    |
| brr dec 25 if rxb == 1679    |
| uxr dec 148 if wf > -2545    |
| s dec 416 if o == -897       |
| hsn inc -427 if ie != -4625  |
| s inc -925 if erb >= -1066   |
| tss dec -413 if d != -2530   |
| j dec 346 if tss <= 2500     |
| uxr inc -160 if wf != -2542  |
| wf inc -718 if bs == -3630   |
| j inc -518 if brr != -3728   |
| hsn dec -489 if bok <= 1372  |
| bok dec -28 if tss == 2496   |
| bok dec -106 if x != -34     |
| d dec 905 if erb == -1060    |
| bok dec -303 if s <= 1529    |
| vso inc 650 if uxr > 4053    |
| cie inc -209 if ie < -4627   |
| erb dec 272 if d <= -3435    |
| h dec 100 if wf != -3253     |
| ie inc -783 if d != -3425    |
| wf dec -712 if vso == 2785   |
| pf dec 133 if ie > -5403     |
| brr dec 218 if bs < -3625    |
| qn dec -420 if rfw < 127     |
| bok dec -633 if s < 1546     |
| cie inc -932 if ie > -5412   |
| wf dec 515 if pf > 1857      |
| mxg inc 454 if ie <= -5411   |
| x inc -77 if hsn == -1593    |
| o inc 746 if brr <= -3950    |
| x dec 872 if erb >= -1332    |
| vso inc 268 if h != 815      |
| h dec -436 if bs != -3624    |
| erb dec -543 if bok < 2141   |
| ie dec -375 if tss == 2496   |
| x dec -176 if rxb > 1672     |
| pf dec 926 if rfw <= 124     |
| bs inc -134 if pf <= 938     |
| isy dec 664 if rxb != 1684   |
| s inc 584 if isy >= 3523     |
| vso dec 913 if rak >= 3098   |
| bs inc 745 if wf == -3064    |
| rfw inc 309 if qn == 2515    |
| uxr dec -496 if isy <= 3515  |
| hsn dec -633 if isy <= 3514  |
| brr dec 502 if j <= -521     |
| brr inc -521 if j != -519    |
| tss dec 302 if o != -891     |
| hsn inc 340 if ie != -5030   |
| cie dec 959 if j > -522      |
| wf inc 417 if erb <= -781    |
| isy dec -376 if d <= -3444   |
| h inc -131 if cie != -2112   |
| bs inc -510 if vso < 3055    |
| x inc -780 if rxb > 1676     |
| ie dec 702 if tss >= 2187    |
| rfw inc 590 if h <= 1124     |
| wf dec -967 if hsn > -969    |
| vso dec -104 if s > 1536     |
| hsn inc 197 if brr <= -4468  |
| qn dec -309 if ie == -5730   |
| x inc 694 if brr > -4472     |
| isy dec -704 if vso > 3164   |
| j inc -127 if x >= -904      |
| pf inc -579 if uxr != 4550   |
| bok inc -666 if rak > 3092   |
| vso dec -926 if hsn <= -969  |
| brr dec 71 if brr > -4467    |
| s dec 10 if o > -904         |
| j inc -338 if x == -901      |
| cie dec -630 if x >= -910    |
| cie dec -716 if ie < -5737   |
| wf inc 613 if wf <= -1678    |
| s dec -409 if bs <= -3539    |
| rfw inc -505 if d < -3432    |
| bok inc 912 if bs == -3529   |
| isy inc -992 if mxg > 2525   |
| bok dec 100 if tss <= 2196   |
| s inc 712 if s > 1520        |
| cie dec -381 if brr != -4465 |
| brr dec 793 if cie > -1099   |
| bok dec -387 if bok < 2283   |
| s dec 812 if mxg > 2520      |
| hsn dec 422 if isy >= 2519   |
| brr dec -597 if wf <= -1063  |
| tss inc -539 if h == 1119    |
| d dec 159 if hsn == -1382    |
| h dec 474 if wf <= -1067     |
| h dec -34 if vso < 3161      |
| rxb inc 714 if pf != 936     |
| wf dec -564 if pf > 926      |
| d inc 534 if erb >= -781     |
| h inc 808 if j == -982       |
| brr inc 976 if qn == 2509    |
| o dec 623 if rfw > 201       |
| hsn dec -794 if h < 1492     |
| uxr inc 649 if mxg <= 2533   |
| cie inc 156 if rak == 3096   |
| j dec -392 if hsn == -588    |
| tss inc -161 if rfw != 213   |
| rfw dec 864 if qn > 2512     |
| d inc -499 if cie == -950    |
| rxb inc -849 if rfw > 203    |
| x inc -478 if pf == 939      |
| j inc -343 if uxr > 5194     |
| qn inc 504 if d < -4087      |
| pf inc -430 if s > 1423      |
| o inc -709 if x <= -911      |
| mxg inc 594 if rxb != 824    |
| h dec -885 if h == 1487      |
| brr inc -663 if bok <= 2657  |
| tss inc 504 if bs != -3532   |
| brr inc -100 if s < 1432     |
| bs inc 133 if rfw == 206     |
| hsn inc 535 if rfw >= 200    |
| hsn inc -82 if h != 2372     |
| mxg dec 254 if rak != 3090   |
| wf inc -401 if o <= -1513    |
| d dec 577 if qn < 3019       |
| qn inc 94 if bok > 2660      |
| pf dec -990 if ie <= -5732   |
| bok dec 181 if cie < -945    |
| qn dec 431 if bok <= 2489    |
| mxg inc 128 if qn >= 2673    |
| d dec -233 if tss > 1996     |
| rak dec 364 if ie != -5732   |
| tss inc 174 if o == -1521    |
| tss dec -463 if isy != 2530  |
| rak inc -238 if bs >= -3403  |
| brr dec 447 if j == -933     |
| ie dec 853 if cie > -952     |
| bs dec 350 if bs < -3393     |
| brr dec -996 if d <= -4434   |
| cie dec -749 if tss < 2634   |
| mxg inc -484 if bok == 2484  |
| vso dec -135 if x == -899    |
| d inc -426 if rxb < 832      |
| h dec -40 if uxr != 5199     |
| rak inc -480 if brr == -2445 |
| h inc 818 if s == 1428       |
| hsn dec -708 if hsn < -51    |
| rfw inc -155 if rxb != 838   |
| pf inc -3 if o < -1511       |
| qn dec -144 if ie <= -6579   |
| hsn dec 166 if s > 1418      |
| rfw inc 216 if bok == 2484   |
| h inc 65 if isy <= 2523      |
| uxr inc -405 if ie <= -6592  |
| h inc -85 if wf <= -896      |
| rfw dec 104 if s == 1428     |
| ie dec -144 if vso != 3157   |
| ie dec -877 if rfw < 156     |
| uxr dec 836 if isy >= 2514   |
| mxg inc -753 if uxr >= 4358  |
| j inc -695 if x >= -901      |
| rak dec -399 if wf >= -910   |
| d dec 289 if vso != 3157     |
| hsn inc 482 if j == -1628    |
| rfw dec 10 if bs >= -3741    |
| vso inc 803 if d != -4864    |
| vso inc -335 if qn == 2820   |
| o dec 527 if rak != 2776     |
| tss dec 799 if rfw > 170     |
| j dec -763 if hsn > 967      |
| tss dec 259 if pf <= 1498    |
| wf inc -260 if rxb <= 820    |
| x inc -560 if hsn < 980      |
| j inc 126 if wf <= -898      |
| uxr inc -665 if j != -736    |
| vso inc -59 if h >= 3170     |
| j dec 88 if isy < 2528       |
| brr inc 622 if uxr < 3692    |
| wf dec -81 if isy >= 2521    |
| rfw inc 497 if tss > 2370    |
| d inc 411 if erb <= -789     |
| cie inc -375 if mxg == 1761  |
| bok inc -998 if hsn <= 972   |
| pf inc 224 if mxg != 1757    |
| x inc 551 if rxb <= 835      |
| qn inc -388 if brr != -2442  |
| rfw inc -79 if rak < 2779    |
| hsn dec 756 if j > -831      |
| wf dec -67 if ie > -6589     |
| hsn dec -175 if tss < 2381   |
| tss dec -861 if rak == 2777  |
| o dec -461 if rak >= 2772    |
| rxb dec 916 if erb <= -795   |
| pf dec 379 if erb == -789    |
| isy inc -155 if bok == 1486  |
| erb dec 790 if o == -1587    |
| brr inc 445 if tss < 3242    |
| rxb inc 884 if hsn > 394     |
| tss dec 591 if x == -913     |
| j dec 298 if cie == -1325    |
| ie dec -68 if mxg <= 1764    |
| mxg dec 387 if vso < 3570    |
| tss dec -86 if bs != -3748   |
| rxb inc 238 if hsn >= 390    |
| rak inc -28 if bok == 1486   |
| rak inc -640 if mxg == 1374  |
| qn dec -83 if tss >= 3314    |
| tss dec -238 if bok != 1476  |
| tss dec -101 if o != -1587   |
| hsn dec -537 if tss == 3561  |
| wf inc -859 if brr == -2000  |
| tss inc -35 if uxr >= 3698   |
| cie inc -970 if rak <= 2112  |
| rfw inc 971 if h < 3172      |
| wf dec 887 if rfw < 1555     |
| bok inc 20 if o <= -1592     |
| mxg inc -326 if cie > -2298  |
| mxg inc -684 if j > -1116    |
| brr inc 639 if qn >= 2510    |
| rxb dec -332 if rxb < 1069   |
| uxr dec 189 if brr > -1369   |
| rak dec -567 if rfw == 1552  |
| cie dec 407 if uxr > 3505    |
| h dec -365 if o < -1585      |
| cie dec -990 if s == 1428    |
| rfw dec 368 if ie == -6517   |
| vso dec -76 if wf != -2502   |
| erb inc 334 if bs >= -3747   |
| o inc 583 if qn == 2515      |
| pf inc 7 if rxb > 1399       |
| o inc 166 if qn >= 2512      |
| wf inc 492 if x <= -905      |
| uxr inc -566 if d == -4452   |
| bok inc -919 if isy >= 2364  |
| hsn inc 517 if rak != 2677   |
| j dec -916 if d != -4454     |
| bok dec 116 if rak > 2674    |
| vso dec -477 if x < -907     |
| qn dec -964 if erb == -1245  |
| j dec 987 if qn > 3478       |
| rak dec 317 if d < -4442     |
| isy dec 1 if cie > -1717     |
| j dec 95 if mxg == 1046      |
| h dec -927 if s <= 1435      |
| o dec 812 if ie >= -6518     |
| brr inc -499 if uxr >= 2936  |
| rak dec 716 if cie == -1712  |
| x inc 482 if pf == 1350      |
| cie inc -272 if mxg != 1049  |
| isy inc -839 if brr == -1870 |
| o inc -259 if erb <= -1239   |
| j dec 859 if x != -910       |
| isy inc 493 if tss != 3521   |
| rxb dec -673 if mxg >= 1043  |
| vso dec 35 if uxr <= 2947    |
| rxb dec -128 if bok < 459    |
| bok inc 645 if isy >= 2853   |
| bok inc 384 if s < 1430      |
| h inc -709 if brr != -1865   |
| o inc 638 if cie != -1980    |
| rak dec 9 if pf != 1345      |
| erb dec -772 if rfw != 1176  |
| ie inc -817 if rfw == 1184   |
| vso dec 21 if ie == -7334    |
| s inc -829 if uxr > 2936     |
| isy inc -205 if cie <= -1984 |
| mxg dec -404 if o == -1271   |
| x inc 633 if mxg < 1462      |
| vso inc 795 if bok <= 1481   |
| cie inc 613 if h == 3753     |
| s inc 156 if qn != 3478      |
| wf inc 908 if erb > -467     |
| x inc -340 if j < -1191      |
| bok dec -790 if uxr > 2940   |
| d inc 588 if vso >= 4774     |
| ie dec 711 if rxb < 2209     |
| j dec -687 if isy >= 2657    |
| brr inc -979 if bok == 2270  |
| uxr dec -130 if isy < 2649   |
| h inc -403 if pf == 1341     |
| pf dec -156 if ie == -8045   |
| o dec 828 if bok <= 2276     |
| bs inc -379 if d != -3864    |
| vso inc 570 if isy != 2654   |
| brr dec -208 if brr > -2837  |
| d dec 364 if wf != -2005     |
| pf inc -459 if d <= -4219    |
| wf dec 449 if tss != 3536    |
| s dec -477 if wf >= -2464    |
| j dec 366 if vso == 4782     |
| s dec 240 if rxb != 2201     |
| hsn dec -892 if h > 3752     |
| ie dec -551 if o <= -2098    |
| wf inc -574 if tss < 3531    |
| s dec -972 if isy >= 2664    |
| isy dec -632 if pf <= 1042   |
| uxr inc -733 if vso > 4779   |
| bok inc -541 if o == -2099   |
| pf inc -723 if cie >= -1378  |
| brr inc 993 if isy != 3285   |
| isy inc -859 if brr == -1851 |
| qn inc -925 if rfw != 1184   |
| brr dec 118 if j != -1572    |
| rak inc -711 if hsn <= 2343  |
| o dec 896 if rfw <= 1184     |
| qn inc -332 if h <= 3759     |
| rak dec -684 if mxg == 1452  |
| qn dec 945 if uxr <= 2216    |
| d inc 971 if rfw < 1189      |
| bok dec -80 if o != -2995    |
| hsn dec 288 if uxr >= 2219   |
| x inc -986 if bok > 1725     |
| o inc -640 if tss > 3527     |
| rak dec -210 if isy == 3287  |
| qn dec -937 if j > -1570     |
| d dec -796 if ie >= -7497    |
| rfw dec 869 if d != -2456    |
| j dec 941 if erb == -473     |
| vso inc -366 if j > -2509    |
| h inc -526 if d != -2461     |"""

indata = """js inc 257 if wn < 9
jq dec -586 if esb != -3
gcf inc -603 if i >= -9
gcf dec -300 if d != 1
g inc -973 if gy > -1
epp dec -79 if rjx < 9
x dec 796 if esb == 0
d inc -526 if rf < 3
qc inc -610 if dma > -8
gcf dec 831 if aqr > 5
wow dec -705 if jq >= 583
gcf dec 135 if esb < 10
gcf inc -777 if aqr != 8
esb inc 262 if rjx > -10
x inc 259 if dma > 3
g dec -784 if rjx != -2
rjx inc -969 if yzp > -3
wow inc -401 if g < -182
dma inc 995 if rjx <= -962
vyy inc 290 if g >= -194
vyy inc 4 if gy == 0
vyy dec -295 if wow >= 314
j dec 476 if j >= -8
u inc 84 if g < -195
g inc -422 if gy == -4
yzp dec -523 if cty == 0
cn dec -938 if g > -195
u dec -652 if g <= -193
aqr dec 829 if qc < -601
u dec 199 if wow < 309
aqr dec -409 if rf >= 9
dma dec -556 if dma > 990
qc inc 134 if i != 0
qc inc 238 if j >= -476
yzp dec 810 if js < 255
i dec 898 if i == 0
g inc 898 if tyg <= -5
j dec -130 if aqr == -832
tyg inc -504 if l > -7
aqr dec 465 if l >= -9
gcf dec 64 if jq != 595
wow inc -102 if yzp >= 515
rf inc -433 if i == -898
rjx inc -334 if l >= -6
rf inc -395 if cn <= 947
u inc -724 if qc < -376
epp inc 309 if gcf >= -1281
zp dec -367 if cty >= -5
aqr dec 265 if aqr <= -1287
u inc 359 if wn == 0
vyy inc 587 if aqr != -1550
uxa inc -541 if u <= 162
js inc 720 if wow >= 195
d inc -857 if wn > -3
cty inc 958 if gcf == -1279
rf dec 153 if x >= -804
cn dec -921 if dma <= 1560
zp inc -554 if qc > -381
jq dec 83 if x < -799
qc dec 912 if cty < 968
i inc -636 if tyg == -504
rjx dec 113 if aqr >= -1566
js inc -184 if wow > 198
qc inc -519 if cty != 958
aqr dec 281 if u > 166
aqr inc 392 if vyy <= 887
cn inc -179 if rjx > -1420
g inc -16 if cn != 1680
d inc 260 if uxa != -541
j inc -873 if yzp < 522
rjx inc 737 if g >= -191
wow inc 288 if qc >= -1287
j inc -844 if wn > 5
i inc 91 if uxa > -546
yzp inc -12 if d == -1383
cn dec -247 if zp >= -189
i dec -246 if dma == 1551
qc inc -919 if gy >= -3
cn dec -804 if esb < 270
uxa inc 593 if qc != -2197
yzp inc -562 if esb <= 264
rjx inc 850 if zp < -181
u dec 944 if j != -486
vyy inc 970 if vyy >= 881
gy inc 659 if u < -779
aqr dec 145 if esb == 262
yzp inc 346 if gcf == -1282
wow inc 112 if gcf != -1279
vyy inc -120 if rjx == 171
esb dec -795 if qc >= -2210
cty inc -282 if zp == -187
uxa dec -683 if l == 0
epp inc -185 if jq >= 589
js inc 542 if cn != 2741
gy inc 591 if d == -1383
wow inc -734 if rf != -987
wow dec 482 if vyy <= 1739
uxa dec 231 if u >= -785
gy dec -153 if d != -1385
dma inc 682 if js > 1330
wn dec -173 if i < -1196
tyg dec -510 if dma > 2230
aqr inc 309 if gcf <= -1289
gcf inc 831 if g > -190
g dec -457 if qc == -2203
aqr dec -682 if gcf != -447
cn dec 75 if js > 1328
vyy inc -639 if cn >= 2666
j dec 119 if uxa != 499
i inc -312 if gy > 1399
rjx dec 145 if aqr != -634
cty dec -600 if wow == -726
dma inc 79 if zp < -179
vyy inc 285 if jq <= 586
tyg inc 34 if d < -1379
u dec -320 if yzp != -44
esb inc -229 if wow >= -730
gy dec 175 if cn != 2659
gy inc 87 if js <= 1334
wn dec 725 if rjx < 35
cty dec -64 if gy == 1228
tyg inc 809 if gcf != -438
zp dec -526 if uxa > 500
rjx inc -520 if wow > -727
gy inc 608 if cty > 1345
u inc -847 if cn == 2656
dma inc -728 if zp < 343
qc dec -722 if wow > -734
gy inc -864 if wn != -552
l dec -53 if cn == 2656
rjx dec -674 if gcf > -446
i dec 647 if jq == 586
dma inc -109 if cty <= 1349
d dec -263 if j == -595
rf dec 835 if rf < -972
esb inc 504 if js >= 1332
uxa dec -215 if wow > -732
l dec 240 if qc != -1472
tyg inc 754 if aqr > -639
d dec -784 if d > -1129
u dec 528 if dma == 1482
x dec 569 if aqr != -636
uxa dec -163 if yzp < -49
qc inc -88 if x != -1365
gy inc -966 if yzp <= -43
cn inc 870 if gy == 262
x dec -511 if gy > 263
qc dec -245 if epp >= 380
rf dec -718 if vyy >= 2018
aqr inc 494 if u != -1302
esb dec 211 if wow < -734
esb dec -284 if epp > 379
x inc 354 if x >= -1372
g dec 378 if cty != 1349
wow dec -405 if js < 1338
tyg dec 615 if yzp != -51
rf inc 475 if dma == 1475
gy dec 15 if aqr <= -132
zp inc 915 if zp != 335
d dec 323 if wn >= -553
g dec -525 if cn != 3517
l dec -13 if gy <= 248
gy dec -687 if i != -2147
tyg inc -487 if gy == 934
rjx dec 444 if vyy == 2014
wn inc 449 if yzp < -46
cn inc 651 if rf != -1337
zp dec 888 if jq >= 578
uxa dec 966 if esb > 1616
wn dec -219 if tyg != 1109
dma inc 599 if cn > 4176
x inc -486 if epp >= 387
l inc -404 if yzp != -43
rjx dec -996 if aqr > -142
g dec 215 if dma == 2079
aqr dec -746 if i > -2159
gcf dec -301 if cn >= 4174
qc inc -700 if vyy == 2016
rjx dec 289 if d >= -661
vyy inc 278 if gcf < -138
g inc 659 if wn != 118
zp inc 622 if l <= -579
zp inc 644 if zp >= 373
aqr inc 468 if gy >= 931
wn inc 608 if zp > 359
js dec 985 if gy <= 942
uxa dec 509 if epp > 383
tyg inc 134 if cty <= 1340
jq dec 677 if dma < 2073
yzp dec -146 if j >= -600
l inc -500 if dma == 2072
cn inc 399 if cty <= 1341
rf inc 521 if wow != -321
gcf dec -70 if wn > 718
gcf dec 946 if tyg == 1250
cty dec 398 if qc == -1936
qc dec -105 if qc > -1936
g dec -16 if g != 1082
cty dec 932 if vyy > 2288
gcf dec -293 if esb != 1616
cn dec 244 if esb >= 1610
rf inc -790 if cn != 4338
dma dec -87 if wn == 724
cn dec -191 if j > -598
aqr inc -246 if d <= -658
cn inc 786 if vyy <= 2297
g dec 211 if qc < -1932
x inc -473 if l >= -587
rjx inc -686 if jq <= 589
dma inc -411 if gcf <= -1019
u inc -596 if qc <= -1933
l inc -60 if rjx > -476
wow dec 910 if zp == 366
gy inc -854 if u != -1916
jq inc -698 if wn <= 729
zp inc 456 if d != -665
x dec -853 if x >= -1964
aqr inc -282 if rjx < -478
tyg inc 975 if cty == 10
js inc -684 if wow >= -1239
uxa dec 702 if g == 879
g inc -602 if tyg <= 2231
cty inc 987 if dma > 1742
gy dec -57 if cn == 5317
zp dec -527 if qc > -1941
tyg dec 689 if g != 282
gcf inc -11 if rjx > -478
epp dec 44 if uxa < -325
aqr dec 936 if i < -2156
i dec -119 if aqr >= 841
yzp dec 46 if uxa > -330
u inc 549 if esb == 1619
zp dec 412 if j >= -598
cn dec -865 if gy < 89
yzp dec 366 if g > 283
j dec 372 if j <= -595
zp inc 879 if tyg > 1532
wow dec 30 if x > -1974
dma dec 288 if j < -966
zp inc -419 if epp == 344
tyg inc 304 if x < -1964
zp dec 77 if j < -960
cty inc -586 if wn < 728
wow inc 271 if wow == -1261
u inc -751 if dma != 1470
wow dec -64 if wn != 727
esb inc 294 if gy <= 75
jq inc -559 if wow > -918
cty inc -283 if gy != 73
cty dec 792 if g != 274
l inc 589 if rjx >= -482
gy inc -659 if jq < -116
cn dec -817 if aqr <= 839
l inc 682 if rjx < -467
l dec -285 if rf <= -2125
qc inc -370 if x < -1961
l dec 582 if yzp >= 47
dma inc -365 if js == -334
js inc 397 if d == -659
g inc 902 if aqr <= 840
x inc 129 if rf >= -2139
g dec -704 if gcf < -1041
cn inc 207 if uxa > -332
epp dec 517 if js < 70
cn dec 125 if qc <= -2305
x inc -187 if tyg > 1844
gy dec -1 if cty < -661
js inc -224 if qc != -2306
x inc -627 if gcf <= -1025
yzp inc -426 if g < 1186
uxa dec -839 if wow >= -933
u inc 688 if gy <= 87
jq dec -453 if aqr < 834
tyg inc -370 if d >= -660
l dec 81 if gy != 89
zp dec -184 if uxa == 510
gcf dec -97 if gcf == -1034
tyg inc -508 if x != -2468
cty inc 89 if j < -960
jq dec 416 if rf >= -2132
rf inc -846 if cty >= -577
uxa dec -315 if vyy <= 2294
g inc -191 if vyy == 2294
js dec -557 if wow == -934
u dec 382 if qc >= -2313
dma dec -841 if wow > -929
u dec 6 if dma < 1932
aqr inc 75 if js == 63
jq inc 640 if gcf < -928
wn inc -992 if j != -967
uxa dec -577 if wn != 726
g inc -458 if rjx < -467
epp dec 141 if x == -2468
l inc 617 if cty < -576
gy dec 542 if yzp != -377
cty dec -99 if uxa < 1410
tyg inc -358 if g > 521
wn dec 514 if uxa <= 1401
dma inc 110 if j > -960
js inc -359 if jq <= 569
epp dec 266 if epp < -312
x inc -473 if jq > 557
vyy inc 890 if wn == 730
zp dec 379 if gcf != -932
u dec 46 if jq == 565
tyg inc -410 if l != 256
i inc -320 if js != -303
l dec 670 if i >= -2482
i inc 788 if u < -2391
l inc 23 if cty == -476
tyg inc -364 if rf <= -2969
gy dec 394 if epp >= -584
esb dec 645 if aqr != 907
epp inc -842 if x < -2935
js dec -289 if l == -392
tyg inc -405 if gcf == -937
vyy dec -58 if epp == -1419
gy dec 110 if u == -2398
vyy dec -789 if epp > -1426
qc dec 463 if zp >= 1117
gcf inc 859 if esb == 1616
u inc -99 if js < 2
epp inc 111 if tyg == -67
jq inc -536 if d < -661
js inc 506 if dma <= 1936
rjx dec -58 if j >= -971
wn dec -513 if tyg <= -64
wow dec 816 if aqr >= 902
gcf inc -957 if x == -2941
uxa dec -39 if yzp <= -377
wn inc 824 if g <= 531
gcf dec 927 if l >= -394
x dec -655 if l == -392
g inc 767 if tyg > -59
dma inc -493 if epp != -1318
esb inc -587 if epp >= -1318
wow inc 996 if cty >= -479
l dec 119 if epp != -1311
gy dec -935 if uxa < 1444
gcf dec -428 if zp >= 1121
js inc -999 if x > -2293
uxa dec 438 if epp != -1305
gcf dec -623 if yzp <= -380
j inc -256 if gcf < -1530
l inc -183 if d >= -662
wn dec 945 if x < -2279
i inc 953 if epp == -1311
vyy inc -434 if js > -1016
yzp dec -695 if epp < -1308
d inc 975 if l == -575
uxa dec -218 if j < -1216
gcf inc 413 if tyg == -67
wow inc -380 if zp != 1125
cn dec 166 if wn > 1113
rjx dec 878 if l != -581
esb inc -745 if g <= 531
aqr dec 14 if esb < 292
j inc 405 if jq == 565
vyy inc 657 if wn == 1124
j dec -624 if qc > -2763
rf inc -711 if esb < 289
uxa inc 453 if gy >= 512
i inc 593 if js >= -1009
qc inc -413 if j > -826
tyg inc -395 if epp == -1311
cty dec -911 if g >= 524
yzp inc -259 if esb >= 277
dma dec -812 if vyy > 2643
wow inc 887 if gcf >= -1121
uxa inc 906 if rf < -3686
l inc -816 if js > -1002
aqr inc -123 if tyg >= -462
x inc 413 if uxa < 2590
tyg dec -141 if wow <= 142
cn inc -138 if gcf > -1118
i inc 665 if wn < 1117
wow inc -250 if gy > 505
wow inc 751 if l != -569
j inc 334 if x >= -1879
i inc -963 if uxa >= 2575
uxa dec -395 if wn == 1106
dma dec 130 if esb != 290
l inc 171 if zp > 1122
esb inc 288 if uxa < 2576
wn inc -672 if i > -445
uxa inc -593 if jq == 565
cty inc -247 if yzp >= 52
vyy inc 480 if cn == 6907
js dec -402 if uxa <= 1982
l dec -121 if cn < 6913
rjx dec 692 if i <= -433
g inc 827 if cty >= 186
d inc -333 if i >= -449
zp inc 438 if u > -2502
gy dec -418 if cn >= 6902
x dec 665 if uxa != 1980
zp dec 497 if l == -283
i inc -51 if rf >= -3694
dma dec -792 if gy < 931
dma dec -189 if wn <= 435
cty dec 337 if g != 1347
zp inc -436 if dma == 2919
yzp dec -184 if rjx <= -1980
gcf inc 688 if qc <= -3174
u inc -536 if zp <= 636
d dec 31 if rjx != -1989
esb dec 523 if wow >= 651
gy inc 566 if zp >= 632
vyy dec 190 if zp == 630
tyg inc 53 if i < -486
x dec -543 if i < -482
uxa dec 403 if epp != -1319
i inc 880 if u == -3033
wn dec 172 if gcf < -428
qc dec 316 if cn > 6904
gcf dec 864 if rf == -3688
esb inc -344 if uxa <= 1583
i inc -234 if js >= -1006
x dec -306 if d < -45
vyy inc -256 if rjx >= -1983
u dec -498 if epp > -1309
esb inc -915 if u == -3033
i inc 910 if esb < -624
l dec 781 if qc > -3505
g dec 803 if u < -3032
dma dec 392 if u == -3033
cty inc 216 if vyy != 2929
zp dec 12 if gy == 930
gy dec -35 if tyg >= -269
wow inc 824 if wow != 642
js inc 974 if epp >= -1319
gcf inc 883 if dma != 2527
jq inc 339 if cty != 72
yzp dec 751 if zp != 627
tyg inc 90 if x < -1679
vyy inc -212 if rjx < -1976
wow dec -642 if epp <= -1302
d dec -643 if x <= -1689
i dec -25 if vyy != 2728
js inc -522 if tyg == -178
js dec -880 if epp == -1311
l inc -899 if x == -1689
u dec 459 if g < 563
tyg dec -485 if i > 1083
zp dec -944 if dma < 2537
cn inc 867 if cty > 57
i dec -95 if jq == 904
gcf dec 548 if d == 595
gcf inc 35 if aqr >= 766
x inc -420 if yzp != -501
x inc -308 if yzp == -500
vyy inc -407 if l <= -1961
gy inc -623 if j < -476
u inc -932 if g > 547
zp dec 18 if js > 324
g dec 776 if cn > 7771
jq dec 581 if cn == 7764
zp inc 392 if g < -215
vyy inc -266 if i < 1185
tyg inc 600 if jq < 906
wow dec 480 if aqr != 770
yzp dec -97 if j <= -488
cn dec 212 if wow == 1284
vyy dec -247 if rjx == -1992
x dec -13 if uxa != 1584
wow inc 929 if vyy < 2330
qc inc 515 if vyy != 2313
wow dec -484 if u <= -4424
wn dec -251 if wow > 2699
dma inc 128 if d > 585
epp inc -429 if cn > 7564
tyg inc 401 if gy < 344
dma inc -757 if qc == -2975
rjx inc 124 if tyg == 1308
j dec -258 if wn < 279
zp inc 265 if u != -4431
epp dec -850 if epp <= -1308
jq inc 875 if cty > 64
esb dec -585 if yzp <= -509
qc inc -663 if vyy != 2313
cn dec 194 if rf < -3682
i inc -821 if rjx > -1862
qc dec -768 if i != 354
rf inc 949 if gcf != -1805
wow inc -350 if gcf == -1807
l dec -72 if dma <= 2663
qc inc -201 if x <= -2106
cty dec -576 if esb == -631
uxa dec 387 if i >= 358
uxa inc 189 if uxa >= 1193
i dec 193 if qc > -3089
gcf inc -164 if wow == 2697
aqr inc -154 if cn < 7364
dma inc 145 if j < -228
cn inc -314 if rf > -2749
qc dec 976 if yzp > -509
tyg dec -277 if j == -226
l dec -339 if yzp < -501
qc dec -615 if js > 320
x inc -678 if rf >= -2743
rjx inc -777 if g > -228
rf dec 151 if vyy <= 2320
js dec 591 if u <= -4422
i inc 166 if d != 585
cn inc -615 if esb < -634
qc dec -148 if dma > 2649
gy dec -93 if d == 595
esb dec 265 if js < -256
wn inc 784 if x != -2795
rf inc 123 if yzp < -499
tyg inc 51 if rf <= -2777
dma inc 273 if tyg != 1575
g dec 546 if uxa == 1386
j inc 787 if l < -1546
rf inc 97 if qc <= -3289
x inc 621 if uxa <= 1388
cn inc -760 if esb <= -894
jq inc -89 if zp <= 2197
uxa dec -485 if wow == 2697
j inc 971 if rjx == -2638
rjx inc 117 if l != -1552
yzp inc -335 if wn < 1059
gy dec -871 if j <= 1541
tyg dec -602 if yzp != -852
rjx dec -852 if cn > 6293
g dec 893 if cn > 6293
uxa inc -524 if cn > 6297
yzp inc 389 if i < 347
epp dec -502 if rf > -2667
dma dec 323 if yzp > -453
l inc -921 if wow <= 2706
yzp dec -534 if jq > 1777
yzp dec 94 if rjx != -1784
uxa inc 254 if vyy != 2320
i dec 224 if gy <= 1313
u inc -466 if vyy < 2318
epp dec -751 if cn <= 6299
qc dec -316 if tyg >= 2197
d inc -666 if epp == 290
g dec -398 if js != -274
rf dec 482 if cn == 6304
vyy inc 295 if cty == 643
wn dec -540 if i != 108
qc inc -334 if wow != 2691
d dec 315 if dma < 2935
qc dec -860 if d != -385
qc dec -202 if gy > 1296
wow dec -67 if vyy > 2610
esb dec 880 if vyy != 2621
cn inc -985 if d <= -383
epp inc -435 if g == -1263
gcf dec 559 if u != -4419
aqr dec 979 if yzp >= -23
jq inc 905 if wn < 1597
cn inc -679 if x >= -2165
rf inc -590 if j != 1532
l dec -73 if wn <= 1598
qc dec 804 if d > -388
j inc 42 if zp < 2198
tyg dec -636 if qc < -3366
gy inc 209 if vyy != 2613
l inc -725 if x < -2158
qc inc -54 if j >= 1531
cty inc 896 if js < -258
u dec -718 if d <= -377
l dec 654 if esb >= -1785
dma dec 912 if i <= 120
uxa inc 827 if cty <= 1543
rf dec -871 if g >= -1271
uxa inc -77 if tyg > 2814
d inc -59 if i <= 121
dma dec 792 if cn == 5309
zp inc 930 if yzp >= -15
gy inc -956 if d == -435
wn dec -205 if j <= 1540
d dec -830 if cty >= 1536
tyg inc -552 if u != -3700
rf inc -616 if gcf != -2533
yzp dec -87 if rf >= -1793
uxa inc -886 if dma <= 1226
g inc 278 if uxa < 1741
j dec 1 if vyy > 2614
d dec 899 if rjx == -1786
rjx dec 238 if vyy >= 2606
cn inc -663 if d <= -505
rjx inc -805 if l != -3785
tyg dec 610 if aqr != -206
gcf inc 842 if yzp <= -12
tyg dec 361 if l <= -3772
wow inc 717 if dma != 1219
vyy dec 182 if gcf != -1695
l inc -972 if vyy >= 2428
cn dec -106 if gy <= 1517
g dec 598 if cn >= 4749
l dec 653 if rf <= -1808
epp dec -768 if esb != -1781
rf dec -566 if uxa != 1740
aqr inc 639 if cn == 4752
wn inc -877 if u == -3699
uxa dec -7 if vyy >= 2427
yzp dec -107 if qc != -3430
yzp inc -426 if esb <= -1776
epp inc 102 if x < -2164
u dec 396 if jq == 2684
dma dec -6 if jq <= 2686
cn inc -739 if gcf > -1698
gcf inc 470 if cty == 1539
gy inc 781 if vyy != 2433
vyy dec 238 if dma < 1236
wow inc 670 if wn != 1801
i dec -230 if jq < 2686
wn dec -500 if wow == 3481
wow dec 865 if j < 1536
x inc -733 if jq == 2684
cty dec 531 if gy >= 1513
g inc 399 if esb < -1768
x inc 201 if rf == -1233
cn inc 394 if d < -515
epp inc -953 if wow >= 2615
qc inc -639 if u != -4095
i inc 935 if vyy > 2191
g inc 846 if gcf != -1218
epp dec 89 if yzp > -334
qc dec -143 if epp >= -317
gy dec 256 if zp != 3132
tyg inc 545 if rjx > -2831
cn dec 913 if gcf != -1226
esb inc -410 if d == -514
rjx dec -71 if tyg <= 1849
rjx inc -127 if yzp > -336
jq inc -206 if gcf >= -1221
i dec -800 if gcf > -1225
aqr inc 98 if gy < 1263
gcf dec 163 if gcf <= -1213
cty dec -965 if zp == 3131
rjx dec -969 if cty < 1976
uxa inc 51 if x == -2698
u dec -380 if wow == 2616
tyg dec -715 if rjx >= -1922
zp inc -825 if yzp >= -323
zp dec 292 if x > -2702
esb inc -415 if d <= -505
wn inc -240 if esb > -2609
gy inc 882 if rf == -1233
vyy dec -638 if gcf <= -1384
tyg dec -63 if jq <= 2479
dma inc -38 if uxa < 1797
qc inc 289 if wow < 2619
d inc 342 if yzp >= -330
cty inc 650 if js < -271
l inc -129 if esb == -2601
jq inc 453 if j > 1531
esb dec 11 if i > 2084
wow inc -729 if wow < 2620
x inc 132 if uxa <= 1796
l dec 818 if vyy <= 2832
tyg dec 804 if yzp != -334
wow inc 285 if rf != -1233
zp dec -329 if wn != 2061
u inc 720 if js == -265
gcf inc 85 if aqr != 528
wow dec -303 if jq != 2472
vyy inc -366 if cty < 1965
yzp inc 598 if cty == 1973
rf inc 685 if jq >= 2471
vyy inc -385 if jq <= 2487
aqr inc 103 if esb >= -2598
d inc 427 if uxa == 1793
rjx inc -736 if zp < 2849
x dec -991 if esb <= -2600
gy inc 642 if gcf <= -1391
yzp dec -726 if wow < 2195
zp dec -582 if u == -3002
rf dec -354 if cn > 3093
g inc -150 if g != -342
uxa inc -381 if wn >= 2060
wow inc -145 if qc < -3628
g inc 589 if qc <= -3626
jq dec -643 if js == -265
yzp dec -768 if cty == 1973
vyy dec 448 if aqr <= 533
uxa dec 507 if cn <= 3103
gy dec 134 if aqr >= 521
x dec 868 if rf != -194
gcf inc 355 if cn >= 3093
rf dec 639 if tyg == 1822
gcf inc -671 if wow >= 2048
jq inc 615 if gy != 2012
zp dec -910 if cn < 3096
rjx inc 949 if wow < 2055
esb dec 623 if jq != 3731
g dec -799 if qc != -3634
uxa inc -352 if rf >= -196
gcf dec 229 if jq != 3729
zp inc 785 if rf > -200
i dec 150 if gcf < -1251
gcf inc -463 if dma != 1189
j inc -424 if wn == 2061
l inc 412 if gcf <= -1715
aqr inc -646 if u <= -2994
i inc 195 if l <= -4471
rjx inc 291 if cty < 1982
epp dec 459 if dma != 1198
u inc -909 if vyy > 1998
uxa dec -208 if vyy > 1994
u dec 727 if i == 1928
x inc -402 if l == -4468
u inc -459 if cn > 3095
j inc 253 if jq < 3733
vyy dec -143 if rf > -204
rjx dec -560 if tyg < 1822
cn dec -602 if jq > 3732
wow dec -231 if wn >= 2066
js inc -40 if x > -1972
gcf dec 591 if rjx >= -842
wn inc -612 if u <= -5090
vyy inc 60 if j >= 1100
cty dec -207 if tyg == 1819
wow dec -862 if dma < 1197
cn dec 534 if i <= 1936
d dec 380 if wow == 2907
x inc 48 if dma < 1199
yzp inc 955 if dma != 1191
dma inc -372 if l <= -4467
uxa dec 83 if wow != 2909
u dec 383 if u > -5102
cn dec 691 if cn <= 3169
vyy inc 952 if jq == 3733
j dec -231 if wn < 1444
i dec -988 if x >= -1931
cn dec -459 if x > -1936
js inc -714 if epp != -779
gy dec 751 if cn <= 2936
epp inc -45 if vyy != 2203
aqr dec -251 if i != 2916
zp dec -248 if x == -1929
vyy dec -917 if tyg > 1814
l inc 906 if rjx > -855
wn dec -262 if aqr >= -120
js inc -293 if j >= 1108
g inc -507 if uxa < 671
tyg dec 848 if uxa < 680
tyg inc 449 if cn != 2931
jq inc 43 if d >= -474
uxa dec 510 if rjx != -852
u dec -15 if cn <= 2936
rf dec 467 if uxa < 688
dma dec 40 if j < 1114
cn inc 256 if l > -3564
uxa dec -193 if cty <= 2173
cn inc 472 if epp <= -773
g dec 509 if qc != -3621
x dec -909 if wow >= 2902
j inc 809 if rf > -663
epp inc 458 if x > -1028
cty dec -210 if wn > 1707
wn dec 778 if rjx <= -848
zp inc 745 if l == -3570
dma inc -86 if rjx != -852
dma inc -964 if aqr > -126
x inc -741 if wow == 2909
cn inc -751 if esb <= -3217
cty dec 910 if qc >= -3636
gcf inc 496 if epp >= -321
rf dec -516 if epp >= -322
dma inc -112 if dma <= -187
yzp dec -376 if zp >= 4451
js dec -829 if qc >= -3629
rf inc -310 if dma > -188
gy inc -312 if wow >= 2899
cn dec 889 if dma > -186
g inc 667 if uxa > 682
u inc 201 if u != -5462
cty dec 589 if yzp > 3082
gy inc -274 if wow != 2907
u dec -533 if tyg == 1420
zp inc 937 if d >= -469
jq dec 18 if cn == 2024
cn dec -59 if rjx <= -850
dma dec -172 if x > -1026
jq dec 129 if gcf > -1231
wn dec 957 if jq < 3627
uxa dec -989 if wn <= 939
jq inc -390 if x != -1013
js inc 251 if g < 385
jq inc -572 if tyg <= 1424
g inc -265 if vyy > 3122
rjx inc 789 if x > -1025
gcf dec -838 if d < -465
g dec -564 if gcf != -387
vyy dec -188 if yzp != 3087
i dec 912 if x < -1015
cty inc -768 if x <= -1019
wn dec 175 if wow == 2906
wow inc 534 if qc > -3627
js inc 247 if x >= -1026
vyy dec 894 if gy == 944
x inc -150 if rf != -445
dma dec 766 if wn < 932
gcf dec -53 if zp >= 5383
g dec 9 if u >= -4740
yzp dec -425 if vyy < 2423
aqr inc 407 if vyy > 2406
gcf inc -244 if tyg != 1429
i inc 120 if i <= 2010
cty dec -40 if rf == -455
x dec -433 if wow <= 2900
u dec -553 if cty != 162
jq dec 329 if u <= -4177
aqr dec -319 if g > 387
esb dec 259 if wow > 2904
jq dec -590 if vyy < 2415
tyg dec -211 if d == -467
rjx dec -209 if l != -3561
tyg inc -564 if aqr >= 281
aqr dec -860 if u != -4186
wn inc -298 if g >= 387
x inc -951 if i < 2122
j inc -141 if cty >= 163
l inc 780 if wow != 2910
zp dec 796 if esb > -3491
j dec 652 if qc < -3628
cn dec 101 if i <= 2128
cty inc -169 if gcf < -573
dma dec -544 if epp <= -309
vyy dec -261 if zp <= 4598
rf inc 166 if esb == -3487
aqr dec 865 if rf == -455
u dec -14 if rjx <= 148
vyy inc -518 if dma < 538
aqr dec -30 if cn <= 1988
rf dec 818 if wow <= 2912
js inc 116 if l > -2786
jq inc 707 if gy > 939
jq dec -673 if x < -1176
wow dec 94 if rjx >= 141
esb inc -654 if esb > -3488
jq inc 982 if i != 2127
cn inc 479 if i > 2122
js dec 530 if rjx >= 144
wn dec -37 if gcf != -578
esb dec -917 if cn > 2458
l dec 519 if wn > 923
uxa dec 671 if wn == 933
zp inc -269 if cn >= 2457
esb inc -329 if wn == 933
tyg inc -490 if d <= -468
dma dec 817 if wn > 930
cty inc -650 if u != -4164
rf inc 804 if l >= -3309
dma dec 629 if esb == -3549
l dec -588 if epp < -317
zp dec 738 if zp >= 4318
l dec -772 if wn != 924
epp dec -423 if js <= -317
g dec 781 if qc != -3637
uxa inc -540 if tyg > 1062
gcf dec 120 if j != 1127
d inc 294 if wow >= 2819
i inc 108 if u >= -4169
x dec -117 if zp > 3581
i inc -434 if gy > 950
jq dec -749 if zp >= 3587
gcf dec -342 if tyg != 1063
j inc -910 if wn != 932
u inc -353 if rjx > 142
qc inc -478 if esb == -3549
uxa inc -992 if wn != 933
cty dec -628 if gcf == -356
u dec -527 if dma != -916
aqr inc -354 if j >= 211
d dec 633 if x >= -1062
l dec 920 if js != -326
wn dec -122 if j > 203
x dec 907 if gcf == -356
epp inc 112 if epp != 105
wn dec 322 if u >= -3988
j inc 934 if wn != 1055
g inc -366 if uxa >= 448
uxa dec -720 if wn <= 1063
zp inc 8 if gy <= 947
esb dec -199 if epp <= 110
cn dec -122 if j != 220
l dec -810 if g <= -763
cty inc -435 if yzp < 3521
zp dec 615 if i >= 2230
jq dec -445 if uxa != 1170
gy inc -654 if u > -3994
tyg dec 48 if dma == -914
gcf inc -346 if dma < -905
wn inc -660 if zp >= 2980
x inc -242 if esb >= -3359
gy inc 28 if rjx < 154
tyg dec 602 if esb <= -3341
jq dec 380 if l > -2061
i inc 502 if js <= -308
uxa inc -255 if qc < -4109
u dec -617 if l == -2051
rjx inc -864 if esb <= -3347
u dec -465 if vyy == 2157
tyg dec 629 if i < 2740
d inc -28 if u < -2907
epp inc -430 if cn <= 2585
vyy dec -740 if yzp == 3515
js inc 387 if gy > 315
vyy dec 792 if gy >= 310
l inc -89 if wn > 389
qc dec -149 if wow > 2810
gy inc 510 if cn == 2583
d inc 381 if g != -757
x inc 633 if gcf != -694
wn dec -677 if j > 222
wn inc -605 if i >= 2729
zp dec 794 if rf < -474
dma inc -560 if js >= 61
rjx dec -364 if wow <= 2819
jq inc 429 if g != -774
rjx dec -305 if j <= 215
epp inc -254 if tyg <= -219
i dec -106 if qc < -3955
g inc -514 if zp < 2983
dma inc 617 if u >= -2911
gy dec -81 if aqr > -40
g inc -722 if wn < -201
zp dec -46 if tyg >= -210
yzp dec 720 if gy <= 830
cty inc 675 if epp >= -318
qc dec 727 if cn >= 2574
zp dec -458 if wow != 2811
jq inc -547 if yzp <= 2800
uxa dec 443 if l == -2140
x dec 76 if tyg == -212
x inc 11 if aqr != -36
x dec 1000 if aqr <= -37
l dec -384 if gy != 822
u dec -329 if aqr == -40
x inc 432 if wn > -202
uxa inc 530 if tyg < -202
i dec -798 if js < 71
dma inc -503 if i == 3645
dma inc 69 if uxa <= 1264
d dec 571 if js != 70
wn inc 134 if u >= -2588
i dec -813 if rjx > -48
epp inc -735 if cn < 2585
aqr dec -223 if dma >= -790
uxa dec -86 if dma >= -789
cty inc 127 if aqr < 188
cty inc 472 if uxa == 1349
cn inc 780 if cty >= 791
cn dec -528 if rjx == -49
l inc 669 if d != -754
gcf dec 427 if epp != -1052
rf inc 465 if dma >= -797
epp inc 452 if g != -2005
epp dec -922 if i != 3648
wow inc -516 if js != 72
esb dec -623 if epp == 314
wn inc 434 if cn == 3111
rjx inc 698 if yzp == 2794
vyy dec -150 if epp < 319
rjx inc 343 if yzp != 2797
jq inc -390 if gy <= 831
yzp dec 296 if l >= -1093
yzp dec 676 if esb > -2730
js dec 320 if epp < 318
jq inc 44 if g < -1996
esb inc 425 if zp >= 3444
i inc -817 if esb == -2727
cty inc -336 if esb != -2727
epp inc -90 if uxa < 1341
zp dec 554 if epp != 312
js dec -299 if epp != 319
zp dec 92 if wn <= 366
wow dec -443 if rf > -12
gy dec -962 if i < 2825
vyy inc 381 if d > -748
wn dec -212 if js <= 54
esb dec -944 if gcf != -1127
cty dec 985 if j != 211
aqr dec 697 if uxa >= 1340
wow dec 459 if gcf < -1120
i inc 728 if dma >= -796
cty inc -277 if tyg >= -216
rjx inc 279 if aqr == -505
yzp inc -38 if zp >= 2793
zp dec 221 if epp == 314
d dec -628 if x <= -2630
uxa dec -846 if esb == -1783
rjx dec 154 if x <= -2625
l inc 541 if wow >= 2290
wow inc -777 if vyy < 2636
rjx dec -492 if uxa >= 2195
gy inc 881 if yzp < 1791
x dec 24 if l >= -1095
jq inc -82 if x >= -2658
tyg dec 763 if aqr > -519
wn dec -242 if esb < -1773
tyg inc 574 if d == -119
d dec 423 if i > 3540"""


# indata = """b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10"""



rows = indata.split('\n')

regList1 = [re.findall('[a-z]+', i)[0] for i in rows]
funcList = [re.findall('[a-z]+', i)[1].replace('inc', '+').replace('dec', '-') for i in rows]
valList1 = [re.findall('[-\d+]+', i)[0] for i in rows]
regList2 = [re.findall('[a-z]+', i)[3] for i in rows]
boolList = [re.findall('[<>=!]+', i)[0] for i in rows]
valList2 = [re.findall('[-\d+]+', i)[1] for i in rows]


registers = set(regList1)

thisModule = sys.modules[__name__]

for reg in registers:
    setattr(thisModule, reg, int(0))

maxEver = 0

index = 0
for reg1, reg2, val1, val2, boolOp, func in zip(regList1,regList2,valList1,valList2,boolList,funcList):
    evalString = '{} {} {}'.format(globals()[reg2], boolOp, val2)
    funcString = '{} {} {}'.format(globals()[reg1], func, val1)
    if eval(evalString):
        print(rows[index])
        print(evalString)
        print(reg1 + ' = ' + str(eval(reg1)))
        print(funcString)
        globals()[reg1] = eval(reg1+func+val1)
        print(reg1+' = '+str(eval(reg1)))
        if eval(reg1) > maxEver:
            maxEver = eval(reg1)
    index += 1
print(max([globals()[reg] for reg in registers]))
print([globals()[reg] for reg in registers])
print(maxEver)