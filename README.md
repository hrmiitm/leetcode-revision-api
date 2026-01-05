# LeetCode Random Solved Questions API

A small FastAPI-based serverless API deployed on Vercel that returns random solved LeetCode questions for a given user.

---

## API Endpoint

```
GET /api/{leetcodeid}/{n}
```

### Example

```
https://your-project.vercel.app/api/hrmiitm/5
```

### Response

```json
[
  {
    "title": "Two Sum",
    "link": "https://leetcode.com/problems/two-sum/"
  }
]
```

---

## Tech Used

* Python
* FastAPI
* Vercel Serverless Functions

---

## Run Locally

```bash
pip install fastapi requests uvicorn

uvicorn api.index:app --reload
```

Open:

```
http://127.0.0.1:8000/hrmiitm/3
```

---

## Note

This project uses publicly accessible LeetCode GraphQL endpoints.
It is **not an official LeetCode API**.

