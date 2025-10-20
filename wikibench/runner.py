#actually runs wikibench!
#params: model_name, start_page, end_page OR path_list

#running thru openrouter

#importsQ
import os
import json
from openai import OpenAI
from .validator import validate_path 

#class ModelRunner
class ModelRunner:
    def __init__(self, api_key=None):
        #init api clients
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        self.base_url = "https://openrouter.ai/api/v1"
        self.client = OpenAI(base_url = self.base_url, api_key = self.api_key)

    def run_model(self, model_name, start_page, end_page, use_tools=False):
        completion = self.client.chat.completions.create(
            extra_body={},
            model=f"{model_name}",
            messages=[
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": f"Let’s play the Wiki Game! I will give you the name of a Wikipedia page. If you were to have access to this page, what links do you think you would click to get to {end_page}? Map out the path you would take, perhaps describing your thought process as needed. \n Then, write your final answer in the format: FINAL_ANSWER: start_page, page_2, page_3, ..., end_page \n Replace the spaces in the page titles with underscores and specify disambiguations as needed, such that we can esaily check it against the actual Wikipedia links. Don't include anything after you write your final answer. Ready? Let’s start with the page: {start_page}"
                    }
                ]
                }
            ]
        )
        #print(completion.choices[0].message.content)
        return completion.choices[0].message.content


#init, run_model

if __name__ == "__main__":
    runner = ModelRunner()
    
    # Test with Claude
    result = runner.run_model(
        model_name="anthropic/claude-sonnet-4.5",
        start_page="Bradawl",
        end_page="Kevin Bacon",
        use_tools=False
    )
    
    print(json.dumps(result, indent=2))

    print(validate_path(result))

    """result = runner.run_model(
        model_name="openai/gpt-5",
        start_page="Bradawl",
        end_page="Kevin Bacon",
        use_tools=False
    )
    
    print(json.dumps(result, indent=2))"""