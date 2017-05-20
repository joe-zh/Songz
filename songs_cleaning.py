def clean():
  lines = []
  with open('songs.csv', 'r') as f:
    lines = f.readlines()

  clean_lines = []
  clean_lines.append(lines[0])
  for i in range(1, len(lines)):
    s = lines[i].lower()
    l = s.split('\t')
    tmp = l[0].strip() + '\t' + l[1].strip() + '\t' + l[2].strip() + '\t' +  l[3].strip() + '\n'
    clean_lines.append(tmp)
  with open('songs_clean.csv','w') as f:
    for i in range(0, len(clean_lines)):
      f.write(clean_lines[i])


if __name__ == "__main__":
  clean()
