
global the,help
the,help = {},""" 
xpln: multi-goal semi-supervised explanation
(c) 2023 Tim Menzies <timm@ieee.org> BSD-2
  
USAGE: lua xpln.lua [OPTIONS] [-g ACTIONS]
  
OPTIONS:
  -a  --eps     eps for dbscan               = 0.05
  -A  --minpts     minpts for dbscan         = 5
  -b  --bins    initial number of bins       = 16
  -t  --sway    dbscan or original           = original
  -e  --better       better                  = zitler
  -f  --file    data file                    = data/auto93.csv
  -F  --Far     distance to distant          = .95
  -m  --min     size of smallest cluster     = .3
  -M  --Max     numbers                      = 512
  -p  --p       dist coefficient             = 2
  -r  --rest    how many of rest to sample   = 4

  -g  --go      start-up action              = all
  -h  --help    show help                    = false
  -R  --Reuse   child splits reuse a parent pole = True
  -s  --seed    random number seed           = 937162211
  -d  --debug   debug mode on                = false

  -z  --bootstrap   bootstrap                = 512
  -y  --conf   conf                          = 0.05
  -x  --cliffs   cliffs                      = .4
  -w  --cohen   cohen                        = .35
  -v  --width   width                        = 40
  -c  --cliffs  cliff's delta threshold      = .147

"""