from fastapi import FastAPI, HTTPException
import requests
import random

app = FastAPI()


@app.get("/{leetcodeid}/{n}")
def get_random_solved_questions(leetcodeid: str, n: int):
    if n <= 0:
        raise HTTPException(status_code=400, detail="n must be positive")

    url = "https://leetcode.com/graphql"

    query = """
    query recentAcSubmissions($username: String!) {
      recentAcSubmissionList(username: $username, limit: 100) {
        title
        titleSlug
        timestamp
      }
    }
    """

    payload = {
        "query": query,
        "variables": {
            "username": leetcodeid
        }
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Referer": f"https://leetcode.com/{leetcodeid}/"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail="Failed to fetch data from LeetCode"
        )

    data = response.json()
    submissions = data.get("data", {}).get("recentAcSubmissionList", [])

    if not submissions:
        return []

    # remove duplicates
    unique = {}
    for s in submissions:
        unique[s["titleSlug"]] = s["title"]

    problems = list(unique.items())
    n = min(n, len(problems))

    selected = random.sample(problems, n)

    return [
        {
            "title": title,
            "link": f"https://leetcode.com/problems/{slug}/"
        }
        for slug, title in selected
    ]
