"""Inventory reorder analyzer with an iTunes API spot check."""

from typing import Optional

import requests


ITUNES_SEARCH_URL = "https://itunes.apple.com/search"


def main() -> None:
    student_key = input("Student key: ")
    seed = sum(ord(ch) for ch in student_key.strip())

    if seed % 3 == 0:
        threshold = 15
    elif seed % 3 == 1:
        threshold = 12
    else:
        threshold = 9

    total_skus = 0
    reorder_count = 0

    while True:
        sku = input("SKU: ").strip()
        if not sku:
            print("SKU cannot be blank.")
            continue
        if sku == "DONE":
            break

        while True:
            try:
                on_hand = int(input("On hand: ").strip())
                if on_hand >= 0:
                    break
                print("On-hand quantity must be at least 0.")
            except ValueError:
                print("Enter a whole-number on-hand quantity.")

        total_skus += 1
        if on_hand < threshold:
            reorder_count += 1
            print("REORDER")
        else:
            print("OK")

    term = "weezer" if seed % 2 == 0 else "drake"
    songs_returned: Optional[int] = None
    api_status = "FAILED"

    try:
        response = requests.get(
            ITUNES_SEARCH_URL,
            params={"entity": "song", "limit": 5, "term": term},
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException:
        pass
    else:
        try:
            data = response.json()
        except ValueError:
            api_status = "INVALID_RESPONSE"
        else:
            results = data.get("results") if isinstance(data, dict) else None
            if isinstance(results, list) and all(
                isinstance(result, dict) and isinstance(result.get("kind"), str)
                for result in results
            ):
                songs_returned = sum(
                    result["kind"] == "song" for result in results
                )
                api_status = "OK"
            else:
                api_status = "INVALID_RESPONSE"

    songs_output = songs_returned if songs_returned is not None else "N/A"
    print(f"Seed: {seed}")
    print(f"Threshold: {threshold}")
    print(f"SKUs entered: {total_skus}")
    print(f"Reorder flagged: {reorder_count}")
    print(f"Spotcheck term: {term}")
    print(f"Songs returned: {songs_output}")
    print(f"API status: {api_status}")


if __name__ == "__main__":
    main()
