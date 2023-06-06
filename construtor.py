import os


def construtor():
    
    dir = {}
    dir['src'] = 'src'
    dir['tests'] = 'tests'
    dir['docs'] = 'docs'
    dir['abs'] = os.getcwd()

    file1 = '/__init__.py'
    file2 = '/module1.py'
    file3 = '/module2.py'

    test_file1 = '/test_modulo1.py'
    test_file2 = '/test_modulo2.py'

    docs_file1 = '/index.md'
    docs_file2 = '/user_guide.md'
    docs_file3 = '/contribution_guide.md'

    for c in range(len(dir)):
        dir_src = os.path.join(dir['abs'], dir['src'])
        dir_tests = os.path.join(dir['abs'], dir['tests'])
        dir_docs = os.path.join(dir['abs'], dir['docs'])

    if not os.path.exists(dir_src):
        os.makedirs(dir_src)
        file = open(dir_src + file1, "w")
        file = open(dir_src + file2, "w")
        file = open(dir_src + file3, "w")
        file.close()
        print('Diretório SRC criado com sucesso! ')

    else:
        print(f'Ja existem o diretório {dir["src"]} ')
    
    if not os.path.exists(dir_tests):
        os.makedirs(dir_tests)
        file = open(dir_tests + test_file1, 'w')
        file = open(dir_tests + test_file2, "w")
        file.close()
        print('Diretório TESTS criado com sucesso! ')
    
    else:
        print(f'Ja existem o diretório {dir["tests"]} ')
    
    if not os.path.exists(dir_docs):
        os.makedirs(dir_docs)
        file = open(dir_docs + docs_file1, 'w')
        file = open(dir_docs + docs_file2, "w")
        file = open(dir_docs + docs_file3, "w")
        file = open(dir['abs'] + '/README.md', "w")
        file.close()
        print('Diretório DOCS criado com sucesso! ')

    else:
        print(f'Ja existem o diretório {dir["docs"]} ')

    

construtor()
