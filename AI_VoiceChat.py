import os

from dotenv import load_dotenv
load_dotenv()
replicate_api_key = os.getenv("Replicate_API_KEY")
os.environ["REPLICATE_API_TOKEN"] = replicate_api_key

import replicate

if __name__ == "__main__":    
    
    prompt = """
    You Are A helpful assistant.
    just chitchatting with this desperate lonely pathetic egyptian person 
    and wants to cheer him up
    """

    output = replicate.run(
        "meta/llama-2-70b-chat",
        input = {"prompt": prompt},
    )

    # The output is just array of strings
    print(''.join(output))
