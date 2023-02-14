
global the,help
the,help = {},""" 
data.lua : an example csv reader script
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE:   data.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -b  --best    coefficient on 'best'        = .5
  -B  --Bins    initial number of bins       = 16
  -c  --cohen   Cohen's small effect test    = .35
  -r  --rest    explore rest* number of best = 2
  -d  --dump    on crash, print stack dump = false
  -g  --go     start-up action            = all
  -h  --help   show help                  = false
ACTIONS:
"""