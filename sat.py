def clean():
  lines = []
  with open('song_artists_tags.csv', 'r') as f:
    lines = f.readlines()

  clean_lines = []
  clean_aux_lines = []
  clean_lines.append(lines[0][:25] + 'tags_id"\n')
  clean_aux_lines.append('"id"\t"tag"\n')
  for i in range(1, len(lines)):
    #strip off final '\n'
    s = lines[i][:len(lines[i])-1].lower()
    l = s.split('\t')
    tmp = l[0].strip() + '\t' + l[1].strip() + '\t' + l[2].strip() + '\t' + str(i) + '\n'
    clean_lines.append(tmp)
    for j in range(3, len(l)):
      tag = l[j].strip()
      if tag[len(tag)-1] == '*':
          tag = tag[:len(tag)-1]
      s2 = str(i) + '\t' + tag + '\n'
      clean_aux_lines.append(s2)

  with open('song_artists_tags_clean.csv','w') as f:
    for i in range(0, len(clean_lines)):
      f.write(clean_lines[i])

  with open('tags_clean.csv', 'w') as f:
    for i in range(0, len(clean_aux_lines)):
      f.write(clean_aux_lines[i])





if __name__ == "__main__":
  clean()
