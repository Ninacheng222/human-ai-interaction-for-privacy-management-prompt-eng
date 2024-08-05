from prompt_eng import prompt

if __name__ == "__main__":

    import json
    f = open('sample_data/sample.json')
    data = json.load(f)
    f.close()

    input_json_first = {
        "conversion_type": "first",
        "ocr_json": data,
        "user_input":"",
        "conversation_history":[]
    }

    result = prompt(input_json_first)
    print("frist result:", result[0]['masks'])
    
    input_json_continued = {
        "conversion_type": "continued",
        "ocr_json": data,
        "user_input": "name and adress only",
        "conversation_history": result[0]['conversation_history']
    }
    
    result = prompt(input_json_continued)
    print("second result:", result[0]['masks'])