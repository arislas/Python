from pathlib import Path

path = Path('10/learning_python.txt')
contenido = path.read_text(encoding='utf-8')

for line in contenido.splitlines():
    print(line)