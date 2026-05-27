from flask import Flask, render_template, request
import time

app = Flask(__name__)

# Naive String Matching Algorithm
def naive_string_match(txt, pat):

    m = len(txt)
    n = len(pat)

    steps = []
    comparisons = 0

    for i in range(m - n + 1):

        current = txt[i:i+n]

        comparisons += 1

        step = {
            "position": i,
            "current": current,
            "pattern": pat,
            "match": current == pat
        }

        steps.append(step)

        if current == pat:

            return {
                "found": True,
                "index": i,
                "steps": steps,
                "comparisons": comparisons
            }

    return {
        "found": False,
        "index": -1,
        "steps": steps,
        "comparisons": comparisons
    }

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        txt = request.form["text"]
        pat = request.form["pattern"]

        stime = time.time()

        result = naive_string_match(txt, pat)

        etime = time.time()

        result["execution_time"] = round(etime - stime, 6)
        result["text"] = txt
        result["pattern_input"] = pat

    return render_template("index.html", result=result)

app = app

if __name__ == "__main__":
    app.run(debug=True)