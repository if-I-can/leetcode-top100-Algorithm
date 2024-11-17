from langchain.llms import OpenAI

llm = OpenAI(openai_api_key="Rsk-CWnCSl5mjc2KNMC52cA9697dC84845168b41D093A176A190")


from langchain.llms import OpenAI

llm = OpenAI(model_name="text-davinci-003",max_tokens=1024)
llm("怎么评价人工智能")

