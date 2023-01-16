import markdown2 as markdown2
from django.shortcuts import render, redirect

from . import util


def index(request):
    query = request.GET.get("q")
    if query:
        return redirect("search")
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })



def page(request, entry):
    entry_body = util.get_entry(entry)
    if entry is None:
        return render(request, "encyclopedia/404.html")
    else:
        entry_html = markdown2.markdown(entry_body)
        return render(request, "encyclopedia/entry.html", {
            "entry_html": entry_html,
            "entry_title": entry
        })

def search(request):
    query = request.GET.get("q")
    if query is None:
        return redirect("index")
    entries = util.list_entries()
    matches = []
    for entry in entries:
        if query.lower() in entry.lower():
            matches.append(entry)
    if len(matches) == 1:
        return redirect(f"wiki/{matches[0]}")
    else:
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "matches": matches
        })

