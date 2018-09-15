


def save_to_text(data):
    file = open('xxx.txt', 'a', encoding='utf-8')
    file.write('\n'.join(data))
    file.write('\n'+'='*50 + '\n')
    file.close()