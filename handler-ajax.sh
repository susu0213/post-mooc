echo -n  'http://mooc1.chaoxing.com'
bash ajax.sh ${1} ${2} ${3} ${4} |  grep ifr  | cut -d '"' -f 10
