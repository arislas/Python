from pathlib import Path

path = Path('10/learning_python.txt')
contenido = path.read_text(encoding='utf-8')

lines = contenido.splitlines()

for line in lines:
    print(line.replace('python', 'C'))