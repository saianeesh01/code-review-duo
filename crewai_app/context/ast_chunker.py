from tree_sitter import Language, Parser
from pathlib import Path
from ..config import BASE_DIR, CHUNK_LINES

BUILD_SO = BASE_DIR / "build" / "my-languages.so"
LANGS    = ["python", "javascript"]          # add more grammars here

def _build():
    if not BUILD_SO.exists():
        vendor = BASE_DIR / "vendor"
        Language.build_library(str(BUILD_SO),
                               [str(vendor / f"tree-sitter-{l}") for l in LANGS])

_build()

PARSERS = {l: Parser() for l in LANGS}
for lang in LANGS:
    PARSERS[lang].set_language(Language(str(BUILD_SO), lang))

def chunk_file(path: Path) -> list[dict]:
    """Return [{'text':..., 'meta':{'file':..., 'line':start}}]"""
    code = path.read_text(encoding="utf-8", errors="ignore")
    lang = path.suffix.lstrip(".")
    if lang not in PARSERS:
        return []
    tree  = PARSERS[lang].parse(bytes(code, "utf-8"))
    root  = tree.root_node
    lines = code.splitlines()
    chunks = []
    start = 0
    for i in range(0, len(lines), CHUNK_LINES):
        chunk = "\n".join(lines[i:i+CHUNK_LINES])
        chunks.append({"text": chunk,
                       "meta": {"file": str(path), "line": i+1}})
    return chunks
