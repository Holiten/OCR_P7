from text_parser.parser import Parser
from goog_api.goog_api import GoogleApi
from wiki_api.wiki_api import WikiApi


def workflow(text):
    p = Parser(text)

    google_args = p.call_all_methods()
    g = GoogleApi()

    wiki_args = g.google_coords
    g_lat = g.google_lat
    g_long = g.google_long

    w = WikiApi()
    wiki_results = w.wiki_fetch_infos(wiki_args)

    return text, google_args, wiki_args, g_lat, g_long, wiki_results


