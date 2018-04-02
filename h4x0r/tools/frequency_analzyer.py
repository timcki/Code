from termcolor import colored

class FrequencyAnalyzer:

    def __init__(self):
        self.dic = {}
        self.module_sign = '>' + colored(' [A] ', 'cyan') + '<'
        
    
    def analyze(self, file_name):
        try:
            with open(file_name) as fil:
                print(self.module_sign, colored('Reading file', 'yellow'))
                text = fil.read()
                print(self.module_sign, colored('Starting frequency analysis\n', 'yellow'))
                for x in text:
                    try:
                        self.dic[x] += 1
                    except:
                        self.dic[x] = 1

                for w in sorted(self.dic, key=self.dic.get, reverse=True):
                    if w == '\n':
                        print(colored('↵', 'yellow'), colored(self.dic[w], 'cyan'))
                        continue
                    print(colored(w, 'yellow'), colored(self.dic[w], 'cyan')) 
                print('\n'+ self.module_sign, colored('Finished frequency analysis', 'yellow'))
        except:
            print(self.module_sign, colored('Couldn\'t open the file', 'yellow'))

