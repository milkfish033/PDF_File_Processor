from volcenginesdkarkruntime import Ark

# fetch ak&sk from environmental variables "VOLC_ACCESSKEY", "VOLC_SECRETKEY"
# or specify ak&sk by Ark(ak="${YOUR_AK}", sk="${YOUR_SK}").
# you can get ak&sk follow this document(https://www.volcengine.com/docs/6291/65568)

client = Ark(ak="**********", sk="****************") replace youor own Ark here

def QA(text, c)->str:
  
    answer = ""
    stream = client.chat.completions.create(
    model="************", #replace your own model here 
    messages=[
        {
            "role": "user",
            "content": f"{c}: {text}"
        },
    ],
      
    stream=True,
    temperature=1,
    top_p=0.7,
    )
  
    for chunk in stream:
        if not chunk.choices:
            continue
        answer += chunk.choices[0].delta.content
    return answer


