import os
from time import sleep
from examples import cg_md, ind, rmd

class construtor:
    
    def __init__(self, pwd):
        dir = {}
        dir['src'] = 'src'
        dir['tests'] = 'tests'
        dir['docs'] = 'docs'
        dir['abs'] =  pwd #os.getcwd() 

        file = {}
        file['1'] = '/__init__.py'
        file['2'] = '/module1.py'
        file['3'] = '/module2.py'

        test_file1 = '/test_module1.py'
        test_file2 = '/test_module2.py'

        docs_file1 = '/index.md'
        docs_file2 = '/user_guide.md'
        docs_file3 = '/contribution_guide.md'


        dir_src = os.path.join(dir['abs'], dir['src'])
        dir_tests = os.path.join(dir['abs'], dir['tests'])
        dir_docs = os.path.join(dir['abs'], dir['docs'])

        if not os.path.exists(dir_src):
            os.makedirs(dir_src)
            file = open(dir_src + file['1'], "w")
            sleep(1)
            file = open(dir_src + file['2'], "w")
            sleep(1)
            file = open(dir_src + file['3'], "w")
            sleep(1)
            file.close()
            print('Diretório SRC criado com sucesso! ')

        else:
            print(f'Ja existe o diretório {dir["src"]} ')
        
        if not os.path.exists(dir_tests):
            os.makedirs(dir_tests)
            file = open(dir_tests + test_file1, 'w')
            file = open(dir_tests + test_file2, "w")
            print('Diretório TESTS criado com sucesso! ')
        
        else:
            print(f'Ja existe o diretório {dir["tests"]} ')
        
        if not os.path.exists(dir_docs):
            os.makedirs(dir_docs)
            file = open(dir_docs + docs_file1, 'w')
            file.write(ind)
            file = open(dir_docs + docs_file2, "w")
            file = open(dir_docs + docs_file3, "w")
            file.write(cg_md)
            print('Diretório DOCS criado com sucesso! ')
            file.close()
        else:
            print(f'Ja existe o diretório {dir["docs"]} ')

        if not os.path.exists(dir['abs']+'/README.md'):
            file = open(dir['abs'] + '/README.md', "w")
            file.write(rmd)
        else:
            print('Arquivo README.md já existe no diretório!')
    
        if not os.path.exists(dir['abs']+ '/requirements.txt'):
            file = open(dir['abs'] + '/requirements.txt', "w")
        else:
            print('Arquivo requirements.txt já existe no diretório!')

try:
    pwd = str(input('Digite o diretório do projeto: ').strip())        
except KeyboardInterrupt:

    print('Cancelado pelo usuário')             
try:
    if __name__=="__main__":
        construtor(pwd)
except NameError:
    pass