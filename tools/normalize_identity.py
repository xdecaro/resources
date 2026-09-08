from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
R=(("decaroresources","xdecaroresources"),("DECARORESOURCES","XDECARORESOURCES"),("Decaroresources","Resources"),("0.1.0","0.2.0"))
S={".php",".xml",".ini",".md",".json",".yml",".yaml",".txt",".sql",".sh"}
def ig(p): return ".git" in p.parts or ".github" in p.parts or p==Path(__file__)
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or ig(p) or (p.suffix.lower() not in S and p.name!='VERSION'): continue
    t=p.read_text(encoding='utf-8'); n=t
    for a,b in R:n=n.replace(a,b)
    if n!=t:p.write_text(n,encoding='utf-8')
for p in sorted((x for x in ROOT.rglob('*') if not ig(x)),key=lambda x:len(x.parts),reverse=True):
    n=p.name
    for a,b in R:n=n.replace(a,b)
    if n!=p.name:p.rename(p.with_name(n))
