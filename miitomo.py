#import the list
from sys import argv
from tabulate import tabulate
import json

def main():
    print('Hello')
    _ , d = argv
    with open(d, 'r') as dictionary:
        emotions = 0
        emotion_dict = dict()
        for line in dictionary:
            if len(line.split(' ')) == 3:
                e = line.split(' ')[1][3:]
                if e not in emotion_dict:
                    # print(line.split(' ')[0][:-2].replace('_', ' '))
                    emotion_dict[e] = [line.split(' ')[0][:-2].replace('_', ' ')]
                else:
                    emotion_dict[e] += [line.split(' ')[0][:-2].replace('_', ' ')]
                emotions += 1
        # print(emotion_dict['Clown'])
        # html_content(emotion_dict)
        html_tabs(emotion_dict)
        # print('There are {} words associated with emotions'.format(emotions))
        # print('Here are the emotions and the number of times each is referenced: ')
        # print(tabulate({'emotes': emotion_dict.keys(), 'occurences': emotion_dict.values()}, tablefmt='grid'))
        # for emote, occurence in emotion_dict.items():
        #     print('{}\t\t\t{}'.format(emote, occurence))

def html_tabs(data):
    html = '<ul class="nav nav-tabs" role="tablist">'
    for key in sorted(data.keys()):
        html += '<li role="presentation"><a href="#{}" aria-controls="{}" role="tab" data-toggle="tab">{} ({})</a></li>'.format(key.lower(), key.lower(), key, len(data[key]))
    html += '</ul>'
    print(html)

def html_content(data):
    html = '<div class="tab-content">'
    for key in sorted(data.keys()):
        html += '<div role="tabpanel" class="tab-pane fade flex" id="{}"></div>'.format(key.lower())
        html_words(key, data)
    html += '</div>'
    print(html)

def html_words(key, data):
    with open('{}.json'.format(key.lower()), 'w') as f:
        f.write(json.dumps(sorted(data[key])))


if __name__ == '__main__':
    main()
