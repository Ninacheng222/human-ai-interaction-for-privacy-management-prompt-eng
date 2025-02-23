from prompt_eng import prompt
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='The JSON file to process')
    args = parser.parse_args()
    # print(args)

    import json
    f = open('sample_data/'+args.filename)
    data = json.load(f)
    f.close()

    input_json_first = {
        "conversion_type": "first",
        "ocr_json": data['pages'][0],
        "user_input":"",
        "conversation_history":[]
    }

    result = prompt(input_json_first)
    print("frist result:", result[0]['masks'])
    
    input_json_continued = {
        "conversion_type": "continued",
        "ocr_json": data['pages'][0],
        "user_input": "name and institution only",
        # "user_input": """Also hide "123 Maple Street", and ”Springfield, IL 62704" separately while having the original address""",
        "conversation_history": result[0]['conversation_history']
    }
    
    result = prompt(input_json_continued)
    print("second result:", result[0]['masks'])