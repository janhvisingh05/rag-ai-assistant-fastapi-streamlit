def rewrite_query(query: str, history: str = "") -> str:
    q = query.strip().lower()

    # expand vague queries
    rules = {
        "how to setup": "how to set up android device android 5.0 lollipop",
        "setup": "android device initial setup steps lollipop",
        "battery": "android battery saver mode lollipop how it works",
        "notifications": "android notifications lollipop how to use",
        "material design": "android lollipop material design explanation",
    }

    for k, v in rules.items():
        if k in q:
            return v

    # default prefix (anchors to your corpus)
    return f"android 5.0 lollipop guide: {query}"