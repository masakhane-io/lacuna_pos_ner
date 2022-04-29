from collections import Counter
def read_file(input_file):
    print(input_file)
    with open(input_file, encoding='utf-8') as f:
        text_lines = f.read().splitlines()

    sentences = [sent for sent in text_lines[:3600]]
    print(len(sentences))
    return set(sentences)

def read_file_entity(input_file):
    print(input_file)
    with open(input_file, encoding='utf-8') as f:
        text_lines = f.read().splitlines()

    sentences = [sent for sent in text_lines]

    old_sentences = list(set(sentences[3146:]))
    new_sentences = sentences[:3146]

    dict_sent = Counter(new_sentences)
    print(len(dict_sent), len(old_sentences), sum(dict_sent.values()))
    sort_dic_sent = sorted(dict_sent.items(), key=lambda x: x[1], reverse=True)

    for sent, num in dict_sent.items():
        if num>1:
            print(num, sent)
    print(len(set(sentences)))

    print("IN OLD SENTENCES: ")
    for sent in dict_sent:
        if sent in old_sentences:
            print(sent)

    with open('language_corpus/twi/twi_2.txt', 'w') as f:
        for sent in sentences:
            f.write(sent+'\n')



#read_file_entity("language_corpus/twi/twi_ghana.txt")
#read_file_entity("language_corpus/twi/englist_texts1.txt")
print(len(read_file("language_corpus/twi/twi.txt")))


print(len(read_file("language_corpus/twi/twi_all.txt")))
'''
print(len(read_file("language_corpus/bbj/bbj.txt")))
print(len(read_file("language_corpus/ewe/ewe.txt")))
print(len(read_file("language_corpus/fon/fon.txt")))
print(len(read_file("language_corpus/hau/hau.txt")))
print(len(read_file("language_corpus/ibo/ibo.txt")))
print(len(read_file("language_corpus/kin/kin.txt")))
print(len(read_file("language_corpus/lin/lin.txt")))
print(len(read_file("language_corpus/lug/lug.txt")))
print(len(read_file("language_corpus/luo/luo.txt")))
print(len(read_file("language_corpus/mos/mos.txt")))
print(len(read_file("language_corpus/nya/nya.txt")))
print(len(read_file("language_corpus/pcm/pcm.txt")))
print(len(read_file("language_corpus/sna/sna.txt")))
print(len(read_file("language_corpus/swa/swa.txt")))
print(len(read_file("language_corpus/tsn/tsn.txt")))
print(len(read_file("language_corpus/wol/wol.txt")))
print(len(read_file("language_corpus/xho/xho.txt")))
print(len(read_file("language_corpus/yor/yor.txt")))
print(len(read_file("language_corpus/zul/zul.txt")))
'''