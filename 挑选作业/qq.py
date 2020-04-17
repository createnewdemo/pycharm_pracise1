import re


def read_txt_file(fpath):
    lines = open(fpath, "r", encoding='utf-8').readlines()
    return lines

def read_ast_file(fpath):
    lines = open(fpath, "r", encoding='utf-8').readlines()
    return lines



if __name__ == '__main__':

    # read txt and ast files
    txt_lines = read_txt_file("0001.txt")
    ast_lines = read_ast_file("0001.ast")

t=0
a=0

for line in ast_lines:
        # parse line of ast files
        # c="cad/chf" 111:1 111:1||t="problem"||a="present"
        apart, bpart, cpart = line.strip().split('||')

        concept_type = bpart.split("=")[1]
        assertion_type = cpart.split("=")[1]


        b, c = apart[apart.index('\" ')+2:].split(' ')
        sent_idx = int(b.split(':')[0])
        token_idx_start = int(b.split(':')[1])
        token_idx_end   = int(c.split(':')[1])

        # 获取对应的句子原文信息
        sent_text = txt_lines[ sent_idx-1 ]
        sent_tokens = sent_text.split(' ')

        # 获取标注的实体原文信息
        concept_term = ' '.join( sent_tokens[ token_idx_start: token_idx_end+1 ]).strip()
        concept_term_marked = '||' + concept_term + '||'


        # 输入语义类型是"否定"或"可能"的句子
        if re.search("absent|possible|conditional|hypothetical|someone_else", assertion_type):
            print("\n\n******************")
            print("concept: %s ; assertion: %s" % (concept_term, assertion_type))
            print("sent_idx", sent_idx)
            print(sent_text.replace(concept_term, concept_term_marked))
