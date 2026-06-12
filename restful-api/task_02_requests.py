#!/usr/bin/python3
"""
Fetch and process posts from JSONPlaceholder API.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts and print their titles.
    """
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch all posts and save them into posts.csv.
    """
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    if response.status_code == 200:
        posts = response.json()

        data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        with open(
            "posts.csv",
            mode="w",
            newline="",
            encoding="utf-8"
        ) as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=["id", "title", "body"]
            )

            writer.writeheader()
            writer.writerows(data)