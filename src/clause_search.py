import argparse, pickle, re
from pathlib import Path
import numpy as np
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def paragraphs(path):
    if path.suffix.lower()==".pdf":
        text="\n".join((p.extract_text() or "") for p in PdfReader(str(path)).pages)
    else:
        text=path.read_text(errors="replace")
    parts=[re.sub(r"\s+"," ",x).strip() for x in re.split(r"\n\s*\n",text)]
    return [p for p in parts if len(p)>40]

def build(folder,out):
    docs=[]
    for p in Path(folder).rglob("*"):
        if p.is_file() and p.suffix.lower() in {".pdf",".txt",".md"}:
            for i,txt in enumerate(paragraphs(p)):
                docs.append({"source":str(p),"section":i+1,"text":txt})
    if not docs: raise ValueError("No clauses found.")
    vec=TfidfVectorizer(stop_words="english",ngram_range=(1,2))
    matrix=vec.fit_transform([d["text"] for d in docs])
    Path(out).mkdir(parents=True,exist_ok=True)
    with open(Path(out)/"clauses.pkl","wb") as f: pickle.dump({"docs":docs,"vec":vec,"matrix":matrix},f)

def search(out,q,k):
    with open(Path(out)/"clauses.pkl","rb") as f:data=pickle.load(f)
    scores=cosine_similarity(data["vec"].transform([q]),data["matrix"])[0]
    for i in np.argsort(scores)[::-1][:k]:
        d=data["docs"][int(i)]
        print(f"\nScore {scores[i]:.3f} | {d['source']} | passage {d['section']}\n{d['text']}")

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest="cmd",required=True)
    a=sub.add_parser("index"); a.add_argument("folder"); a.add_argument("--index-dir",default="index")
    s=sub.add_parser("search"); s.add_argument("index_dir"); s.add_argument("query"); s.add_argument("--top-k",type=int,default=5)
    x=ap.parse_args(); build(x.folder,x.index_dir) if x.cmd=="index" else search(x.index_dir,x.query,x.top_k)
if __name__=="__main__":main()
