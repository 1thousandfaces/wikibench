#actually runs wikibench!
#params: model_name, start_page, end_page OR path_list

#running thru openrouter

#importsQ
import os
import json

#class ModelRunner
class ModelRunner:
    def __init__(self, api_key=None):
        #init api clients
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"

    def run_model(model_name, start_page, end_page, use_tools=False):
        return

#init, run_model

if __name__ == "__main__":
    runner = ModelRunner()
    
    # Test with Claude
    result = runner.run_model(
        model_name="claude-sonnet-4",
        start_page="Bradawl",
        use_tools=False
    )
    
    print(json.dumps(result, indent=2))